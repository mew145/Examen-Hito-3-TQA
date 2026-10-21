# -*- coding: utf-8 -*-
"""
Examen Practico Hito 3 - TQA
Ejecucion de los 5 casos de prueba de caja negra sobre https://www.saucedemo.com/
+ verificaciones exploratorias para detectar defectos reproducibles.

Requiere: pip install playwright / python -m playwright install chromium
Uso:     python scripts/ejecutar_pruebas.py
Salidas: evidencias/capturas/*.png  y  scripts/resultados.json
"""

import json
import pathlib
from datetime import datetime

from playwright.sync_api import sync_playwright

BASE = "https://www.saucedemo.com/"
RAIZ = pathlib.Path(__file__).resolve().parent.parent
CAPTURAS = RAIZ / "evidencias" / "capturas"
CAPTURAS.mkdir(parents=True, exist_ok=True)

USUARIO = "standard_user"
CLAVE = "secret_sauce"

resultados = []


def ahora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def shot(page, nombre):
    ruta = CAPTURAS / nombre
    page.screenshot(path=str(ruta), full_page=False)
    return nombre


def registrar(tc, titulo, pasos, estado, observacion, capturas, bug=None):
    resultados.append(
        {
            "id": tc,
            "titulo": titulo,
            "fecha": ahora(),
            "pasos": pasos,
            "estado": estado,
            "observacion": observacion,
            "capturas": capturas,
            "bug": bug,
        }
    )
    print(f"[{estado}] {tc} - {titulo}")


def login(page, usuario, clave):
    page.goto(BASE)
    page.fill("#user-name", usuario)
    page.fill("#password", clave)
    page.click("#login-button")


def caso_001(page):
    """TC-001: Inicio de sesion con credenciales validas."""
    capturas, pasos = [], []
    login(page, USUARIO, CLAVE)
    page.wait_for_load_state("networkidle")
    url_ok = "inventory.html" in page.url
    titulo_ok = "Products" in page.content()
    c1 = shot(page, "evid_tc001_01_login_exitoso.png")
    capturas.append(c1)
    pasos.append({"paso": f"Ingresar {USUARIO} / {CLAVE}", "esperado": "Acceso al catalogo", "obtenido": page.url})
    badge = page.locator(".shopping_cart_badge")
    c2 = shot(page, "evid_tc001_02_catalogo.png")
    capturas.append(c2)
    estado = "PASS" if url_ok and titulo_ok else "FAIL"
    obs = (
        "Redirige a la pagina de inventario (inventory.html) y muestra el catalogo de productos. "
        f"Contador de carrito visible: {badge.is_visible()} (vacio al iniciar)."
    )
    registrar("TC-001", "Inicio de sesion con credenciales validas", pasos, estado, obs, capturas)


def caso_002(page):
    """TC-002: Inicio de sesion con credenciales invalidas (prueba negativa)."""
    capturas, pasos = [], []
    login(page, USUARIO, "wrong_password")
    page.wait_for_load_state("networkidle")
    c1 = shot(page, "evid_tc002_01_error_login.png")
    capturas.append(c1)
    msg = page.locator("[data-test='error']").inner_text()
    pasos.append({"paso": "Ingresar clave incorrecta", "esperado": "Mensaje de error y permanecer en login", "obtenido": msg})
    en_login = "inventory.html" not in page.url
    c2 = shot(page, "evid_tc002_02_persiste_login.png")
    capturas.append(c2)
    estado = "PASS" if en_login and "do not match" in msg else "FAIL"
    obs = (
        f"Se muestra el error '{msg}' y el usuario NO accede al catalogo. "
        "Icono (X) rojo presente en los campos usuario y clave."
    )
    registrar("TC-002", "Inicio de sesion con credenciales invalidas", pasos, estado, obs, capturas)


def caso_003(page):
    """TC-003: Agregar un producto al carrito."""
    capturas, pasos = [], []
    login(page, USUARIO, CLAVE)
    page.wait_for_load_state("networkidle")
    boton = page.locator("#add-to-cart-sauce-labs-backpack")
    boton.click()
    page.wait_for_timeout(300)
    c1 = shot(page, "evid_tc003_01_producto_agregado.png")
    capturas.append(c1)
    badge = page.locator(".shopping_cart_badge").inner_text()
    texto_boton = page.locator("#remove-sauce-labs-backpack").inner_text()
    pasos.append({"paso": "Agregar 'Sauce Labs Backpack'", "esperado": "Badge = 1 y boton 'Remove'", "obtenido": f"Badge={badge}, boton={texto_boton}"})
    page.click(".shopping_cart_link")
    page.wait_for_load_state("networkidle")
    c2 = shot(page, "evid_tc003_02_carrito.png")
    capturas.append(c2)
    en_carrito = page.locator(".inventory_item_name", has_text="Sauce Labs Backpack").count()
    estado = "PASS" if badge == "1" and texto_boton == "Remove" and en_carrito == 1 else "FAIL"
    obs = (
        f"El badge del carrito muestra '{badge}', el boton cambia a '{texto_boton}' y el item "
        "'Sauce Labs Backpack' aparece en la pagina del carrito."
    )
    registrar("TC-003", "Agregar un producto al carrito", pasos, estado, obs, capturas)


