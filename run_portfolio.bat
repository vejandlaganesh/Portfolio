@echo off
title Ganesh Sharma Portfolio
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
pause
