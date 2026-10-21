# -*- coding: utf-8 -*-
"""
Examen Practico Hito 3 - TQA
Verificaciones exploratorias de defectos (independientes entre si).

Uso: python scripts/explorar_defectos.py
Salidas: evidencias/capturas/expl_*.png y scripts/exploracion.json
"""

import json
import pathlib
from datetime import datetime

from playwright.sync_api import sync_playwright

BASE = "https://www.saucedemo.com/"
RAIZ = pathlib.Path(__file__).resolve().parent.parent
CAPTURAS = RAIZ / "evidencias" / "capturas"
USUARIO, CLAVE = "standard_user", "secret_sauce"


def shot(page, nombre):
    page.screenshot(path=str(CAPTURAS / nombre))
    return nombre


def login(page):
    page.goto(BASE)
    page.fill("#user-name", USUARIO)
    page.fill("#password", CLAVE)
    page.click("#login-button")
    page.wait_for_load_state("networkidle")


def ir_a_checkout(page):
    login(page)
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.wait_for_load_state("networkidle")
    page.click("#checkout")
    page.wait_for_load_state("networkidle")


def explorar_espacios(page):
    """EX-1: campos del checkout con solo espacios en blanco."""
    ir_a_checkout(page)
    page.fill("#first-name", "   ")
    page.fill("#last-name", "   ")
    page.fill("#postal-code", "   ")
    captura = shot(page, "expl_01_checkout_solo_espacios.png")
    page.click("#continue")
    page.wait_for_load_state("networkidle")
    avanzo = "checkout-step-two" in page.url
    captura2 = shot(page, "expl_01b_resultado_espacios.png")
    return {
        "id": "EX-1",
        "escenario": "Checkout con campos (nombre, apellido y codigo postal) que contienen solo espacios en blanco",
        "esperado": "El formulario deberia rechazar valores sin contenido real y mostrar 'Error: First Name is required'",
        "obtenido": ("Se aceptaron los campos con solo espacios y se avanzo al resumen de la compra"
                     if avanzo else "El formulario rechazo los campos y mostro el mensaje de error"),
        "capturas": [captura, captura2],
        "reproducible": avanzo,
    }


def explorar_logout(page):
    """EX-2: tras cerrar sesion, navegar hacia atras con el navegador."""
    login(page)
    try:
        page.click("#react-burger-menu-btn", timeout=8000)
        page.wait_for_timeout(500)
        page.click("#logout_sidebar_link", timeout=8000)
    except Exception:
        # Respaldo: limpiar la sesion y volver al login
        page.goto(BASE + "logout.html")
    page.wait_for_load_state("networkidle")
    captura1 = shot(page, "expl_02_logout.png")
    en_login = "saucedemo.com" in page.url and "inventory" not in page.url
    page.go_back()
    page.wait_for_load_state("networkidle")
    captura2 = shot(page, "expl_03_tras_logout_atras.png")
    protegida = "inventory.html" not in page.url
    return {
        "id": "EX-2",
        "escenario": "Tras cerrar sesion, usar el boton 'Atras' del navegador",
        "esperado": "No debe mostrarse el catalogo sin una sesion activa",
        "obtenido": ("La sesion caduco y se redirige al login" if protegida
                     else "Se mostro el catalogo sin sesion activa"),
        "capturas": [captura1, captura2],
        "reproducible": not protegida,
        "nota": f"Tras logout se estaba en la pagina de login: {en_login}",
    }


def explorar_orden(page):
    """EX-3: el ordenamiento del catalogo se conserva al agregar un producto al carrito."""
    login(page)
    page.select_option(".product_sort_container", "za")
    page.wait_for_load_state("networkidle")
    primero_antes = page.locator(".inventory_item_name").first.inner_text()
    captura1 = shot(page, "expl_04_orden_za.png")
    page.locator(".inventory_item_name").first.locator("xpath=../../..").locator("button").click()
    page.wait_for_timeout(400)
    primero_despues = page.locator(".inventory_item_name").first.inner_text()
    captura2 = shot(page, "expl_05_orden_tras_agregar.png")
    conserva = primero_antes == primero_despues
    return {
        "id": "EX-3",
        "escenario": "Ordenar el catalogo de Z a A y luego agregar el primer producto al carrito",
        "esperado": "El ordenamiento 'Name (Z to A)' deberia conservarse tras la accion",
        "obtenido": (f"El ordenamiento se conserva (primero: {primero_despues})" if conserva
                     else f"El ordenamiento se reinicio: antes '{primero_antes}', despues '{primero_despues}'"),
        "capturas": [captura1, captura2],
        "reproducible": not conserva,
    }


def main():
    resultados = []
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        contexto = navegador.new_context(viewport={"width": 1440, "height": 900})
        page = contexto.new_page()
        for nombre, funcion in (("EX-1", explorar_espacios), ("EX-2", explorar_logout),
                                ("EX-3", explorar_orden)):
            try:
                resultados.append(funcion(page))
            except Exception as exc:  # noqa: BLE001
                resultados.append({"id": nombre, "escenario": nombre, "esperado": "-",
                                   "obtenido": str(exc), "capturas": [], "reproducible": False})
        navegador.close()

    salida = RAIZ / "scripts" / "exploracion.json"
    salida.write_text(json.dumps({"fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
                                  "verificaciones": resultados}, ensure_ascii=False, indent=2),
                      encoding="utf-8")
    for r in resultados:
        print(f"[{'DEFECTO' if r['reproducible'] else 'OK'}] {r['id']}: {r['escenario']}")
        print(f"    Obtenido: {r['obtenido']}")
    print(f"Guardado en {salida}")


if __name__ == "__main__":
    main()
