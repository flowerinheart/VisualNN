ps | grep node |  cut -c 1-5 | xargs kill -9
ps | grep celery |  cut -c 1-5 | xargs kill -9

