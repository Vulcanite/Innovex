from django.db import models

DEPT_CHOICES = (
    ('it','IT'),
    ('comps', 'COMPS'),
    ('extc','EXTC'),
    ('mech','MECH'),
)

CATEGORY_CHOICES = (
    ('pro_dev','PRODUCT DEVELOPMENT'),
    ('research', 'RESEARCH BASED'),
    ('env_sust','ENVIRONMENT SUSTAINABILITY'),
)

# Create your models here.
class Project(models.Model):
    proj_id = models.AutoField(primary_key=True)
    proj_title = models.CharField(max_length=100)
    proj_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='pro_dev')
    dept = models.CharField(max_length=6, choices=DEPT_CHOICES, default='it')
    mem1_name = models.CharField(max_length=100)
    mem2_name = models.CharField(max_length=100)
    mem3_name = models.CharField(max_length=100)
    mem1_linkedin = models.CharField(max_length=100)
    mem2_linkedin = models.CharField(max_length=100)
    mem3_linkedin = models.CharField(max_length=100)
    youtube_link = models.CharField(max_length=11)
    proj_description = models.TextField()