#!/usr/bin/env bash
set -e

echo "--> Running Black..."
black --check backend/

echo "--> Running isort..."
isort --check-only backend/

echo "--> Running flake8..."
flake8 backend/

echo "--> Running mypy..."
mypy backend/app

echo "--> Running frontend type-check & lint..."
cd frontend && npm run type-check && cd ..

echo "All linting and type checks passed successfully!"
