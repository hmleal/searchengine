help:
	@echo 'Makefile for python-search-engine                                     '
	@echo '                                                                      '
	@echo 'Usage:                                                                '
	@echo '   test                                Run project tests              '
	@echo '   setup                               Install all dependencies to dev'

setup:
	@pip install -r requirements_dev.txt

test:
	@py.test tests --cov-report term-missing --cov-report xml --cov=searchengine --pep8 --flakes

.PHONY: help, setup, test
