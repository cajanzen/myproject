#!/usr/bin/env bash

cd ~/myproject
git pull
docker-compose -f docker-compose.test.yml up --build --exit-code-from suta && docker-compose up -d --build
