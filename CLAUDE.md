# Fonocata.cl — Landing Catalina Orellana

Landing page profesional de **Catalina Orellana Molnar**, fonoaudióloga clínica.
Tratamiento fonoaudiológico integral: voz, deglución, comunicación y cuidados paliativos.

## Stack

- Runtime: `bun`
- Framework: Astro 5.x + TailwindCSS v4
- Fuentes: Nunito (headings) + Inter (body) via Google Fonts
- Hosting: GitHub Pages (deploy automático) + FTP a cPanel (manual)

## Comandos

```bash
bun install
bun run dev          # Dev server
bun run build        # Build estático
bun run build:zip    # Build + comprime dist/ en dist.zip
bun run deploy       # Build + deploy por FTP a cPanel
bun run backup       # Backup
bun run format       # Prettier
```

## Estructura

```
src/
├── pages/index.astro       # Landing (una sola página)
├── layouts/Layout.astro    # HTML base, SEO, Meta Pixel, JSON-LD
├── components/
│   ├── Header.astro        # Nav sticky con menú mobile
│   ├── Hero.astro          # Sección principal + CTA WhatsApp
│   ├── Services.astro      # 4 servicios (voz, deglución, cognición, paliativos)
│   ├── About.astro         # Bio + formación (Vocología UANDES, Vía Aérea USS)
│   ├── InstagramFeed.astro # Feed via Behold.so API
│   └── Footer.astro        # Contacto + redes + links
├── assets/                  # Imágenes optimizadas (webp)
└── styles/global.css        # Tailwind import
```

## Deploy

- **GitHub Pages**: automático al push a `main` via GitHub Actions
- **cPanel (cpsingenieria.cl)**: manual con `bun run deploy`, sube `dist/` por FTP

## Datos de contacto

- WhatsApp: +56 9 5632 0835
- Email: catalina.orellanamol@gmail.com
- Instagram: [@fonocata.cl](https://instagram.com/fonocata.cl)
- LinkedIn: [catalina-orellana-molnar](https://www.linkedin.com/in/catalina-orellana-molnar-16028022b/)
- Dominio: fonocata.cl

## Servicios

1. **Voz y Vocología** — alteraciones vocales, síndrome de laringe irritable
2. **Deglución y Disfagia** — rehabilitación, vía aérea artificial
3. **Cognición y Comunicación** — estimulación lenguaje adultos, neuroplasticidad
4. **Cuidados Paliativos y Fin de Vida** — evaluación comunicación, confort

## Formación

- Fonoaudióloga, Universidad Mayor
- Diplomado en Vocología, Universidad de Los Andes
- Diplomado en Manejo de Vía Aérea Artificial, Universidad San Sebastián

## SEO y analytics

- Schema.org JSON-LD (MedicalBusiness)
- Open Graph + Twitter Cards
- Sitemap automático (plugin @astrojs/sitemap)
- Meta Pixel (ID: 889855824021683)

## Integraciones externas

- **Behold.so**: feed de Instagram (`https://feeds.behold.so/y8ZzL88DSZ0CiTE3F0K3`)
- **Google Fonts**: Nunito + Inter

## Notion

Workspace Podis: `2ac703eceeec809cb467de7f7678cd85`

## Wiki

Documentación de marca, contenido y estrategia en `wiki/`.

## Convenciones

- Mensajes de commit en español o inglés, descriptivos
- Branch principal: `main`
- Formateo con Prettier (config en `.prettierrc`)
