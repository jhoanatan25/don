echo 'Starting Cars4drivers. 8)'
exec gunicorn cars4drivers.wsgi:application \
    --name cars4drivers \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    "$@" \
    --reload

