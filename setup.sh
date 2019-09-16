#!/bin/sh

pip install -r requirements.txt
python src/dragon/manage.py makemigrations library
python src/dragon/manage.py makemigrations members
python src/dragon/manage.py migrate
