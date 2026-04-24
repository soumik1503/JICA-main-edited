
python manage.py runserver

python manage.py collectstatic
 
python manage.py makemigrations events
 
python manage.py makemigrations holidays
 
python manage.py migrate

python manage.py collectstatic

Get-Content db\db_backup_01-21-2026.sql | docker exec -i postgres-db psql -U postgres -d postgres

nginx -s reload

nginx -s stop

nginx -c "C:\inetpub\wwwroot\django_cms\nginx.conf"

docker-compose restart nginx
