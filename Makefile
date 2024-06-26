
FILE ?= manage.py

run: #Run the project server
	python manage.py runserver

migrate: #Make the migraions of database
	python manage.py migrate

lint: #Format the code and PEP8
	black $(FILE)	
	pycodestyle $(FILE)

test: #Run the tests
	python manage.py test --settings=todoapp.settings.ci
