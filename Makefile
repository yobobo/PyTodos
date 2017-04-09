help:
		@echo 'Makefile for Tinker                              '
		@echo 'Usage:                                           '
		@echo '   make install          install                                          '
		@echo '   make test             run test cases          '
		@echo '   make clean            clean                   '

install:
	pip install -r requirements.txt

test: install
	pytest
	make clean

clean:
	find . \( -name "*.pyc" -o -name "*.log" -o -name "*.swp" -o -name "*.swo" \) -delete
