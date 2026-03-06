import sharp from "sharp";
import fs from "fs";
import path from "path";

const sourceDir = path.join(process.cwd(), "src", "assets");
const targetDir = path.join(process.cwd(), "src", "assets", "webp");

// Asegurarse de que el directorio de destino existe
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

// Obtener todos los archivos PNG
const files = fs.readdirSync(sourceDir).filter((file) => file.endsWith(".png"));

async function convertToWebP() {
  for (const file of files) {
    const inputPath = path.join(sourceDir, file);
    const outputPath = path.join(targetDir, file.replace(".png", ".webp"));

    try {
      await sharp(inputPath)
        .webp({ quality: 80 }) // Ajusta la calidad según necesites
        .toFile(outputPath);

      console.log(`Convertido: ${file} -> ${path.basename(outputPath)}`);
    } catch (error) {
      console.error(`Error al convertir ${file}:`, error);
    }
  }
}

convertToWebP().catch(console.error);
