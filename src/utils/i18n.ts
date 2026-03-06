import { getLocale } from "astro-i18n-aut";
import { defaultLocale } from "../config/i18n";
import { translations } from "../i18n/translations";

export function getPreferredLocale(url: URL): string {
  return getLocale(url) || defaultLocale;
}

export function t(
  key: keyof typeof translations.en,
  locale: string = defaultLocale
): string {
  return (
    translations[locale as keyof typeof translations][key] ||
    translations[defaultLocale][key]
  );
}
