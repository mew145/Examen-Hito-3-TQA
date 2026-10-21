# -*- coding: utf-8 -*-
"""Caja blanca - Hito 3 TQA.

Ejecuta los 3 casos diseñados (CB-001 .. CB-003) mas el caso adicional
CB-004 propuesto para completar la cobertura de decisiones (100 %).

Uso: python scripts/validar_compra.py
"""

MENSAJE_EDAD = "Compra no permitida: edad"
MENSAJE_CUENTA = "Compra no permitida: cuenta"
APROBADA = "Compra aprobada"
RECHAZADA = "Compra rechazada"


def validar_compra(edad, cuenta_activa, saldo, monto):
    """Fragmento de codigo proporcionado en el examen."""
    if edad < 18:
        return MENSAJE_EDAD
    if not cuenta_activa:
        return MENSAJE_CUENTA
    if saldo >= monto and monto > 0:
        return APROBADA
    return RECHAZADA


CASOS = [
    # id, edad, cuenta_activa, saldo, monto, resultado esperado, decision cubierta
    ("CB-001", 17, True, 100, 50, MENSAJE_EDAD, "D1 = V"),
    ("CB-002", 25, False, 100, 50, MENSAJE_CUENTA, "D1 = F, D2 = V"),
    ("CB-003", 30, True, 200, 100, APROBADA, "D2 = F, D3 = V"),
    ("CB-004", 30, True, 50, 100, RECHAZADA, "D3 = F (ajuste propuesto)"),
]


def main():
    print(f"{'ID':<8}{'Entradas':<45}{'Esperado':<32}{'Obtenido':<32}{'Estado':<8}Cubre")
    print("-" * 145)
    for cid, edad, activa, saldo, monto, esperado, cubre in CASOS:
        obtenido = validar_compra(edad, activa, saldo, monto)
        estado = "PASS" if obtenido == esperado else "FAIL"
        entradas = f"edad={edad}, cuenta_activa={activa}, saldo={saldo}, monto={monto}"
        print(f"{cid:<8}{entradas:<45}{esperado:<32}{obtenido:<32}{estado:<8}{cubre}")


if __name__ == "__main__":
    main()
