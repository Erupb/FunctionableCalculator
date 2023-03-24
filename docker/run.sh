python manage.py migrate
python manage.py collectstatic --noinput
sleep 2
gunicorn simple_votings.wsgi:application --bind 0.0.0.0:8084 \
            --error-logfile /var/log/ms102_yacalc/gunicorn_error.log \
            --access-logfile /var/log/ms102_yacalc/gunicorn_access.log \
            --workers 2
