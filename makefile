environment:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

migrate:
	venv/bin/python src/dragon/manage.py makemigrations library members
	venv/bin/python src/dragon/manage.py migrate

execute:
	venv/bin/python src/dragon/manage.py runserver localhost:8000
