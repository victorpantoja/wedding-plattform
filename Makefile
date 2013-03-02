
all: clean

clean:
	find . -name '*.pyc' | xargs rm -f
	rm -rf build

start:
	PYTHONPATH=`pwd`:`pwd`/wedding_plattform python wedding_plattform/server.py ${PORT}

test: clean
	echo "Running tests..."
	PYTHONPATH=`pwd` \
		nosetests -s --verbose --with-coverage --cover-package=wedding_plattform tests/*
