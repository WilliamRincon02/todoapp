run: #Run the project server
	python manage.py runserver

migrate: #Make the migraions of database
	python manage.py migrate

lint: #Make use of linter pydescodestyle PEP8 and black
	pycodestyle manage.py
	black manage.py