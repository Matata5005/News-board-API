web gunicorn News_board.wsgi --log-file -
worker: celery -A News_board worker -l info 
beat: celery -A News_board beat --loglevel=info
worker: celery -A News_board worker -l info -B

