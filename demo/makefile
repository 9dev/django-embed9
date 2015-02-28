
ENVIRONMENT = development
PROJECT_NAME = demo
VENV_PATH = ./virtualenv/demo

#####

default:
	$(MAKE) run

install:
	$(MAKE) upgrade
	( \
		. $(VENV_PATH)/bin/activate; \
		python manage.py makemigrations; \
		python manage.py migrate; \
		python manage.py loaddata data_common.json; \
	)

#####

run:
	( \
		. $(VENV_PATH)/bin/activate; \
		python manage.py runserver localhost:8000; \
	)

upgrade:
	( \
		. $(VENV_PATH)/bin/activate; \
		pip install -r requirements.txt; \
	)

test:
	( \
		. $(VENV_PATH)/bin/activate; \
		python manage.py test --failfast --noinput; \
	)

coverage:
	( \
		. $(VENV_PATH)/bin/activate; \
		coverage run manage.py test -v 2; \
		coverage report -m --omit=$(VENV_PATH)/*; \
	)