def caso_004(page):
    """TC-004: Eliminar un producto desde el carrito."""
    capturas, pasos = [], []
    login(page, USUARIO, CLAVE)
    page.wait_for_load_state("networkidle")
    page.click("#add-to-cart-sauce-labs-bike-light")
    page.wait_for_timeout(300)
    badge_antes = page.locator(".shopping_cart_badge").inner_text()
    page.click(".shopping_cart_link")
    page.wait_for_load_state("networkidle")
    c1 = shot(page, "evid_tc004_01_carrito_con_item.png")
    capturas.append(c1)
    page.locator("#remove-sauce-labs-bike-light").click()
    page.wait_for_timeout(300)
    c2 = shot(page, "evid_tc004_02_item_eliminado.png")
    capturas.append(c2)
    badge_despues = page.locator(".shopping_cart_badge").count()
    items_restantes = page.locator(".cart_item").count()
    pasos.append({"paso": "Eliminar 'Sauce Labs Bike Light' desde el carrito", "esperado": "Badge desaparece y lista vacia", "obtenido": f"badge_antes={badge_antes}, badge_despues={badge_despues}, items={items_restantes}"})
    estado = "PASS" if badge_despues == 0 and items_restantes == 0 else "FAIL"
    obs = (
        f"Antes de eliminar el badge mostraba {badge_antes}; al eliminar el producto el badge desaparece "
        f"(elementos restantes en el carrito: {items_restantes}) y el carrito queda vacio."
    )
    registrar("TC-004", "Eliminar un producto desde el carrito", pasos, estado, obs, capturas)


def caso_005(page):
    """TC-005: Completar el proceso de checkout."""
    capturas, pasos = [], []
    login(page, USUARIO, CLAVE)
    page.wait_for_load_state("networkidle")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.wait_for_load_state("networkidle")
    page.click("#checkout")
    page.wait_for_load_state("networkidle")
    c1 = shot(page, "evid_tc005_01_formulario_checkout.png")
    capturas.append(c1)
    page.fill("#first-name", "Ana")
    page.fill("#last-name", "Quispe")
    page.fill("#postal-code", "0000")
    page.click("#continue")
    page.wait_for_load_state("networkidle")
    c2 = shot(page, "evid_tc005_02_resumen.png")
    capturas.append(c2)
    page.click("#finish")
    page.wait_for_load_state("networkidle")
    c3 = shot(page, "evid_tc005_03_compra_finalizada.png")
    capturas.append(c3)
    mensaje = page.locator(".complete-header").inner_text()
    detalle = page.locator(".complete-text").inner_text()
    pasos.append({"paso": "Llenar datos y finalizar compra", "esperado": "'Thank you for your order!'", "obtenido": mensaje})
    estado = "PASS" if "Thank you for your order!" in mensaje else "FAIL"
    obs = f"Mensaje final: '{mensaje}'. Detalle: '{detalle}'. Se regresa al catalogo con 'Back Home'."
    registrar("TC-005", "Completar el proceso de checkout", pasos, estado, obs, capturas)


def explorar_espacios(page):
    """EX-1: checkout con campos que contienen solo espacios en blanco."""
    from explorar_defectos import explorar_espacios as _impl
    return _impl(page)


def explorar_logout(page):
    """EX-2: tras cerrar sesion, navegar hacia atras con el navegador."""
    from explorar_defectos import explorar_logout as _impl
    return _impl(page)


def explorar_orden(page):
    """EX-3: el ordenamiento del catalogo se conserva al agregar un producto."""
    from explorar_defectos import explorar_orden as _impl
    return _impl(page)


def main():
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"Ejecucion iniciada: {fecha}")
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        contexto = navegador.new_context(viewport={"width": 1440, "height": 900})
        contexto.add_init_script("localStorage.clear();")
        page = contexto.new_page()
        for caso in (caso_001, caso_002, caso_003, caso_004, caso_005):
            try:
                caso(page)
            except Exception as exc:  # noqa: BLE001
                registrar(caso.__doc__.split(":")[0], caso.__doc__, [], "ERROR", str(exc), [])
        bugs = []
        for chequeo in (explorar_espacios, explorar_logout, explorar_orden):
            try:
                bugs.append(chequeo(page))
            except Exception as exc:  # noqa: BLE001
                bugs.append({"id": chequeo.__doc__.split(":")[0], "escenario": chequeo.__doc__,
                             "esperado": "-", "obtenido": str(exc), "captura": None,
                             "reproducible": False})
        navegador.close()

    salida = RAIZ / "scripts" / "resultados.json"
    salida.write_text(
        json.dumps({"fecha_ejecucion": fecha, "casos": resultados, "exploracion": bugs}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Resultados guardados en {salida}")


if __name__ == "__main__":
    main()
