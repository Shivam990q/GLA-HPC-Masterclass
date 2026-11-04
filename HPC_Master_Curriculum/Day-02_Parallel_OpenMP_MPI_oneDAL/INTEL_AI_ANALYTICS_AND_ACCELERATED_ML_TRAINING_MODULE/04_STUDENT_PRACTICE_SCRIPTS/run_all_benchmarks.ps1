# =============================================================================
# INTEL oneAPI ACCELERATED MACHINE LEARNING - AUTOMATED BENCHMARK RUNNER (POWERSHELL)
# Script: run_all_benchmarks.ps1
# Purpose: Execute all student practice scripts sequentially on Windows PowerShell
# =============================================================================

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $scriptDir

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "   GLA HPC MASTERCLASS - DAY 02 AFTERNOON ML ACCELERATION SUITE       " -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Starting automated benchmark evaluation at: $(Get-Date)"
Write-Host ""

# Detect python
$pythonCmd = $null
if (Get-Command "python" -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command "py" -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} elseif (Get-Command "python3" -ErrorAction SilentlyContinue) {
    $pythonCmd = "python3"
} else {
    Write-Host "[!] ERROR: Python is not found in PATH." -ForegroundColor Red
    exit 1
}

$pyVer = & $pythonCmd --version 2>&1
Write-Host "[*] Using Python: $pyVer" -ForegroundColor Yellow
Write-Host ""

function Run-Benchmark {
    param(
        [string]$ScriptName,
        [string]$Desc
    )
    Write-Host ">>> [RUNNING] $ScriptName`: $Desc" -ForegroundColor Green
    & $pythonCmd $ScriptName
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[!] FAILED: $ScriptName with exit code $LASTEXITCODE" -ForegroundColor Red
        exit $LASTEXITCODE
    }
    Write-Host ">>> [FINISHED] $ScriptName" -ForegroundColor Green
    Write-Host ""
}

# 1. Telemetry Audit
Run-Benchmark "01_verify_intel_env.py" "Hardware & oneAPI Telemetry Audit"

# 2. NumPy MKL DGEMM
Run-Benchmark "02_numpy_mkl_speedup.py" "NumPy MKL BLAS Matrix Multiply Speedup"

# 3. K-Means
Run-Benchmark "03_kmeans_acceleration.py" "Accelerated K-Means Customer Clustering"

# 4. Random Forest
Run-Benchmark "04_random_forest_acceleration.py" "Accelerated Random Forest Ensemble"

# 5. PCA Reduction
Run-Benchmark "05_pca_reduction_acceleration.py" "Accelerated PCA Dimensionality Reduction"

# 6. Full Benchmark Suite
Run-Benchmark "06_full_benchmark_suite.py" "Complete Multi-Algorithm Benchmark Suite"

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "   ALL BENCHMARK SCRIPTS COMPLETED SUCCESSFULLY!                      " -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
$csvPath = Join-Path $scriptDir "intel_ml_acceleration_results.csv"
Write-Host "CSV Report generated at: $csvPath"
