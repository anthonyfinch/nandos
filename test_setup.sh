#! /bin/sh

set -e

echo $TDDIUM_DB_NAME

#createdb "$TDDIUM_DB_NAME"
createdb template_postgis
createdb "$TDDIUM_DB_NAME"

psql template_postgis -c 'CREATE EXTENSION postgis;'
psql "$TDDIUM_DB_NAME" -c 'CREATE EXTENSION postgis;'
