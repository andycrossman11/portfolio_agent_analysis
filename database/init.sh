#!/bin/bash

set -e
set -u

IFS=','

for database in $ALL_POSTGRES_DBS; do
  echo "Creating additional database $database"
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -c "CREATE DATABASE $database"
  echo "Database $database created"

  if [[ -f "$MIGRATION_SCRIPT" ]]; then
    echo "Running migrations on $database"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" "$database" -f "$MIGRATION_SCRIPT"
    echo "Migrations applied to $database"
  else
    echo "Migration script not found, skipping migrations for $database"
  fi
done
