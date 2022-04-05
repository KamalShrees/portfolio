from audioop import reverse
from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from logging import PlaceHolder
from platform import platform
from unicodedata import category
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
#regex validation 
string_validate = RegexValidator(r'^(([A-Za-z]+)(\s[A-Za-z]+)?)$', 'only alphabets are allowed')
image_validate = RegexValidator('([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)', 'only jpg, jepg, png, gif, bmp images are allowed')
email_validate = RegexValidator(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')


class Skills(models.Model):
    skill_name = models.CharField(max_length=100, validators=[string_validate], null=True)
    image = models.ImageField(upload_to='skills', validators=[image_validate])
    percentage = models.IntegerField()
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return self.skill_name 
#........................................................................
    
class Testimonials(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    post = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=False)
    image = models.ImageField(upload_to='Testimonials', null=False)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'Testimonials of {self.fullname}')

#........................................................................

class Intrests(models.Model):
    name = models.CharField(max_length=100, null=True)
    icon = models.ImageField(upload_to='Intrests', null=False)
    
    def __str__(self):
        return (f'Name of Intrests {self.name}')
#........................................................................


class Social(models.Model):
    name = models.CharField(max_length=100, null=True)
    icon = models.ImageField(upload_to='Social', null=False)
    link = models.CharField(max_length=100, null=False)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'Name of Social Links {self.name}')
#........................................................................   
    

class Service(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=False)
    icon = models.ImageField(upload_to='Service', null=False)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'Name of Services {self.name}')
    
# ..................................................................
Category = (
       ('Design', 'Design'),
       ('PHP', 'PHP'),
       ('Python', 'Python'),
       ('Wordpress', 'Wordpress'),
)

class Portfolio(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, choices=Category, default='Design')
    client = models.CharField(max_length=100, null=True, default='none')
    description = models.TextField(max_length=1000, null=True, default='none')
    publish_date = models.DateField(null=True, default='2022-01-01')
    link = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='Portfolio', null=True)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'Name of Portfolio {self.name}')
#........................................................................
    
    
class Status(models.Model):
    happy_client_no = models.IntegerField( null=True)
    support_hour = models.IntegerField( null=True)
    award_no = models.IntegerField( null=True)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'Tatal number of status {self.happy_client_no}')
    
    
# ......................................................................

class Education(models.Model):
    institution_name = models.CharField(max_length=100, null=False)
    level = models.CharField(max_length=100, null=False)
    start_year = models.DateField(null=True)
    end_year = models.DateField(null=True)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'Name of Educational Institution {self.institution_name}')
    
    
# ......................................................................


class About(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    description = models.TextField(max_length=1000, null=False)
    image = models.ImageField(upload_to='About', null=False)
    cv_upload = models.FileField(upload_to='About', null=False)
    
    def __str__(self):
        return (f'Details of {self.fullname}')
    
    
#.............................................................. 

Experience = (
       ('Training', 'Training'),
       ('Internship', 'Internship'),
       ('Work', 'Work'),
)

class Experience(models.Model):
    experience_name = models.CharField(max_length=100, choices=Experience, default='Training')
    responsiblity = models.TextField(max_length=500, null=True)
    platform = models.CharField(null=False, max_length=100, default='programming')
    start_year = models.DateField(null=True)
    end_year = models.DateField(null=True)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return (f'Details of Experience {self.experience_name}')

# ..................................

def get_absolute_url(self):
    return reverse('portfolio_details', args=[self.id])


# ...........................

class Contact(models.Model):
    name = models.CharField(max_length=40, null=False, validators=[string_validate])
    email = models.EmailField(null=False, validators=[email_validate])
    subject = models.CharField(max_length=40, null=False, validators=[string_validate])
    message = models.TextField(max_length=2000, null=True)
    
    def __str__(self):
        return (f'Feedback of {self.name}') 
    
