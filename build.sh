set -o errexit

pip install -r requirements/prod.txt

pyhton manage.py collectstatic --no-input
pyhton manage.py migrate