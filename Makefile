
FILE ?= manage.py

run: #Run the project server
	python manage.py runserver

migrate: #Make the migraions of database
	python manage.py migrate

lint:
	black $(FILE)	
	pycodestyle $(FILE)
