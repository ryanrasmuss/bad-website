#!/bin/bash

# add-apt-repository universe
# apt-get update
# apt-get install python3-pip

touch /var/log/mysite.log
sqlite3 login.db < schema.sql