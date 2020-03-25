echo "inicializando o banco de dados"
python manage.py flush --no-input

echo "rodando as migraçoes "
python manage.py migrate

echo "criando usuario ('admin@example.com', 'admin42')"
echo "from account.models import User; User.objects.create_superuser('admin@example.com', 'admin42')" | python manage.py shell
exec "$@"

echo "Subindo aplicação"
gunicorn --bind :8000 --workers 3 chbrasilprev.wsgi:application