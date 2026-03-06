import { execSync } from 'child_process';
import fs from 'fs';
import archiver from 'archiver';
import path from 'path';

// Función para ejecutar comandos
const runCommand = (command) => {
  try {
    execSync(command, { stdio: 'inherit' });
  } catch (error) {
    console.error('❌ Error ejecutando el comando:', error);
    process.exit(1);
  }
};

// Función para comprimir la carpeta dist
const compressDist = () => {
  const output = fs.createWriteStream('dist.zip');
  const archive = archiver('zip', {
    zlib: { level: 9 }, // Nivel máximo de compresión
  });

  output.on('close', () => {
    console.log('✅ Archivo ZIP creado exitosamente');
    console.log(
      `📦 Tamaño total: ${(archive.pointer() / 1024 / 1024).toFixed(2)} MB`,
    );
  });

  archive.on('error', (err) => {
    throw err;
  });

  archive.pipe(output);
  archive.directory('dist/', false);
  archive.finalize();
};

// Ejecutar el proceso
console.log('🚀 Iniciando build...');
runCommand('bun run build');
console.log('📦 Comprimiendo carpeta dist...');
compressDist();
