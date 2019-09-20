bootstrap:
	source venv/bin/activate; pip install -r requirements.txt
	python manage.py migrate

run:
	export DJANGO_SETTINGS_MODULE=MongoPythonBackend.settings.py
	python manage.py runserver

generate_migrations:
	python manage.py makemigrations RestApi	
	
apply_migrations: generate_migrations
	python manage.py migrate

shell:
	python manage.py shell