# Convierte los documentos Word del repositorio a PDF usando Microsoft Word.
# Uso: powershell -ExecutionPolicy Bypass -File scripts\convertir_a_pdf.ps1
$ErrorActionPreference = "Stop"
$raiz = Split-Path $PSScriptRoot -Parent

$pares = @(
    @{ Docx = "$raiz\entregable\informe_hito3.docx";             Pdf = "$raiz\entregable\informe_hito3.pdf" },
    @{ Docx = "$raiz\docs\casos_caja_negra_plantilla_llena.docx"; Pdf = "$raiz\entregable\casos_prueba_caja_negra.pdf" }
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    foreach ($par in $pares) {
        if (-not (Test-Path $par.Docx)) { Write-Host "Omitido (no existe): $($par.Docx)"; continue }
        $doc = $word.Documents.Open($par.Docx, $false, $true)
        $doc.SaveAs([ref]$par.Pdf, [ref]17)   # 17 = wdFormatPDF
        $doc.Close($false)
        Write-Host "PDF generado: $($par.Pdf)"
    }
}
finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
