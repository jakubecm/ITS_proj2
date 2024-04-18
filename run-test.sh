#!/bin/sh
cd $(dirname $0)
[ -f requirements.txt ] && pip3 install -r requirements.txt
docker-compose up -d || exit 1
sleep 30
behave
docker-compose down -v
