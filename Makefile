.PHONY: all \
		setup \
		black

venv/bin/activate: ## alias for virtual environment
	python -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

black: venv/bin/activate ## black
	. venv/bin/activate; black .
