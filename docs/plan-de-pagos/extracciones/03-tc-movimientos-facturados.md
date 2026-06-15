# Extracción 03 — TC Visa Dorada: Movimientos Facturados

**Archivo origen:** `Mov_Facturado.xls`
**Titular:** Catalina Lucia Orellana Molnar · RUT 19.916.979-3
**Tarjeta:** Titular Visa Dorada `****7559`
**Estado:** Vigente o Activo

## Resumen de la factura

| Campo | Valor |
|-------|-------|
| Monto Facturado | **$502.688** |
| Pago Mínimo | $103 |
| Fecha de Facturación | 20/05/2026 |
| Pagar Hasta | 08/06/2026 |

> Esta factura se pagó íntegramente el 09/06/2026 (TEF $502.688, visible en cartola C/C y en movimientos no facturados como abono).

## Detalle de movimientos facturados (Nacionales)

| Fecha | Descripción | Cuotas | Monto ($) |
|-------|-------------|:------:|----------:|
| 15/05/2026 | Red Movilidad Santi Santiago | 01/01 | 815 |
| 13/05/2026 | ENEL SANTIAGO | 01/01 | **136.678** |
| 12/05/2026 | Pago Pesos TEF *(abono)* | 01/01 | 686.764 |
| 11/05/2026 | Pago PAP Cuenta Corriente *(abono)* | 01/01 | 22.006 |
| 09/05/2026 | LA POPULAR INFANTE SANTIAGO | 01/01 | 6.035 |
| 09/05/2026 | EXPRESS PD VALDIVIA SANTIAGO | 01/01 | 13.020 |
| 09/05/2026 | MEGASALUD PROV. MED SANTIAGO | 01/01 | 15.276 |
| 07/05/2026 | CANVA LAS CONDES | 01/01 | 7.900 |
| 01/05/2026 | N Y L SPA 11001 SANTIAG | 01/01 | 1.220 |
| 27/04/2026 | MERPAGO*DECATHLONCH LAS CONDES | 01/01 | 17.600 |
| 17/04/2026 | SALCOBRAND AV.11 DE TASA INT. 0,00% | **01/03** | 61.923 |
| 24/03/2026 | AVANCE EN CUOTAS TE TASA INT. 3,40% | **01/06** | 235.042 |
| 18/03/2026 | CURSOS EXTENSION CL TASA INT. 0,00% | **03/03** | 10.000 |
| 06/03/2026 | MERCADOPAGO*IRENEDE TASA INT. 0,00% | **02/03** | 7.333 |

## Cargos, comisiones e intereses (sumados a la factura)

| Fecha | Concepto | Monto ($) |
|-------|----------|----------:|
| 20/05/2026 | IMPUESTO DECRETO LEY 3475 (0,066%) | 457 |
| 20/05/2026 | COMISION MENSUAL POR MANTENCION | 3.638 |
| 20/05/2026 | INTERESES ROTATIVOS | 2.505 |
| 20/05/2026 | INTERESES DE MORA | 62 |
| 07/05/2026 | COMISION COMPRA INTERNACIONAL | 84 |
| 07/05/2026 | TRASPASO DEUDA INTERNACIONAL | 5.060 |
| 05/05/2026 | COMISION COMPRA INTERNACIONAL | 46 |

## Lectura clave de las cuotas en curso (extraída de los códigos X/Y)

| Compra | Código cuota facturada ahora | Significado |
|--------|------------------------------|-------------|
| Avance en Cuotas $235.042 | **01/06** | Esta fue la **cuota 1 de 6**. Quedan 5 cuotas (jul→nov). |
| Salcobrand $61.923 | **01/03** | Cuota **1 de 3**. Quedan 2 (jun, jul). |
| Cursos Extensión $10.000 | **03/03** | Cuota **3 de 3** (última). ✅ Ya terminó con este pago. |
| MercadoPago (Irenede) $7.333 | **02/03** | Cuota **2 de 3**. Queda 1 (jun). |

## Observaciones de extracción

- La factura incluye una compra grande no mencionada en el plan: **ENEL $136.678** (13/05, cuenta de luz).
- También omite: MERPAGO*DECATHLON $17.600, MEGASALUD $15.276 (contado), EXPRESS PD VALDIVIA $13.020.
- Hay **intereses de mora $62**, indicio de atraso en algún ciclo anterior.
- "TRASPASO DEUDA INTERNACIONAL $5.060" sugiere que se pasó deuda en USD al saldo en pesos.
