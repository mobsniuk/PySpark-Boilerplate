
help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build"
	@echo "clean-env - remove python environment"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style"
	@echo "test - run tests quickly with the default Python"
	@echo "build - package"

all: default

default: clean deps dev_deps test lint build

.venv:
	if [ ! -e "venv/bin/activate_this.py" ] ; then python3 -m venv --copies venv ; fi

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr dist/

clean-env:
	rm -fr venv

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f nosetests.xml

deps: .venv
	. venv/bin/activate && pip install -U -r requirements.txt

dev_deps: .venv
	. venv/bin/activate && pip install -U -r dev_requirements.txt

lint:
	. venv/bin/activate && pylint -r n src/main.py src/shared src/jobs tests
	. venv/bin/activate &&  flake8 src/jobs/ --ignore=E501
	. venv/bin/activate &&  flake8 src/main.py --ignore=E501
	. venv/bin/activate &&  flake8 src/shared --ignore=E501
	. venv/bin/activate &&  flake8 tests --ignore=E501

test:
	. venv/bin/activate && nosetests ./tests/* --config=.noserc

build: clean
	mkdir ./dist
	cp ./src/main.py ./dist
	cd ./src && zip -x main.py -x \*libs\* -r ../dist/jobs.zip .
	cd venv && tar -hczf ../dist/venv.tar.gz *
