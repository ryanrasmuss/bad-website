#!/bin/bash

docker run -d -p 80:5000 -v $(``pwd``)/files/:/mysite/files/ mysite:latest
docker ps
