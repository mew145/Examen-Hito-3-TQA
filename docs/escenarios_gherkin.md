# Escenarios Gherkin — Hito 3 TQA (actividad adicional)

**Aplicación:** SauceDemo (Swag Labs) — https://www.saucedemo.com/
**Usuario de prueba:** `standard_user` / `secret_sauce`

---

## Feature: Inicio de sesión

Como usuario del sistema,
quiero iniciar sesión con mis credenciales,
para acceder al catálogo de productos.

### Scenario 1: Acceso exitoso con credenciales válidas (positivo)
```gherkin
Given que estoy en la página de inicio de sesión de SauceDemo
When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
And presiono el botón "Login"
Then debería ser redirigido a la página del catálogo "Products"
And debería ver la lista de 6 productos disponibles
And el ícono del carrito debería aparecer vacío
```

### Scenario 2: Acceso con credenciales incorrectas (de error)
```gherkin
Given que estoy en la página de inicio de sesión de SauceDemo
When ingreso el usuario "standard_user" y la contraseña "wrong_password"
And presiono el botón "Login"
Then debería permanecer en la página de inicio de sesión
And debería ver el mensaje "Epic sadface: Username and password do not match each other"
And el campo de contraseña debería marcarse como inválido
```

### Scenario 3: Acceso bloqueado por el usuario bloqueado (alternativo)
```gherkin
Given que estoy en la página de inicio de sesión de SauceDemo
When ingreso el usuario "locked_out_user" y la contraseña "secret_sauce"
And presiono el botón "Login"
Then debería permanecer en la página de inicio de sesión
And debería ver el mensaje "Epic sadface: sorry, this user has been locked out"
```

---

## Feature: Catálogo y carrito de compras

Como usuario del sistema,
quiero agregar y eliminar productos del carrito,
para seleccionar lo que deseo comprar.

### Scenario 4: Agregar un producto al carrito (positivo)
```gherkin
Given que inicié sesión y estoy en el catálogo de productos
When presiono "Add to cart" en el producto "Sauce Labs Backpack"
Then el botón debería cambiar a "Remove"
And el contador del carrito debería mostrar "1"
And al ingresar al carrito debería ver "Sauce Labs Backpack" en la lista
```

### Scenario 5: Eliminar un producto desde el carrito (alternativo)
```gherkin
Given que agregué "Sauce Labs Bike Light" al carrito y estoy en la página del carrito
When presiono "Remove" sobre ese producto
Then el producto dejaría de aparecer en la lista del carrito
And el contador del carrito debería desaparecer porque quedaría vacío
```

---

## Feature: Proceso de compra (checkout)

Como usuario del sistema,
quiero completar el formulario de compra,
para finalizar un pedido correctamente.

### Scenario 6: Compra exitosa con datos válidos (positivo)
```gherkin
Given que inicié sesión y tengo al menos un producto en el carrito
When presiono "Checkout"
And completo el formulario con nombre "Ana", apellido "Quispe" y código postal "0000"
And presiono "Continue" y luego "Finish"
Then debería ver la confirmación "Thank you for your order!"
And debería poder volver al catálogo con "Back Home"
```

### Scenario 7: Checkout sin completar los campos obligatorios (de error)
```gherkin
Given que estoy en el primer paso del formulario de checkout
When dejo el campo "First Name" vacío y presiono "Continue"
Then debería ver el mensaje de error "Error: First Name is required"
And debería permanecer en el formulario de checkout
```

---

> **Nota:** Gherkin describe el comportamiento esperado; por sí solo no automatiza las pruebas. Los escenarios anteriores se contrastaron con la ejecución real documentada en [casos_caja_negra.md](casos_caja_negra.md).
