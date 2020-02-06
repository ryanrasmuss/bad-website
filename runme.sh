#!/bin/bash
uwsgi --http-socket 0.0.0.0:5000 --plugin /usr/lib/uwsgi/plugins/python3_plugin.so --wsgi-file wsgi.py --callable app --master --processes 4 --threads 2 --stats 0.0.0.0:9191