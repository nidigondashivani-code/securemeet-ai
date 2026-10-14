#!/usr/bin/env bash
set -e

echo "=== Initializing SecureMeet AI Developer Environment ==="

# Backend setup
echo "Configuring Python virtual environment..."
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
cd ..

# Frontend setup
echo "Installing frontend dependencies..."
cd frontend
npm install
cd ..

# Pre-commit setup
echo "Installing pre-commit hooks..."
pre-commit install

echo "=== Environment configured successfully! ==="
