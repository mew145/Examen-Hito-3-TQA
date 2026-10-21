# Casos de prueba de caja negra — Hito 3 TQA

**Aplicación bajo prueba:** SauceDemo (Swag Labs) — https://www.saucedemo.com/
**Cuenta de demostración:** `standard_user` / `secret_sauce`
**Ambiente:** QA (sitio público de demostración) · Navegador Chromium 1440×900
**Ejecutado por:** Yuri Jesús (GitHub: mew145)
**Fecha de ejecución:** 20/10/2026 21:26
**Automatización de la ejecución:** `scripts/ejecutar_pruebas.py` (Playwright) · resultados en `scripts/resultados.json`

> Cada caso sigue las dos partes de la plantilla unificada de la materia: **Parte 1 – Diseño** y **Parte 2 – Ejecución**. El resultado esperado se definió **antes** de ejecutar; el resultado observado se registró **durante** la ejecución real.

## Resumen de resultados

| ID | Título | Tipo | Prioridad | Resultado |
|---|---|---|---|---|
| TC-001 | Inicio de sesión con credenciales válidas | Funcional / Positiva | Alta | ✅ **PASS** |
| TC-002 | Inicio de sesión con credenciales inválidas | Negativa | Alta | ✅ **PASS** |
| TC-003 | Agregar un producto al carrito | Funcional / Positiva | Alta | ✅ **PASS** |
| TC-004 | Eliminar un producto desde el carrito | Funcional / Positiva | Media | ✅ **PASS** |
| TC-005 | Completar el proceso de checkout | Funcional / Positiva | Alta | ✅ **PASS** |

**5 de 5 PASS.** Ningún caso generó defecto; las verificaciones exploratorias adicionales sí detectaron un defecto reproducible → [BUG-001](../bugs/bugs_encontrados.md).

---

## TC-001 · Inicio de sesión con credenciales válidas

### PARTE 1 · Diseño del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-001 |
| **Título** | Inicio de sesión con credenciales válidas |
| **Prioridad** | Alta |
| **Tipo** | Funcional / Positiva |
| **Módulo** | Inicio de sesión |
| **Ambiente** | QA — https://www.saucedemo.com/ |
| **¿Qué se quiere validar?** | Que un usuario con credenciales correctas acceda al catálogo de productos |
| **Estado inicial** | Navegador limpio en la URL de la aplicación |
| **Usuario / permisos** | Usuario demo `standard_user` (sin permisos especiales) |
| **Configuración** | Resolución 1440×900, navegador Chromium |

**Datos de prueba**

| Dato | Valor utilizado | Observación |
|---|---|---|
| Usuario | `standard_user` | Usuario de demostración indicado en la propia página |
| Contraseña | `secret_sauce` | Contraseña oficial del usuario demo |

**Pasos**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Abrir https://www.saucedemo.com/ | – | Se muestra la página de login (Username / Password / Login) |
| 2 | Ingresar el usuario | `standard_user` | El campo Username muestra el valor ingresado |
| 3 | Ingresar la contraseña | `secret_sauce` | El campo Password enmascara el valor |
| 4 | Presionar el botón Login | – | Redirige al catálogo (`inventory.html`) |

**Criterio de éxito:** el usuario accede al catálogo "Products" y no permanece en el login.

### PARTE 2 · Ejecución del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-001 |
| **Ejecutado por** | Yuri Jesús (GitHub: mew145) |
| **Fecha / hora** | 20/10/2026 21:26:15 |
| **Ambiente / versión** | QA — saucedemo.com (build en línea) |
| **Resultado** | ✅ **PASS** |
| **¿Qué ocurrió realmente?** | Se redirigió a la página de inventario (`inventory.html`) y se mostró el catálogo "Products" con los 6 productos; el ícono del carrito aparece vacío al iniciar. |
| **Comparación** | Coincide con lo esperado. |

| # | Paso ejecutado | Estado | Resultado observado |
|---|---|---|---|
| 1 | Ingresar `standard_user` / `secret_sauce` | PASS | Campos completados correctamente |
| 2 | Presionar Login | PASS | Redirección a `inventory.html` |

**Evidencia:** `evidencias/capturas/evid_tc001_01_login_exitoso.png`, `evid_tc001_02_catalogo.png`
**Si resulta FAIL:** N/A

---

## TC-002 · Inicio de sesión con credenciales inválidas (prueba negativa)

### PARTE 1 · Diseño del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-002 |
| **Título** | Inicio de sesión con credenciales inválidas |
| **Prioridad** | Alta |
| **Tipo** | Negativa |
| **Módulo** | Inicio de sesión |
| **Ambiente** | QA — https://www.saucedemo.com/ |
| **¿Qué se quiere validar?** | Que el sistema rechace el acceso con una contraseña incorrecta y muestre un mensaje de error claro |
| **Estado inicial** | Navegador limpio en la URL de la aplicación |
| **Usuario / permisos** | Usuario demo `standard_user` |
| **Configuración** | Resolución 1440×900, navegador Chromium |

**Datos de prueba**

