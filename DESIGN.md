---
name: Serene Care
colors:
  surface: '#f8f9ff'
  surface-dim: '#ccdbf4'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dde9ff'
  surface-container-highest: '#d5e3fd'
  on-surface: '#0d1c2f'
  on-surface-variant: '#4c4452'
  inverse-surface: '#233144'
  inverse-on-surface: '#ebf1ff'
  outline: '#7d7483'
  outline-variant: '#cec3d3'
  surface-tint: '#7b41b4'
  primary: '#7b41b4'
  on-primary: '#ffffff'
  primary-container: '#c084fc'
  on-primary-container: '#500989'
  inverse-primary: '#ddb8ff'
  secondary: '#765469'
  on-secondary: '#ffffff'
  secondary-container: '#fdd0ea'
  on-secondary-container: '#79576c'
  tertiary: '#505f76'
  on-tertiary: '#ffffff'
  tertiary-container: '#90a0b9'
  on-tertiary-container: '#27374b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0dbff'
  primary-fixed-dim: '#ddb8ff'
  on-primary-fixed: '#2c0051'
  on-primary-fixed-variant: '#62259b'
  secondary-fixed: '#ffd8ed'
  secondary-fixed-dim: '#e5bad3'
  on-secondary-fixed: '#2c1325'
  on-secondary-fixed-variant: '#5c3d51'
  tertiary-fixed: '#d3e4fe'
  tertiary-fixed-dim: '#b7c8e1'
  on-tertiary-fixed: '#0b1c30'
  on-tertiary-fixed-variant: '#38485d'
  background: '#f8f9ff'
  on-background: '#0d1c2f'
  surface-variant: '#d5e3fd'
  background-subtle: '#F8FAFC'
  text-heading: '#0F172A'
  lavender-light: '#E9D5FF'
  pink-light: '#FCE7F3'
typography:
  display-lg:
    fontFamily: Nunito Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Nunito Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Nunito Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-md:
    fontFamily: Nunito Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  container-padding: 20px
  gutter: 16px
---

## Brand & Style

The design system is built on a foundation of empathy, professionalism, and warmth, specifically tailored for a speech therapy (fonoaudióloga) practice. The brand personality is approachable yet clinical, ensuring patients and families feel both supported and confident in the expertise provided. 

The design style follows a **Modern Soft-Minimalism** approach. It utilizes generous whitespace to reduce cognitive load—essential for users seeking therapy services—while incorporating subtle **Glassmorphism** and soft tonal layering. The aesthetic avoids harsh edges and aggressive contrasts, opting instead for a calming, rhythmic interface that feels "human" and fluid. This is achieved through the use of soft pastel transitions, rounded geometries, and high-quality, legible typography.

## Colors

This design system employs a palette of "Professional Pastels." The primary color is a soft lavender (#C084FC), chosen for its associations with creativity and tranquility. The secondary pink (#FBCFE8) provides a warm, nurturing accent, ideal for pediatric and elderly care contexts. 

The color logic follows a 60-30-10 rule:
- **60% (Base):** #F8FAFC serves as the primary canvas, providing a crisp, clean medical feel without the sterile coldness of pure white.
- **30% (Support):** Lavender and Pink are used for interactive elements, soft containers, and decorative flourishes.
- **10% (Emphasis):** Deep Slate (#0F172A) is reserved strictly for high-contrast typography and essential functional icons to ensure accessibility.

## Typography

The typography strategy pairs the friendly, rounded terminals of **Nunito Sans** for headings with the systematic clarity of **Inter** for body text. 

**Headlines:** Nunito Sans conveys a gentle, approachable voice. Use tighter letter-spacing for larger display sizes to maintain a modern look.
**Body & Data:** Inter is used for all functional text to ensure maximum legibility across different screen densities. Its neutral character balances the "playfulness" of the lavender and pink palette, maintaining professional authority.
**Hierarchy:** Use font weight (Semi-Bold to Bold) rather than size alone to distinguish between information levels, ensuring a clean and organized layout.

## Layout & Spacing

This design system utilizes a **Fluid-Responsive Grid** centered on a 4px baseline unit. 

- **Mobile:** A 4-column grid with 20px side margins and 16px gutters. Mobile layouts should prioritize vertical stacking and easily tappable "thumb-zones."
- **Tablet:** An 8-column grid with 32px margins. Components can begin to sit side-by-side (e.g., card grids).
- **Desktop:** A 12-column fixed-max grid (1280px) with auto-margins.

Spacings are designed to be generous. Avoid crowding content; "breathable" layouts are a functional requirement to reduce anxiety for patients navigating the application. Use `xl` (32px) and `2xl` (48px) spacing between major sections to clearly delineate service offerings and contact forms.

## Elevation & Depth

Depth in this design system is created through **Tonal Layering** and **Soft Ambient Shadows** rather than stark borders.

1.  **Surfaces:** The background uses #F8FAFC. Secondary containers (like cards) use pure white (#FFFFFF).
2.  **Shadows:** Use extremely soft, tinted shadows. Instead of neutral grey, shadows should have a tiny hint of the primary lavender (`rgba(192, 132, 252, 0.08)`). Shadows should have large blur radii (16px–32px) and minimal offsets to simulate a gentle float.
3.  **Glassmorphism:** For top navigation bars and floating action buttons, use a backdrop blur effect (8px–12px) with a semi-transparent white fill (opacity 80%). This maintains a sense of place and modern sophistication.

## Shapes

The shape language is defined by "The Rounded Edge." Sharp corners are strictly avoided to maintain the empathetic and friendly personality of the practice.

- **Standard Elements (Buttons, Inputs):** 0.5rem (8px) corner radius.
- **Large Elements (Cards, Modals):** 1rem (16px) corner radius.
- **Icon Enclosures & Avatars:** Always circular or "squircle" (high-roundedness) to reinforce the organic, human nature of the brand.

Interaction states (like hover or active) should never sharpen the corners; they should remain consistent to keep the UI predictable and soft.

## Components

**Buttons:** Primary buttons use a solid Lavender (#C084FC) fill with white text. Secondary buttons use a light Pink (#FCE7F3) background with Lavender text. All buttons should have a minimum height of 48px for mobile accessibility and feature rounded-md corners.

**Input Fields:** Use a subtle background fill (#F1F5F9) instead of heavy borders. On focus, transition the background to white and add a 2px lavender soft-glow outline.

**Cards:** Cards are the primary vessel for service descriptions and therapist bios. They should feature a white background, the "Rounded" (1rem) corner radius, and a soft ambient shadow. Avoid "ghost" borders unless the card is placed on a pure white background.

**Chips/Badges:** Use for session types (e.g., "Online," "In-person"). Use the secondary pink or lavender with 10% opacity as a background and the full-strength color for the text.

**Lists:** Use generous vertical padding (16px) between list items. Instead of solid line dividers, use 1px horizontal rules in #F1F5F9 or simple whitespace separation.

**Progress Indicators:** For therapy milestones or onboarding, use soft-rounded bars with a lavender-to-pink gradient to make clinical progress feel rewarding and positive.