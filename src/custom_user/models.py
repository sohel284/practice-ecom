from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,   **extra_fields):
        """ create and save user """

        if not email:
            raise ValueError("The user must have email")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have been True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )

    STATUS = (
        ('active', 'Active',),
        ('archived', 'Archived'),
        ('deleted', 'Deleted'),
    )

    first_name = models.CharField(max_length=55, )
    last_name = models.CharField(max_length=55, )
    is_active = models.BooleanField(default=True, )
    is_staff = models.BooleanField(default=False, )
    is_superuser = models.BooleanField(default=False, )
    password = models.CharField(max_length=150, null=True, blank=True,)
    confirm_password = models.CharField(max_length=150, null=True, blank=True,)
    email = models.CharField(max_length=255, )
    gender = models.CharField(max_length=20, choices=GENDER, default='male', )
    status = models.CharField(max_length=20, choices=STATUS, default='active', )
    groups = ArrayField(models.CharField(max_length=100), default=list)

    new_password = models.CharField(max_length=30, null=True, blank=True, )
    old_password = models.CharField(max_length=30, null=True, blank=True,)

    USERNAME_FIELDS = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'is_active', 'is_staff',
                       'is_superuser', 'gender', 'status', 'groups', ]

    objects = CustomUserManager()

    last_login = None

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
