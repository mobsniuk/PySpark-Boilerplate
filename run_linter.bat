@echo off
pylint -r n src/main.py src/shared src/jobs tests
flake8 src/jobs/ --ignore=E501
flake8 src/main.py --ignore=E501
flake8 src/shared --ignore=E501
flake8 tests --ignore=E501

