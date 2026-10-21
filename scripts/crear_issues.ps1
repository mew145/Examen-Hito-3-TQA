# Crea los Issues del examen en el repositorio de GitHub.
# Uso: powershell -ExecutionPolicy Bypass -File scripts\crear_issues.ps1
# Requiere: GH_TOKEN definido en el entorno.

$ErrorActionPreference = "Stop"
$repo = "mew145/Examen-Hito-3-TQA"

$issues = @(
    @{ t = "Disenar 5 casos de prueba de caja negra"; l = "tarea"; b = "Disenar 5 casos funcionales distintos sobre SauceDemo usando la plantilla unificada de la materia (Parte 1 diseno / Parte 2 ejecucion).`n`nArchivo: docs/casos_caja_negra.md" },
    @{ t = "Ejecutar los casos de caja negra en SauceDemo"; l = "tarea"; b = "Ejecutar TC-001 a TC-005 sobre https://www.saucedemo.com/ y registrar PASS/FAIL con fecha y hora.`n`nScript: scripts/ejecutar_pruebas.py`nResultados: scripts/resultados.json" },
    @{ t = "Registrar capturas de evidencia"; l = "tarea"; b = "Guardar una captura por cada paso relevante de cada caso.`n`nCarpeta: evidencias/capturas/" },
    @{ t = "Analizar el codigo de caja blanca y determinar la cobertura"; l = "tarea"; b = "Identificar decisiones (3) y condiciones simples (4) de la funcion validar_compra, elegir el criterio (cobertura de decisiones) y calcular el minimo de casos (4).`n`nArchivo: docs/analisis_caja_blanca.md" },
    @{ t = "Ejecutar los casos de caja blanca (CB-001 a CB-004)"; l = "tarea"; b = "Ejecutar los 3 casos solicitados mas el caso adicional propuesto para completar el 100% de cobertura de decisiones.`n`nScript: scripts/validar_compra.py`nResultados: docs/casos_caja_blanca_resultados.md" },
    @{ t = "Redactar escenarios Gherkin (actividad adicional)"; l = "tarea"; b = "Redactar al menos 2 escenarios (uno exitoso y uno alternativo/de error) con Feature, Scenario, Given, When y Then.`n`nArchivo: docs/escenarios_gherkin.md (7 escenarios)" },
    @{ t = "Documentar defectos reproducibles"; l = "tarea"; b = "Registrar solo bugs reproducibles con pasos, resultado esperado/actual, evidencia y severidad.`n`nArchivo: bugs/bugs_encontrados.md" },
    @{ t = "Organizar el repositorio y el README"; l = "tarea"; b = "Crear la estructura sugerida (docs/, bugs/, evidencias/, entregable/) y el README con proposito, URL probada y resumen.`n`nArchivo: README.md" },
    @{ t = "Preparar el informe final en PDF"; l = "tarea"; b = "Consolidar introduccion, casos y resultados, bugs, analisis de caja blanca, Gherkin y conclusiones en un unico PDF.`n`nArchivo: entregable/informe_hito3.pdf" },
    @{ t = "Invitar al docente al repositorio"; l = "tarea"; b = "Agregar al docente como colaborador con permisos de escritura.`n`nEstado: invitation enviada a @Reynel7 (por correo la invitacion no es posible: el correo institucional no esta asociado a una cuenta de GitHub)." },
    @{ t = "BUG-001: el checkout acepta campos con solo espacios en blanco"; l = "bug"; b = "El formulario del paso 1 del checkout valida solo que los campos no esten vacios, pero acepta valores formados solo por espacios en blanco y permite finalizar el pedido.`n`nPasos: iniciar sesion, agregar un producto, Checkout, llenar los 3 campos con espacios, Continue.`nEsperado: 'Error: First Name is required'.`nActual: avanza al resumen de la compra.`nEvidencia: evidencias/capturas/expl_01_checkout_solo_espacios.png y expl_01b_resultado_espacios.png`nReproducible: si.`n`nDetalle: bugs/bugs_encontrados.md" }
)

foreach ($i in $issues) {
    $numero = $null
    foreach ($intento in 1..6) {
        try {
            $salida = gh issue create --repo $repo --title $i.t --body $i.b --label $i.l 2>&1 | Out-String
            if ($salida -match "github.com/.+/issues/(\d+)") { $numero = $Matches[1]; break }
        } catch { }
        Start-Sleep -Seconds 4
    }
    if ($numero) {
        Write-Host "Issue #$numero creado: $($i.t)"
        if ($i.l -eq "bug") {
            gh issue close $numero --repo $repo --comment "Resuelto/informado en el informe final. Ver bugs/bugs_encontrados.md y entregable/informe_hito3.pdf." | Out-Null
        } else {
            gh issue close $numero --repo $repo --comment "Completado. Ver commits y archivos asociados en el repositorio." | Out-Null
        }
    } else {
        Write-Host "NO SE PUDO CREAR: $($i.t) -> $salida"
    }
}
