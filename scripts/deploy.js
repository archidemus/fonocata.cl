import { Client } from "basic-ftp";
import readline from "readline";
import { execSync } from "child_process";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Configuración de cPanel
const config = {
    host: "cpsingenieria.cl", // o la IP: "200.83.167.89"
    user: "cpsingen",
    port: 21,
    remoteRoot: "public_html", // Carpeta en cPanel donde se subirá el proyecto
    localRoot: path.join(__dirname, "..", "dist")
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const askPassword = () => {
    return new Promise((resolve) => {
        rl.question(`🔑 Ingresa la contraseña de cPanel/FTP para el usuario '${config.user}': `, (pass) => {
            resolve(pass.trim());
        });
    });
};

const runCommand = (command) => {
    console.log(`\n🚀 Ejecutando: ${command}`);
    try {
        execSync(command, { stdio: "inherit" });
    } catch (error) {
        console.error("❌ Error ejecutando el comando:", error);
        process.exit(1);
    }
};

async function deploy() {
    console.log("\n📦 1. Construyendo la aplicación...");
    runCommand("bun run build");

    console.log("\n🌐 2. Preparando subida por FTP...");
    const password = await askPassword();
    rl.close();

    if (!password) {
        console.error("❌ La contraseña es obligatoria.");
        process.exit(1);
    }

    const client = new Client();
    client.ftp.verbose = true;

    try {
        console.log(`\n🔄 Conectando a ${config.host}...`);
        await client.access({
            host: config.host,
            user: config.user,
            password: password,
            secure: false // Cambiar a true si el servidor requiere FTPS explícito
        });

        console.log(`✅ Conectado exitosamente.`);
        
        console.log(`📂 Navegando a /${config.remoteRoot}...`);
        await client.ensureDir(config.remoteRoot);
        await client.clearWorkingDir(); // Opcional: Esto borra los archivos viejos

        console.log(`📤 Subiendo archivos desde '${config.localRoot}'...`);
        console.log(`⏳ Esto puede tomar un momento dependiendo de tu conexión.`);
        await client.uploadFromDir(config.localRoot);

        console.log("\n🎉 ¡Despliegue completado con éxito! 🎉");
    }
    catch (err) {
        console.error("\n❌ Error durante el despliegue:", err);
    }
    finally {
        client.close();
    }
}

deploy();
