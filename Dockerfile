# mysite
# ======
#
# Dockerfile for my website
#
# Requires ~ 512 mb disk
#
# Build via
# docker build -t mysite .
#
# Run via
# docker run -d -p 80:5000 -v $(``pwd``)/files/:/mysite/files/ mysite:latest
# docker run -ti -p 80:5000 -v $(``pwd``)/:/mysite/ -v $(``pwd``)/files/:/mysite/files/ mysite:latest
#

# Base image debian
FROM debian:latest

# Label base
LABEL mysite latest

RUN apt-get update && apt-get install -y \
    sqlite3 \
    python3 \
    python3-pip \
    python-dev \
    uwsgi-core \
    uwsgi-plugin-python3 && \
    pip3 install flask bcrypt flask-login && \
    apt-get autoremove --purge -y && \
    apt-get clean

EXPOSE 5000

WORKDIR /mysite

COPY . .

RUN ./install.sh

RUN chmod 744 runme.sh

CMD [ "./runme.sh" ]
