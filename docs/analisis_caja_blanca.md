# Análisis de caja blanca — Hito 3 TQA

**Código bajo análisis:** fragmento proporcionado en el examen (función `validar_compra`).

```python
def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:
        return "Compra no permitida: edad"
    if not cuenta_activa:
        return "Compra no permitida: cuenta"
    if saldo >= monto and monto > 0:
        return "Compra aprobada"
    return "Compra rechazada"
```

---

## 1. Identificación de decisiones y condiciones simples

| Elemento | Definición | Tipo |
|---|---|---|
| **D1** | `if edad < 18:` | Decisión |
| **C1** | `edad < 18` | Condición simple de D1 |
| **D2** | `if not cuenta_activa:` | Decisión |
| **C2** | `cuenta_activa` (evaluada negada: `not cuenta_activa`) | Condición simple de D2 |
| **D3** | `if saldo >= monto and monto > 0:` | Decisión compuesta (operador `and`) |
| **C3** | `saldo >= monto` | Condición simple de D3 |
| **C4** | `monto > 0` | Condición simple de D3 |

**Resumen:** 3 decisiones y 4 condiciones simples. D3 es una decisión compuesta porque combina dos condiciones con `and` (evaluación de cortocircuito: si `C3` es falsa, `C4` no se evalúa).

### Caminos posibles (una sola salida por ejecución)

| Camino | Condición del flujo | Salida |
|---|---|---|
| P1 | D1 = V | `"Compra no permitida: edad"` |
| P2 | D1 = F y D2 = V | `"Compra no permitida: cuenta"` |
| P3 | D1 = F, D2 = F y D3 = V | `"Compra aprobada"` |
| P4 | D1 = F, D2 = F y D3 = F | `"Compra rechazada"` |

---

## 2. Criterio utilizado

**Criterio elegido: cobertura de decisiones** (complementado con la cobertura de sentencias, que se alcanza de forma automática).

> *Cobertura de decisiones:* cada decisión del código debe tomar **ambos** resultados posibles (verdadero y falso) al menos una vez.

### Cálculo del mínimo de casos

| Decisión | Resultados a cubrir | Cantidad |
|---|---|---|
| D1 (`edad < 18`) | Verdadero, Falso | 2 |
| D2 (`not cuenta_activa`) | Verdadero, Falso | 2 |
| D3 (`saldo >= monto and monto > 0`) | Verdadero, Falso | 2 |
| **Total** | | **6 resultados de decisión** |

Cada caso de prueba ejecuta **un único camino** y, como la función tiene un solo `return` por camino, **cada ejecución cubre exactamente una salida**. Como existen **4 caminos disjuntos (P1–P4)** y cada camino es la única forma de obtener cada salida, el mínimo teórico de casos para 100 % de cobertura de decisiones es:

> **Mínimo = 4 casos** (uno por cada camino/salida). Con 4 casos se cubren los 6 resultados de decisión y, de forma simultánea, se alcanza el **100 % de cobertura de sentencias** (las 4 sentencias `return` se ejecutan).

No existe un mínimo universal: el número depende del código y del criterio elegido. Por ejemplo, si se eligiera **cobertura de condiciones** (que C1–C4 tomen V y F), serían necesarios **5 casos**, porque D3 exige cubrir por separado `saldo >= monto = F`, `monto > 0 = F` y ambos verdaderos (ver sección 5).

---

## 3. Los 3 casos diseñados (con valores concretos)

| ID | edad | cuenta_activa | saldo | monto | Resultado esperado | Condición / decisión que cubre |
|---|---|---|---|---|---|---|
| **CB-001** | `17` | `True` | `100` | `50` | `"Compra no permitida: edad"` | **D1 = V** (C1 = V) |
| **CB-002** | `25` | `False` | `100` | `50` | `"Compra no permitida: cuenta"` | **D1 = F**, **D2 = V** (C1 = F, C2 = V) |
| **CB-003** | `30` | `True` | `200` | `100` | `"Compra aprobada"` | **D2 = F**, **D3 = V** (C2 = F, C3 = V, C4 = V) |

### Tabla de cobertura alcanzada con los 3 casos

| Resultado de decisión | CB-001 | CB-002 | CB-003 | ¿Cubierto? |
|---|---|---|---|---|
| D1 = V | ✔ | | | ✅ |
| D1 = F | | ✔ | ✔ | ✅ |
| D2 = V | | ✔ | | ✅ |
| D2 = F | | | ✔ | ✅ |
| D3 = V | | | ✔ | ✅ |
| **D3 = F** | | | | ❌ **No cubierto** |

**Cobertura lograda: 5 de 6 resultados de decisión = 83,3 %.** Ninguno de los 3 casos alcanza la salida `"Compra rechazada"`, por lo que el criterio de cobertura de decisiones **no se completa**.

---

## 4. Ajuste necesario para completar el criterio

Se requiere **un caso adicional (CB-004)** que recorra el camino P4:

| ID | edad | cuenta_activa | saldo | monto | Resultado esperado | Cubre |
|---|---|---|---|---|---|---|
| **CB-004** | `30` | `True` | `50` | `100` | `"Compra rechazada"` | **D3 = F** (saldo insuficiente: `50 >= 100` es falso) |

Con CB-004 se obtiene **100 % de cobertura de decisiones (6/6)** y 100 % de cobertura de sentencias. Con 3 casos es matemáticamente imposible llegar al 100 %: son 4 caminos disjuntos y cada caso sólo recorre uno.

---

## 5. Nota: si el criterio fuera cobertura de condiciones

| Condición simple | Valores que debe tomar |
|---|---|
| C1 `edad < 18` | V y F |
| C2 `cuenta_activa` | V y F |
| C3 `saldo >= monto` | V y F |
| C4 `monto > 0` | V y F |

Para cubrir C3 = F y C4 = F **por separado** hacen falta dos ejecuciones distintas de P4 (por ejemplo `saldo=50, monto=100` y `saldo=100, monto=0`), lo que eleva el mínimo a **5 casos**:

| Caso | edad | cuenta_activa | saldo | monto | Salida | Condiciones nuevas que cubre |
|---|---|---|---|---|---|---|
| CB-001 | 17 | True | 100 | 50 | no permitida: edad | C1 = V |
| CB-002 | 25 | False | 100 | 50 | no permitida: cuenta | C1 = F, C2 = V |
| CB-003 | 30 | True | 200 | 100 | aprobada | C2 = F, C3 = V, C4 = V |
| CB-004 | 30 | True | 50 | 100 | rechazada | C3 = F, C4 = V |
| CB-005 | 30 | True | 100 | 0 | rechazada | C3 = V, C4 = F |

**Conclusión:** no confundir cobertura de decisiones con cobertura de condiciones. La decisión compuesta D3 tiene **2 resultados** (V/F), pero sus **2 condiciones** exigen casos adicionales para cubrir cada valor de forma independiente.

---

## 6. Ejecución de los casos (verificación)

Los 3 casos (CB-001 a CB-003) fueron ejecutados contra la función real en Python (`scripts/validar_compra.py`); la tabla de resultados se encuentra en [casos_caja_blanca_resultados.md](casos_caja_blanca_resultados.md).
