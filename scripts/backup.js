import { Client } from 'basic-ftp';
import readline from 'readline';
import path from 'path';
import fs from 'fs';
import archiver from 'archiver';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Configuración de cPanel
const config = {
  host: 'cpsingenieria.cl',
  user: 'cpsingen',
  port: 21,
  remoteRoot: 'public_html', // Carpeta en cPanel que se quiere respaldar (la raíz)
  backupDir: path.join(__dirname, '..', 'backups'), // Carpeta local para guardar los respaldos
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const askPassword = () => {
  return new Promise((resolve) => {
    rl.question(
      `🔑 Ingresa la contraseña de cPanel/FTP para el usuario '${config.user}': `,
      (pass) => {
        resolve(pass.trim());
      },
    );
  });
};

const compressBackup = (sourceDir, outPath) => {
  return new Promise((resolve, reject) => {
    console.log('📦 Comprimiendo el respaldo...');
    const output = fs.createWriteStream(outPath);
    const archive = archiver('zip', { zlib: { level: 9 } });

    output.on('close', () => {
      console.log(`✅ Respaldo comprimido exitosamente: ${outPath}`);
      console.log(
        `📦 Tamaño: ${(archive.pointer() / 1024 / 1024).toFixed(2)} MB`,
      );

      // Opcional: limpiar la carpeta temporal no comprimida
      fs.rmSync(sourceDir, { recursive: true, force: true });

      resolve();
    });

    archive.on('error', (err) => reject(err));

    archive.pipe(output);
    archive.directory(sourceDir, false);
    archive.finalize();
  });
};

async function backup() {
  console.log('\n🛡️  Iniciando proceso de respaldo desde cPanel...');

  // Asegurar que la carpeta de backups exista
  if (!fs.existsSync(config.backupDir)) {
    fs.mkdirSync(config.backupDir, { recursive: true });
  }

  const password = await askPassword();
  rl.close();

  if (!password) {
    console.error('❌ La contraseña es obligatoria.');
    process.exit(1);
  }

  const client = new Client();
  // client.ftp.verbose = true; // Descomentar para debug detallado

  // Crear nombres basados en timestamp
  const dateStr = new Date().toISOString().replace(/[:.]/g, '-');
  const tempBackupFolder = path.join(
    config.backupDir,
    `backup_temp_${dateStr}`,
  );
  const finalZipPath = path.join(
    config.backupDir,
    `backup_raiz_${dateStr}.zip`,
  );

  try {
    console.log(`\n🔄 Conectando a ${config.host}...`);
    await client.access({
      host: config.host,
      user: config.user,
      password: password,
      secure: false,
    });

    console.log(`✅ Conectado exitosamente.`);

    console.log(`📂 Verificando directorio remoto /${config.remoteRoot}...`);
    await client.cd(config.remoteRoot);

    console.log(`📥 Descargando archivos a una carpeta temporal...`);
    console.log(
      `⏳ Esto puede tomar tiempo dependiendo del tamaño del sitio y tu conexión.`,
    );

    // Crear carpeta temporal
    fs.mkdirSync(tempBackupFolder, { recursive: true });

    await client.downloadToDir(tempBackupFolder);

    console.log('✅ Descarga completada.');

    // Comprimir el respaldo y luego limpiar la carpeta temporal
    await compressBackup(tempBackupFolder, finalZipPath);

    console.log('\n🎉 ¡Respaldo completado con éxito! 🎉');
  } catch (err) {
    console.error('\n❌ Error durante el respaldo:', err);
    // Intentar limpiar en caso de error crítico
    if (fs.existsSync(tempBackupFolder)) {
      try {
        fs.rmSync(tempBackupFolder, { recursive: true, force: true });
      } catch (e) {}
    }
  } finally {
    client.close();
  }
}

backup();
