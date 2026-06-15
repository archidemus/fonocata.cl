# Informe de Verificación — Plan de Rescate vs. Antecedentes

**Plan revisado:** `plan-rescate-financiero-13jun2026.md`
**Antecedentes:** carpeta `antecedentes13dejunio/` (13 documentos)
**Extracciones detalle:** carpeta `extracciones/` (un `.md` por documento)
**Fecha del análisis:** 14 de junio de 2026

---

## Resumen ejecutivo

El plan es **parcialmente confiable**: las cifras del CAE, crédito de consumo y cuotas TC facturadas son correctas, pero contiene **3 errores graves** que cambian el diagnóstico financiero y la viabilidad del plan:

1. 🔴 **Liquidez subestimada 10×**: el plan dice **$12.486**; el saldo contable real al 13/06 es **$122.486**.
2. 🔴 **La tarjeta de crédito NO está en cero**: el plan la da por saldada ("TC de arrastre en CERO"), pero el **cupo utilizado real al 13/06 es $1.703.839**, con uso activo durante junio.
3. 🔴 **Confunde AFP con Isapre**: el pago de **$404.174 es de cotizaciones AFP PlanVital** (para activar el convenio CAE), **no de la Isapre Colmena**. Son obligaciones distintas.

Además, el plan **subestima los gastos de supervivencia** ($500.000/mes vs. ~$1.000.000/mes reales) y omite un **traspaso de $405.000 a Lia el 09/06** *(aclarado: pago de Isapre vía Lia)*.

---

## Verificación ítem por ítem

### ✅ Datos correctos en el plan

| Afirmación del plan | Documento que lo confirma | Veredicto |
|---------------------|---------------------------|:---------:|
| Deuda CAE $15.038.642 | `convenioCAE.txt` (extr. 10) | ✅ |
| Expediente 19359-2026 | `DEMANDA.pdf` (extr. 02) | ✅ |
| Embargo despachado 03/06/2026 | `DEMANDA.pdf` (extr. 02) | ✅ |
| Deuda CAE original $14.152.803 | `DEMANDA.pdf` (extr. 02, giro 04/12/2024) | ✅ |
| Convenio: pie $1M + 23 cuotas $173.524 | `convenioCAE.txt` (extr. 10) | ✅ |
| Monto convenio $4.991.052 / saldo $10.047.590 | `convenioCAE.txt` (extr. 10) | ✅ |
| Ingreso anual F22 $20.822.862 | `convenioCAE.txt` (extr. 10) | ✅ |
| TC arrastre facturado $502.688, pagado 09/06 | `Mov_Facturado.xls` + cartola | ✅ |
| Avance TC $235.042, cuota 1/6, termina nov | `Mov_Facturado.xls` (extr. 03) | ✅ |
| Salcobrand $61.923 en 3 cuotas | `Mov_Facturado.xls` (extr. 03) | ✅ |
| Crédito consumo $136.549/mes, al día | `informeCredito.pdf` (extr. 11) | ✅ |
| Ingreso por honorarios ~$1,5M/mes | cartola (proveedores 0690703017) | ✅ |
| Línea de crédito pagada, usada como puente | cartolas mayo/junio | ✅ |

### 🔴 Errores graves (corrigen el diagnóstico)

#### Error 1 — Liquidez real es 10× mayor

| Plan | Real | Fuente |
|------|------|--------|
| **$12.486** | **$122.486** | `cartola.txt`: `SALDO CONTABLE` al 13/06 |

> El plan leyó mal el campo (omitieron un dígito o dividieron por error). La caja disponible real es **$110.000 más** de lo que el plan cree. Esto cambia la factibilidad de varias acciones de junio.

#### Error 2 — La TC NO está en cero

| Plan | Real | Fuente |
|------|------|--------|
| "TC de arrastre en CERO" (logro) ✅ | **Cupo utilizado $1.703.839** al 13/06 | `Saldo_y_Mov_No_Facturado.xls` (extr. 04) |

