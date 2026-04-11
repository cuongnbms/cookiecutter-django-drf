from django.db import migrations


def create_superuser(apps, schema_editor):
    # Replace with your desired credentials
    username = "admin"
    email = "admin@example.com"
    password = "admin"

    User = apps.get_model('users', 'User')
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)


def rollback_create_superuser(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, rollback_create_superuser),
    ]
