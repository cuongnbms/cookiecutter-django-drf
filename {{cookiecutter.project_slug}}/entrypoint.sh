#!/bin/bash
set -e

if [ "${RUN_MIGRATIONS:-true}" = "true" ]; then
    python3 manage.py migrate --noinput
fi

exec "$@"
