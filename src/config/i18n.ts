export const locales = {
  es: "Español",
  en: "English",
} as const;

export const defaultLocale = "es" as const;

// Configuración del subdirectorio base
export const basePath = "";

export function getLanguageName(locale: string): string {
  const langMap: Record<string, string> = {
    es: "Español",
    en: "English",
  };
  return langMap[locale] || locale;
}

export function getLanguageCode(locale: string): string {
  return locale.split("-")[0].toUpperCase();
}

export type Locale = keyof typeof locales;
