clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

setup:
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py loaddata onecloud/fixtures/users.json

dev:
	python manage.py runserver

functionaltests:
	lettuce functional_tests/features