| Dato | Valor utilizado | Observación |
|---|---|---|
| Usuario | `standard_user` | Usuario válido |
| Contraseña | `wrong_password` | Dato inválido a propósito |

**Pasos**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Abrir https://www.saucedemo.com/ | – | Se muestra la página de login |
| 2 | Ingresar el usuario | `standard_user` | El campo muestra el valor |
| 3 | Ingresar una contraseña incorrecta | `wrong_password` | El campo enmascara el valor |
| 4 | Presionar Login | – | No debe ocurrir el acceso al catálogo |

**Criterio de éxito:** permanece en el login y se muestra "Epic sadface: Username and password do not match each other".

### PARTE 2 · Ejecución del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-002 |
| **Ejecutado por** | Yuri Jesús (GitHub: mew145) |
| **Fecha / hora** | 20/10/2026 21:26:19 |
| **Ambiente / versión** | QA — saucedemo.com (build en línea) |
| **Resultado** | ✅ **PASS** |
| **¿Qué ocurrió realmente?** | Se mostró el error "Epic sadface: Username and password do not match each other", el usuario NO accedió al catálogo y los campos de usuario y contraseña recibieron el ícono (X) rojo. |
| **Comparación** | Coincide con lo esperado. |

| # | Paso ejecutado | Estado | Resultado observado |
|---|---|---|---|
| 1 | Ingresar usuario válido y contraseña incorrecta | PASS | Login rechazado |
| 2 | Verificar mensaje de error | PASS | "Epic sadface: Username and password do not match each other" |

**Evidencia:** `evidencias/capturas/evid_tc002_01_error_login.png`, `evid_tc002_02_persiste_login.png`
**Si resulta FAIL:** N/A

---

## TC-003 · Agregar un producto al carrito

### PARTE 1 · Diseño del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-003 |
| **Título** | Agregar un producto al carrito |
| **Prioridad** | Alta |
| **Tipo** | Funcional / Positiva |
| **Módulo** | Catálogo y carrito |
| **Ambiente** | QA — https://www.saucedemo.com/ |
| **¿Qué se quiere validar?** | Que al agregar un producto el contador del carrito se actualice y el ítem aparezca en el carrito |
| **Estado inicial** | Sesión iniciada con `standard_user` y catálogo visible |
| **Usuario / permisos** | Usuario demo `standard_user` |
| **Configuración** | Resolución 1440×900, navegador Chromium |

**Datos de prueba**

| Dato | Valor utilizado | Observación |
|---|---|---|
| Producto | Sauce Labs Backpack | Primer producto del catálogo |
| Acción | Add to cart | Botón del producto |

**Pasos**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Iniciar sesión | `standard_user` / `secret_sauce` | Acceso al catálogo |
| 2 | Presionar "Add to cart" en Sauce Labs Backpack | – | El botón cambia a "Remove" |
| 3 | Verificar el contador del carrito | – | El badge muestra "1" |
| 4 | Ingresar al carrito | – | El producto aparece en la lista |

**Criterio de éxito:** badge = 1, botón en "Remove" y el ítem presente en el carrito.

### PARTE 2 · Ejecución del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-003 |
| **Ejecutado por** | Yuri Jesús (GitHub: mew145) |
| **Fecha / hora** | 20/10/2026 21:26:21 |
| **Ambiente / versión** | QA — saucedemo.com (build en línea) |
| **Resultado** | ✅ **PASS** |
| **¿Qué ocurrió realmente?** | El badge del carrito mostró "1", el botón del producto cambió a "Remove" y "Sauce Labs Backpack" apareció en la página del carrito. |
| **Comparación** | Coincide con lo esperado. |

| # | Paso ejecutado | Estado | Resultado observado |
|---|---|---|---|
| 1 | Add to cart en Sauce Labs Backpack | PASS | Botón → "Remove" |
| 2 | Verificar badge del carrito | PASS | Badge = "1" |
| 3 | Ingresar al carrito | PASS | Producto en la lista |

**Evidencia:** `evidencias/capturas/evid_tc003_01_producto_agregado.png`, `evid_tc003_02_carrito.png`
**Si resulta FAIL:** N/A

---

## TC-004 · Eliminar un producto desde el carrito

### PARTE 1 · Diseño del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-004 |
| **Título** | Eliminar un producto desde el carrito |
| **Prioridad** | Media |
| **Tipo** | Funcional / Positiva |
| **Módulo** | Catálogo y carrito |
| **Ambiente** | QA — https://www.saucedemo.com/ |
| **¿Qué se quiere validar?** | Que al eliminar un producto el carrito se actualice y el contador desaparezca al quedar vacío |
| **Estado inicial** | Sesión iniciada con un producto agregado al carrito |
| **Usuario / permisos** | Usuario demo `standard_user` |
| **Configuración** | Resolución 1440×900, navegador Chromium |

**Datos de prueba**

| Dato | Valor utilizado | Observación |
|---|---|---|
| Producto | Sauce Labs Bike Light | Agregado previamente al carrito |
| Acción | Remove | Botón de eliminar dentro del carrito |

