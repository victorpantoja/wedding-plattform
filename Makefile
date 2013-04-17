
all: clean

clean:
	find . -name '*.pyc' | xargs rm -f
	rm -rf build

deploy:
	fab -i ~/Downloads/victorpantoja.pem prod deploy

setup:
	@echo "Installing dependencies..."
	@pip install -r requirements-dev.txt

start:
	PYTHONPATH=`pwd`:`pwd`/wedding_plattform python wedding_plattform/server.py ${PORT}

test: clean
	echo "Running tests..."
	PYTHONPATH=`pwd` \
		nosetests -s --verbose --with-coverage --cover-package=wedding_plattform tests/*
