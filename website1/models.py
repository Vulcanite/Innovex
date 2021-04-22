from django.db import models

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

DESIGNATION_CHOICES = (
    ('STUDENT','STUDENT'),
    ('FACULTY','FACULTY'),
)

# Create your models here.
class Project(models.Model):
    proj_id          = models.AutoField(primary_key=True)
    proj_title       = models.CharField(max_length=100)
    proj_category    = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='PRODUCT DEVELOPMENT')
    dept             = models.CharField(max_length=6, choices=DEPT_CHOICES, default='it')
    mem1_name        = models.CharField(max_length=100)
    mem2_name        = models.CharField(max_length=100)
    mem3_name        = models.CharField(max_length=100)
    mem1_linkedin    = models.CharField(max_length=100)
    mem2_linkedin    = models.CharField(max_length=100)
    mem3_linkedin    = models.CharField(max_length=100)
    youtube_link     = models.CharField(max_length=11)
    proj_description = models.TextField()
    tech_aspects     = models.CharField(max_length=100, default="img.jpg")


class UserModel(models.Model):
    user_id          = models.AutoField(primary_key=True)
    user_name        = models.CharField(max_length=100)
    user_email       = models.CharField(max_length=100, unique=True)
    user_designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES, default='STUDENT')
    user_phone       = models.IntegerField()
    organisation     = models.CharField(max_length=100)


    

