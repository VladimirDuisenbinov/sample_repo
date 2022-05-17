#!/bin/sh

if [ "$WAIT_DJANGO" = "true" ]
then
    echo "Waiting for django..."

    while ! nc -z $DJANGO_HOST $DJANGO_PORT; do
      sleep 0.5
    done

    echo "Django started"
fi

exec "$@"