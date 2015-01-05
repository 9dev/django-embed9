
ENVIRONMENT = development
PROJECT_NAME = demo
PYTHON_COMMAND = python2.7
VENV_PATH = ./virtualenv/demo

#####

default:
	$(MAKE) run

install:
	$(MAKE) upgrade
	$(MAKE) syncdb

#####

run:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py runserver localhost:8000; \
	)

upgrade:
	( \
		. $(VENV_PATH)/bin/activate; \
		pip install -r requirements.txt; \
	)

syncdb:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py syncdb --noinput; \
	)

test:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py test main; \
		$(PYTHON_COMMAND) manage.py test embed9; \
	)

reinstall:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py sqlclear main | $(PYTHON_COMMAND) manage.py dbshell; \
		$(PYTHON_COMMAND) manage.py sqlclear embed9 | $(PYTHON_COMMAND) manage.py dbshell; \
	)
	$(MAKE) syncdb

