python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin42')" | python manage.py shell
exec "$@"