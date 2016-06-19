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

setuptests:
	sudo apt-get install xvfb python-dev libnss3 -y
	pip install -r requirements/test.txt

functionaltests:
	lettuce functional_tests/features --xunit-file=functional_test_results.xml --with-xunit

unittests:
	py.test --junitxml=unit_test_results.xml
