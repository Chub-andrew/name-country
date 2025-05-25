import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "name_country.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_users():
    if not User.objects.filter(email="admin@mail.com").exists():
        User.objects.create_superuser(
            email="admin@mail.com",
            password="123123"
        )
        print("Superuser \"admin\" was created ")
    else:
        print("Superuser \"admin\" is already created")

    if not User.objects.filter(email="user@mail.com").exists():
        User.objects.create_user(
            email="user@mail.com",
            password="123123"
        )
        print("User user was created ")
    else:
        print("User user is already created")

if __name__ == "__main__":
    create_users()
