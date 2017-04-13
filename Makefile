help:
		@echo 'Makefile for Tinker                              '
		@echo 'Usage:                                           '
		@echo '   make install          install                 '
		@echo '   make test             run test cases          '
		@echo '   make upload           upload to pypi          '
		@echo '   make clean            clean                   '

install:
	pip install -r requirements.txt

test: install
	pytest
	make clean

upload:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	find . \( -name "*.pyc" -o -name "*.log" -o -name "*.swp" -o -name "*.swo" \) -delete
