# Ejecución de los casos de caja blanca — Hito 3 TQA

**Script:** `scripts/validar_compra.py` (ejecuta la función `validar_compra` real en Python)
**Fecha de ejecución:** 20/10/2026
**Ejecutado por:** Yuri Rojas (GitHub: mew145)

```
ID      Entradas                                            Esperado                        Obtenido                        Estado  Cubre
-------------------------------------------------------------------------------------------------------------------------------------------------
CB-001  edad=17, cuenta_activa=True, saldo=100, monto=50    Compra no permitida: edad       Compra no permitida: edad       PASS    D1 = V
CB-002  edad=25, cuenta_activa=False, saldo=100, monto=50   Compra no permitida: cuenta     Compra no permitida: cuenta     PASS    D1 = F, D2 = V
CB-003  edad=30, cuenta_activa=True, saldo=200, monto=100   Compra aprobada                 Compra aprobada                 PASS    D2 = F, D3 = V
CB-004  edad=30, cuenta_activa=True, saldo=50, monto=100    Compra rechazada                Compra rechazada                PASS    D3 = F (ajuste propuesto)
```

## Tabla resumen

| ID | edad | cuenta_activa | saldo | monto | Resultado esperado | Resultado obtenido | Estado | Qué cubre |
|---|---|---|---|---|---|---|---|---|
| CB-001 | 17 | True | 100 | 50 | Compra no permitida: edad | Compra no permitida: edad | ✅ PASS | D1 = V |
| CB-002 | 25 | False | 100 | 50 | Compra no permitida: cuenta | Compra no permitida: cuenta | ✅ PASS | D1 = F, D2 = V |
| CB-003 | 30 | True | 200 | 100 | Compra aprobada | Compra aprobada | ✅ PASS | D2 = F, D3 = V |
| CB-004 | 30 | True | 50 | 100 | Compra rechazada | Compra rechazada | ✅ PASS | D3 = F (caso adicional propuesto) |

## Interpretación

- Los **3 casos solicitados** (CB-001 a CB-003) devolvieron **exactamente el resultado esperado**: PASS.
- Cobertura alcanzada con los 3 casos: **5 de 6 resultados de decisión = 83,3 %**. El resultado no cubierto es **D3 = F** (salida "Compra rechazada").
- Con el **caso adicional CB-004** se completa el **100 % de cobertura de decisiones** (y también el 100 % de cobertura de sentencias).

Ver el análisis completo en [analisis_caja_blanca.md](analisis_caja_blanca.md).
