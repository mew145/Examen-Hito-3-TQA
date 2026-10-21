# Registro de defectos (bugs) — Hito 3 TQA

**Aplicación:** SauceDemo (Swag Labs) — https://www.saucedemo.com/
**Fecha de detección:** 20/10/2026
**Detectado por:** Yuri Rojas (GitHub: mew145)

> **Regla aplicada:** si la prueba pasa, se registra PASS y **no** se inventa un bug. Solo se documentan defectos **reproducibles** con evidencia.

---

## BUG-001 — El formulario de checkout acepta campos con solo espacios en blanco

| Campo | Detalle |
|---|---|
| **ID y título** | BUG-001 · El formulario de checkout acepta campos con solo espacios en blanco |
| **Severidad / prioridad** | Media / Baja (defecto de validación de datos de entrada) |
| **Módulo** | Compra y navegación (checkout — paso 1: Your Information) |
| **Detectado en** | Verificación exploratoria EX-1 (tras ejecutar TC-005) |

### Descripción del problema

La validación del primer paso del checkout verifica únicamente que los campos no estén **vacíos**, pero no descarta valores que no tienen contenido real (espacios en blanco). Un usuario puede enviar un pedido con nombre, apellido y código postal formados solo por espacios, y el sistema lo acepta y finaliza la compra.

### Precondiciones y datos

- Navegador limpio en https://www.saucedemo.com/
- Sesión iniciada con `standard_user` / `secret_sauce`
- Al menos un producto agregado al carrito (Sauce Labs Backpack)
- Datos de prueba: nombre = `"   "` (3 espacios), apellido = `"   "` (3 espacios), código postal = `"   "` (3 espacios)

### Pasos para reproducirlo

1. Abrir https://www.saucedemo.com/ e iniciar sesión con `standard_user` / `secret_sauce`
2. Agregar "Sauce Labs Backpack" al carrito
3. Ingresar al carrito y presionar **Checkout**
4. Completar First Name, Last Name y Postal Code con **solo espacios en blanco**
5. Presionar **Continue**

### Resultado esperado

El formulario debería rechazar los datos sin contenido real y mostrar el mensaje de validación (por ejemplo, `Error: First Name is required`), permaneciendo en el paso 1 del checkout.

### Resultado actual

El formulario **acepta** los campos con solo espacios y avanza al resumen de la compra (*Your cart / Overview*). El pedido puede finalizarse con éxito ("Thank you for your order!") usando datos sin contenido real.

### Evidencia

| Tipo | Referencia | Descripción |
|---|---|---|
| Captura | `evidencias/capturas/expl_01_checkout_solo_espacios.png` | Paso 1 del checkout con los tres campos llenos con solo espacios |
| Captura | `evidencias/capturas/expl_01b_resultado_espacios.png` | El sistema avanzó al resumen de la compra aceptando los datos inválidos |

**Reproducibilidad:** ✔️ Confirmada — el comportamiento se repite en cada ejecución del script `scripts/explorar_defectos.py`.

### Recomendación

Normalizar (trim) los valores ingresados y validar que contengan al menos un carácter no vacío antes de permitir el avance, aplicando la misma regla de validación que ya existe para los campos vacíos.

---

## Verificaciones sin defecto

Estas verificaciones **no** generan reporte de defecto porque el comportamiento observado es el correcto:

| ID | Verificación | Resultado observado | Conclusión |
|---|---|---|---|
| EX-2 | Tras cerrar sesión, usar el botón "Atrás" del navegador | La sesión caduca y se redirige al login | ✅ Comportamiento correcto |
| EX-3 | Ordenar el catálogo de Z a A y agregar un producto | El ordenamiento se conserva (primero: *Test.allTheThings() T-Shirt (Red)*) | ✅ Comportamiento correcto |

## Casos de prueba sin defecto

Los casos **TC-001 a TC-005** resultaron **PASS** (el comportamiento coincidió con lo esperado); conforme a la regla de la plantilla, un caso PASS no genera reporte de defecto.
