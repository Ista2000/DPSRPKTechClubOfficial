#!/usr/bin bash
python manage.py makemigrations
python manage.py migrate
echo "from users.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell
