from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        if not self.pk:
            if self.email:
                try:
                    MyUser.objects.get(email=self.email)
                    raise ValidationError({'email': f'{self.email} почта уже существует' })
                except MyUser.DoesNotExist:
                    pass
        else:
            if self.email:
                mu = MyUser.objects.filter(email=self.email).exclude(id=self.pk)
                if mu.count() > 0:
                    raise ValidationError({'email': f'{self.email} почта уже существует' })


    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
