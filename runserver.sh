
python3 manage.py migrate
gunicorn --bind 0.0.0.0:8080 --workers 1 --timeout 120 search.wsgi
