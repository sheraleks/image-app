help: ## show this help
	@echo 'usage: make [target] ...'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

venv:  ## create python env
	virtualenv -p ~/.pyenv/versions/3.9.6/bin/python venv

install:  ## install requirements
	venv/bin/pip install -r requirements.txt

test: ## run tests with pytest
	venv/bin/pytest --cov=image_app tests

run: ## run in local
	venv/bin/python -m main