> La factura de mayo ($502.688) sí se pagó, pero **la tarjeta siguió usándose y arrastra ~$1,7M de deuda** (cuotas del Avance $1,18M + Salcobrand $124K + Megasalud $135K + compras rotativas nuevas $262K). El plan oculta esto. En los primeros 13 días de junio hubo cargos nuevos por **~$280.000** (FORUSSA $88K, EXPRESS PD $59,6K, TOKU/METLIFE $30K, Uber Eats, Canva, supermercados…), pese a que el plan dice "cerrar llave TC".

#### Error 3 — Confusión AFP vs. Isapre

| Plan dice | Realidad | Fuente |
|-----------|----------|--------|
| "Las cotizaciones previsionales ($404.174) son la Isapre" | Los $404.174 son **AFP PlanVital** (jubilación), pagados para activar el convenio CAE | `comprobantePago.pdf` (extr. 09) + `Cotizaciones cata.pdf` (extr. 01) |
| "Isapre Colmena … feb-may pagados" | Colmena (salud) tiene **solo evidencia de mayo** ($137.144, 12/05). No hay certificado de Colmena en los antecedentes. | `cartola_29052026.xls` (extr. 07) |

> **Dos obligaciones distintas:**
> - **AFP PlanVital** (jubilación): acreditados 05–12/2025; pagados 02–04/2026 el 09/06. **Faltan 01/2026, 05/2026, 06/2026.**
> - **Isapre Colmena** (salud): mayo pagado. Estado del resto **desconocido** (sin documento).

### 🟡 Errores menores / imprecisiones

| Ítem | Plan | Real | Comentario |
|------|------|------|------------|
| Crédito consumo cuotas restantes | 13 | **14** (incluyendo julio) | "Plazo pendiente 13" = 13 *después* de la cuota 5. Saldo $1.911.686 = 14 × $136.549. |
| Isapre junio pendiente "~$125.000" | $125K | Sin documento | Suposición, no verificable con los antecedentes. |
| Traspaso a Loreto (Mamá) junio | $355.000 | **$365.000** | ($300K + $55K + $10K). Error de suma menor. |
| Traspaso a Lia Orellana junio | $58.200 | **$422.700** | El plan omitió el traspaso de **$405.000 del 09/06** (solo sumó $17.700+$40.500). Dato crítico. |
| Gastos supervivencia | $500.000/mes | **~$1.000.000/mes** | Hogar+super+salud+transporte+servicios reales (sin lujos). Plan subestima 2×. |
| Compras TC mayo no mencionadas | — | ENEL $136.678, DECATHLON $17.600, MEGASALUD $15.276 | Compras contado facturadas en mayo. |
| Cotizaciones AFP pendientes | "solo junio" | **01/2026, 05/2026, 06/2026** (3 periodos) | Más de lo que el plan reconoce. |
| Fecha expediente "19359-2026" | ✅ | ✅ | — |

### 🟡 Datos del plan no verificables con estos antecedentes

- Monto exacto de Isapre Colmena de junio (~$125.000): **sin documento** que lo confirme.
- Que Isapre Colmena esté "al día" salvo junio: **sin certificado de Colmena** en los antecedentes.
- Naturaleza del traspaso de $405.000 a Lia Orellana: ~~el plan lo asume "gastos compartidos"~~ **Aclarado por Cata:** fue **pago de Isapre (Colmena) canalizado por Lia** (Cata no tenía autorizado transferir ese monto directo a la Isapre). Ya contabilizado como gasto de salud. Quedan $123,7K a Lia sin explicar.

---

## Impacto de los errores en el plan

El plan concluye que "cabe en el presupuesto" con ~$491K libres/mes. **Esto es falso** porque:

1. Usa gastos de supervivencia de $500K (lo real es ~$1.000K) → **sobreestima el libre en $500K**.
2. Ignora la deuda rotativa TC de $1,7M y su servicio mensual (intereses rotativos + compras nuevas).
3. Ignora 3 periodos AFP pendientes (~$400K) y la Isapre de junio.
4. El pie de $1M en julio genera un **déficit real de ~$640K** ese mes (ver `PLAN-DE-PAGO-CONFIABLE.md`, proyección).

**Conclusión:** el plan original es **demasiado optimista y no ejecutable tal cual**. Se necesita una versión corregida y conservadora (ver archivo adjunto).
