# source activate py3
gunicorn apps.wsgi --preload -b 0.0.0.0:8084 --log-file -