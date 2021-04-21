from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

DEPT_CHOICES = (
    ('it','IT'),
    ('comps', 'COMPS'),
    ('extc','EXTC'),
    ('mech','MECH'),
)

CATEGORY_CHOICES = (
    ('PRODUCT DEVELOPMENT','PRODUCT DEVELOPMENT'),
    ('RESEARCH BASED', 'RESEARCH BASED'),
    ('ENVIRONMENT SUSTAINABILITY','ENVIRONMENT SUSTAINABILITY'),
)

# Create your models here.
class Project(models.Model):
    proj_id = models.AutoField(primary_key=True)
    proj_title = models.CharField(max_length=100)
    proj_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='PRODUCT DEVELOPMENT')
    dept = models.CharField(max_length=6, choices=DEPT_CHOICES, default='it')
    mem1_name = models.CharField(max_length=100)
    mem2_name = models.CharField(max_length=100)
    mem3_name = models.CharField(max_length=100)
    mem1_linkedin = models.CharField(max_length=100)
    mem2_linkedin = models.CharField(max_length=100)
    mem3_linkedin = models.CharField(max_length=100)
    youtube_link = models.CharField(max_length=11)
    proj_description = models.TextField()


class AccountManager(BaseUserManager):
    def create_user(self, full_name, org_name, email, password=None):
        if not email:
            raise ValueError("User must provide an email address")
        if not full_name:
            raise ValueError("User must provide his/her full name")
        if not org_name:
            raise ValueError("User must provide his/her institute/organization name")

        user = self.model(
                email = self.normalize_email(email),
                full_name= full_name)

        user.set_password(password)
        user.save(user = self._db)
        return user

class Account(AbstractBaseUser):
    # user_id = models.AutoField(primary_key=True)
    email =  models.EmailField(verbose_name="email", max_length=60, unique=True)
    full_name = models.CharField(max_length=100, unique=True)
    organisation_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = AccountManager()

    def __str__(self):
        return self.email

