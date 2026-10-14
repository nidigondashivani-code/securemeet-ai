# SecureMeet AI Windows Environment Setup Script
Write-Host "=== Initializing SecureMeet AI Developer Environment ===" -ForegroundColor Cyan

# Backend setup
Write-Host "Configuring Python virtual environment..." -ForegroundColor Yellow
Set-Location backend
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
Set-Location ..

# Frontend setup
Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
Set-Location frontend
npm install
Set-Location ..

# Pre-commit hooks
Write-Host "Installing pre-commit hooks..." -ForegroundColor Yellow
pre-commit install

Write-Host "=== Environment configured successfully! ===" -ForegroundColor Green
