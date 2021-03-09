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

default: clean dev_deps deps test lint build

.venv:
	if [ ! -e "pyspark_env/bin/activate_this.py" ] ; then python3 -m venv --copies pyspark_env ; fi

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr dist/

clean-env:
	rm -fr pyspark_env

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f nosetests.xml

deps: .venv
	. pyspark_env/bin/activate && pip install -U -r requirements.txt

dev_deps: .venv
	. pyspark_env/bin/activate && pip install -U -r dev_requirements.txt

lint:
	. pyspark_env/bin/activate && pylint -r n src/main.py src/shared src/jobs tests
	. pyspark_env/bin/activate && flake8 src/jobs/ --ignore=E501
	. pyspark_env/bin/activate && flake8 src/main.py --ignore=E501
	. pyspark_env/bin/activate && flake8 src/shared --ignore=E501
	. pyspark_env/bin/activate && flake8 tests --ignore=E501

test:
	. pyspark_env/bin/activate && nosetests ./tests/* --config=.noserc

build: clean
	mkdir ./dist
	cp ./src/main.py ./dist
	cp run_pyspark.sh ./dist
	cp conf/config.ini ./dist
	cd ./src && zip -x main.py -r ../dist/jobs.zip .
	cd pyspark_env && tar -hzcf ../dist/pyspark_env.tar.gz *