echo 'Recolectando archivos estáticos'
python manage.py collectstatic --noinput --no-post-process

echo 'Starting cars4drivers. 8)'
exec gunicorn cars4driver.wsgi:application \
    --name cars4driver \
    --bind 0.0.0.0:9000 \
    --workers 3 \
    --log-level=info \
    "$@" \
    --reload

