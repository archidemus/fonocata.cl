# Extracción 13 — Reglas del Convenio CAE (sin registros de renta)

**Archivo origen:** `reglasCAE.txt` (texto de la página de TGR)

## Reglas generales

- Aplica a quienes **no registren declaración de renta**; deben presentar certificado de cotizaciones previsionales del año inmediatamente anterior (ene–dic).
- Las deudas morosas son las informadas por la **Comisión Ingresa**.

## Cálculo del pie (cuota de activación)

> El pie mínimo será el **mayor valor** entre **1 UTM** y **10%, 15% o 20%** de la deuda neta total del CAE, según comportamiento de pago previo.
> El pie puede aumentarse (sube el monto del convenio, sin alterar la cuota propuesta).
> El valor final de la cuota pie corresponde al **menor** entre el porcentaje de la deuda neta y el **tope de ingresos** de la tabla.

## Tabla de topes de ingresos para el pie

| Tramo de renta anual | Comportamiento bueno (10%) | Regular (15%) | Malo (20%) |
|----------------------|--------------------------:|--------------:|-----------:|
| $0 – $1.000.000 | 1 UTM | 1 UTM | 1 UTM |
| $1.000.001 – $2.000.000 | **$1.000.000** | $1.500.000 | $2.000.000 |
| $2.000.001 – $5.000.000 | $1.500.000 | $2.250.000 | $3.000.000 |

## Cuotas y caducidad

- Convenio en **hasta 24, 18 ó 12 cuotas** iguales (según comportamiento de pago).
- **Caducidad:** dos cuotas impagas o no pago de la cuota de ajuste.
- Si tramo de renta $0–$1M: cuota mínima = 1 UTM.

## Aplicación al caso de Cata

| Dato | Valor | Fuente |
|------|-------|--------|
| Ingreso anual año anterior | $20.822.862 | Convenio (extr. 10) |
| Tramo aplicable | $2.000.001 – $5.000.000 *(ingreso mensual aprox)* | — |

> ⚠️ **Nota de consistencia:** la tabla se interpreta sobre **renta mensual**. La renta anual de Cata ($20,8M) equivale a ~$1,7M/mes, que cae en el tramo **$1M–$2M** → tope de ingresos **$1.000.000** (buen comportamiento 10%). Esto explica el **pie de $1.000.000** de su propuesta.

## Observaciones de extracción

- ⚠️ Discrepancia con `package.pdf`: porcentajes **15%** aquí vs **12%** en el correo. No afecta a Cata (cae en 10%).
- El pie **no es negociable a la baja** (mínimo = mayor entre 1 UTM y el %/tope). **Sí puede aumentarse** para reducir la deuda residual.
- La **caducidad con 2 cuotas impagas** es el riesgo más alto: reactivaría el embargo inmediatamente.
