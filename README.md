# Examen Práctico Hito 3 — Testing & Quality Assurance (TQA)

Repositorio individual del **examen práctico Hito 3**: caja negra, caja blanca, Gherkin, registro de defectos y organización del trabajo con Git/GitHub.

| | |
|---|---|
| **Aplicación bajo prueba** | SauceDemo (Swag Labs) — https://www.saucedemo.com/ |
| **Cuenta de demostración** | `standard_user` / `secret_sauce` |
| **Estudiante** | Yuri Jesús (GitHub: [@mew145](https://github.com/mew145)) |
| **Docente** | Mg. Reynel Sánchez — doc.reynel.sanchez.ch@unifranz.edu.bo |
| **Fecha de ejecución** | 20/10/2026 |

## Resumen de resultados

| Actividad | Cantidad | Resultado |
|---|---|---|
| 🧪 Casos de caja negra (SauceDemo) | 5 | **5 PASS / 0 FAIL** |
| 💻 Casos de caja blanca (`validar_compra`) | 3 solicitados + 1 adicional | **4 PASS** — 83,3 % de cobertura de decisiones con los 3 casos; 100 % con el caso adicional |
| 💬 Escenarios Gherkin | 7 (positivos, alternativos y de error) | Redactados |
| 🐞 Defectos reproducibles | 1 | **BUG-001**: el checkout acepta campos con solo espacios en blanco |

## Estructura del repositorio

```
Examen-Hito-3-TQA/
├── README.md                              ← este archivo
├── docs/
│   ├── casos_caja_negra.md                ← los 5 casos (diseño + ejecución) y sus resultados
│   ├── casos_caja_negra_plantilla_llena.docx  ← mismos casos en la plantilla unificada de la materia
│   ├── Plantilla_TC_Unificada_TQA.docx    ← plantilla original de referencia
│   ├── analisis_caja_blanca.md            ← decisiones, condiciones, criterio y cálculo del mínimo
│   ├── casos_caja_blanca_resultados.md    ← ejecución de CB-001 a CB-004
│   └── escenarios_gherkin.md              ← 7 escenarios Given/When/Then
├── bugs/
│   └── bugs_encontrados.md                ← reporte de defectos reproducibles
├── evidencias/
│   └── capturas/                          ← capturas de pantalla de cada caso y verificación
├── entregable/
│   ├── informe_hito3.pdf                  ← informe final consolidado
│   └── casos_prueba_caja_negra.pdf        ← plantilla unificada completada
└── scripts/
    ├── ejecutar_pruebas.py                ← ejecuta los 5 casos con Playwright
    ├── explorar_defectos.py               ← verificaciones exploratorias (EX-1 a EX-3)
    ├── validar_compra.py                  ← ejecuta los casos de caja blanca
    ├── gen_informe.py                     ← genera el informe Word
    ├── gen_plantilla_llena.py             ← rellena la plantilla de casos de prueba
    ├── convertir_a_pdf.ps1                ← convierte los Word a PDF con Microsoft Word
    ├── resultados.json                    ← resultados reales de la ejecución
    └── exploracion.json                   ← resultados de las verificaciones exploratorias
```

## Cómo ejecutar las pruebas

```bash
pip install playwright
python -m playwright install chromium

python scripts/ejecutar_pruebas.py     # 5 casos de caja negra + capturas
python scripts/explorar_defectos.py    # verificaciones exploratorias
python scripts/validar_compra.py       # casos de caja blanca

python scripts/gen_plantilla_llena.py  # regenera la plantilla completada
python scripts/gen_informe.py          # regenera el informe Word
powershell -ExecutionPolicy Bypass -File scripts/convertir_a_pdf.ps1   # Word -> PDF
```

## Resumen de hallazgos

- **Caja negra:** los 5 casos (login válido, login inválido, agregar al carrito, eliminar del carrito y checkout completo) se ejecutaron sobre la aplicación real y todos coincidieron con el resultado esperado.
- **Defecto encontrado (BUG-001):** en el paso 1 del checkout, los campos "First Name", "Last Name" y "Postal Code" aceptan valores formados **solo por espacios en blanco** y permiten finalizar el pedido. Es reproducible y está documentado con capturas en `bugs/bugs_encontrados.md`.
- **Caja blanca:** el código `validar_compra` tiene **3 decisiones y 4 condiciones simples**; con criterio de cobertura de decisiones el mínimo es **4 casos** (uno por cada camino/salida). Los 3 casos solicitados cubren 5 de 6 resultados (83,3 %) y se explica el ajuste necesario (CB-004) para alcanzar el 100 %.
- **Gherkin:** 7 escenarios sobre login, catálogo/carrito y checkout, incluyendo positivos, alternativos y de error.

## Seguimiento del trabajo

Las tareas y los defectos se gestionaron con **Issues** y un **Project Board** (columnas To Do / In Progress / In Review / Done) en la pestaña *Projects* del repositorio.
