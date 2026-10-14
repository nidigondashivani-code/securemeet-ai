#!/usr/bin/env bash
set -e

echo "Running entrypoint checks for SecureMeet AI..."

# Wait for postgres if POSTGRES_SERVER is provided
if [ -n "$POSTGRES_SERVER" ]; then
  echo "Checking database connectivity to $POSTGRES_SERVER:$POSTGRES_PORT..."
  while ! nc -z "$POSTGRES_SERVER" "${POSTGRES_PORT:-5432}"; do
    sleep 0.5
  done
  echo "Database is reachable."
fi

# Apply migrations if requested or in API mode
if [ "$RUN_MIGRATIONS" = "true" ]; then
  echo "Applying Alembic database migrations..."
  alembic upgrade head
fi

exec "$@"
