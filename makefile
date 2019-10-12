serve:
	source venv/bin/activate && cd MouseHouseLIMS && python manage.py runserver

create_migrations:
	source venv/bin/activate && cd MouseHouseLIMS && python3 manage.py makemigrations

apply_migrations:
	source venv/bin/activate && cd MouseHouseLIMS && python3 manage.py migrate

create_admin:
	source venv/bin/activate && cd MouseHouseLIMS && python manage.py createsuperuser

shell:
	source venv/bin/activate && cd MouseHouseLIMS && python manage.py shell

