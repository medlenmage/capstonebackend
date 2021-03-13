rm -rf capstoneapi/migrations
rm db.sqlite3
python manage.py makemigrations capstoneapi
python manage.py migrate
python manage.py loaddata user
python manage.py loaddata tokens
python manage.py loaddata benefits
python manage.py loaddata deposit_account
python manage.py loaddata payment_type
python manage.py loaddata employee
python manage.py loaddata student
python manage.py loaddata curriculum
python manage.py loaddata company_contact
python manage.py loaddata grouping
python manage.py loaddata equipment
python manage.py loaddata paystub
# python manage.py loaddata school