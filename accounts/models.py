from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


def validate_email(value):
    if not "@konkuk" in value:
        raise ValidationError("Not a valid email")
    else:
        return value

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password=None):

        if not email:
            raise ValueError('이메일은 필수 입니다.')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):

        if not email:
            raise ValueError('이메일은 필수 입니다.')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            is_active=True,
            is_admin=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    object = UserManager()
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email',
        validators=[validate_email]
    )
    nickname = models.CharField(
        max_length=20,
        null=False,
        verbose_name='nickname'
    )
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.nickname

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


