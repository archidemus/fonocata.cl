// @ts-check
import { defineConfig } from "astro/config";
import { i18n } from "astro-i18n-aut/integration";
import tailwindcss from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "https://cpsingenieria.cl",
  vite: {
    plugins: [tailwindcss()],
  },
  integrations: [
    i18n({
      locales: {
        es: "es-ES",
        en: "en-US",
      },
      defaultLocale: "es",
      redirectDefaultLocale: true,
    }),
    sitemap(),
  ],
});
