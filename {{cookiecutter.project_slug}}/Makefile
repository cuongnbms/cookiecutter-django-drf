build:
	docker-compose build {{cookiecutter.project_slug}}

install:
	uv sync

fix-lint:
	 black --line-length 120 --exclude="migrations" .

run:
	python3 manage.py runserver 0.0.0.0:8000

collectstatic:
	python3 manage.py collectstatic --noinput

createadmin:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin');" | python3 manage.py shell

remove-all-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete

worker:
	python3 manage.py rundramatiq --processes 2 --threads 10 --queues default
