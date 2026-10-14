#!/usr/bin/env bash
set -e

echo "--> Running backend test suite with coverage..."
pytest --cov=backend/app --cov-report=term-missing tests/

echo "--> Running frontend test suite..."
cd frontend && npm run test:ci && cd ..

echo "All tests executed successfully!"