**Pasos**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Iniciar sesión y agregar Sauce Labs Bike Light | – | Badge = "1" |
| 2 | Ingresar al carrito | – | El producto aparece en la lista |
| 3 | Presionar "Remove" sobre el producto | – | El ítem deja de aparecer |
| 4 | Verificar el contador | – | El badge desaparece (carrito vacío) |

**Criterio de éxito:** el ítem se elimina, la lista queda vacía y el badge desaparece.

### PARTE 2 · Ejecución del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-004 |
| **Ejecutado por** | Yuri Jesús (GitHub: mew145) |
| **Fecha / hora** | 20/10/2026 21:26:23 |
| **Ambiente / versión** | QA — saucedemo.com (build en línea) |
| **Resultado** | ✅ **PASS** |
| **¿Qué ocurrió realmente?** | Antes de eliminar el badge mostraba "1"; al presionar "Remove" el producto desapareció de la lista, el carrito quedó vacío y el badge del contador desapareció. |
| **Comparación** | Coincide con lo esperado. |

| # | Paso ejecutado | Estado | Resultado observado |
|---|---|---|---|
| 1 | Agregar Sauce Labs Bike Light | PASS | Badge = "1" |
| 2 | Ingresar al carrito | PASS | Producto presente |
| 3 | Presionar Remove | PASS | Ítem eliminado, badge oculto |

**Evidencia:** `evidencias/capturas/evid_tc004_01_carrito_con_item.png`, `evid_tc004_02_item_eliminado.png`
**Si resulta FAIL:** N/A

---

## TC-005 · Completar el proceso de checkout (compra exitosa)

### PARTE 1 · Diseño del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-005 |
| **Título** | Completar el proceso de checkout |
| **Prioridad** | Alta |
| **Tipo** | Funcional / Positiva |
| **Módulo** | Compra y navegación |
| **Ambiente** | QA — https://www.saucedemo.com/ |
| **¿Qué se quiere validar?** | Que un usuario pueda completar el formulario de compra y finalizar el pedido correctamente |
| **Estado inicial** | Sesión iniciada y al menos un producto en el carrito |
| **Usuario / permisos** | Usuario demo `standard_user` |
| **Configuración** | Resolución 1440×900, navegador Chromium |

**Datos de prueba**

| Dato | Valor utilizado | Observación |
|---|---|---|
| Nombre | Ana | Dato válido |
| Apellido | Quispe | Dato válido |
| Código postal | 0000 | Dato válido |

**Pasos**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Agregar un producto e ingresar al carrito | – | El producto está en la lista |
| 2 | Presionar "Checkout" | – | Se muestra "Your Information" |
| 3 | Completar nombre, apellido y código postal | Ana / Quispe / 0000 | Los campos muestran los datos |
| 4 | Presionar "Continue" | – | Se muestra el resumen (Overview) |
| 5 | Presionar "Finish" | – | Se muestra la confirmación |

**Criterio de éxito:** se muestra el mensaje "Thank you for your order!".

### PARTE 2 · Ejecución del caso de prueba

| Campo | Detalle |
|---|---|
| **ID del TC** | TC-005 |
| **Ejecutado por** | Yuri Jesús (GitHub: mew145) |
| **Fecha / hora** | 20/10/2026 21:26:25 |
| **Ambiente / versión** | QA — saucedemo.com (build en línea) |
| **Resultado** | ✅ **PASS** |
| **¿Qué ocurrió realmente?** | Se completó el formulario, se mostró el resumen de la compra y al finalizar apareció "Thank you for your order!" con "Your order has been dispatched..." y el botón "Back Home" para volver al catálogo. |
| **Comparación** | Coincide con lo esperado. |

| # | Paso ejecutado | Estado | Resultado observado |
|---|---|---|---|
| 1 | Checkout con producto en el carrito | PASS | Formulario "Your Information" |
| 2 | Completar datos | PASS | Campos completados |
| 3 | Continue | PASS | Página de resumen "Overview" |
| 4 | Finish | PASS | "Thank you for your order!" |

**Evidencia:** `evidencias/capturas/evid_tc005_01_formulario_checkout.png`, `evid_tc005_02_resumen.png`, `evid_tc005_03_compra_finalizada.png`
**Si resulta FAIL:** N/A

---

## Verificaciones exploratorias adicionales

Además de los 5 casos, se ejecutaron verificaciones exploratorias para intentar encontrar defectos reproducibles (`scripts/explorar_defectos.py`):

| ID | Verificación | Resultado |
|---|---|---|
| EX-1 | Checkout con campos que contienen solo espacios en blanco | ⚠️ **Defecto reproducible** → [BUG-001](../bugs/bugs_encontrados.md) |
| EX-2 | Tras cerrar sesión, usar el botón "Atrás" del navegador | ✅ Correcto: la sesión caduca y se redirige al login (sin defecto) |
| EX-3 | Ordenar catálogo de Z a A y agregar un producto | ✅ Correcto: el ordenamiento se conserva (sin defecto) |

> **Regla de uso aplicada:** si la prueba pasa se registra PASS y **no** se inventa un bug. Los defectos se documentan únicamente cuando son reproducibles y están respaldados con evidencia.
