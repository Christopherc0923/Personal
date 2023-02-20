from django.db import models

# Create your models here.
class Project(models.Model):
    # Django model fields
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to ='media/')
    url = models.URLField(blank = True)
    
    # Functions that displays title on the admin page
    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Publication(models.Model):
    # Django model fields
    title = models.CharField(max_length = 250)
    description = models.TextField()
    image = models.ImageField(upload_to ='media/')
    url = models.URLField(blank = True)
    
    # Functions that displays title on the admin page
    def __str__(self):
        return self.title

class ContactForm(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=255, default='')
    find = models.CharField(max_length=255, default='')
    additional_info = models.TextField(default='')
    file = models.FileField(upload_to='media/', default=None, blank=True, null=True)
    terms = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class ML(models.Model):
    # Django model fields
    title = models.CharField(max_length = 250)
    description = models.TextField()
    tech = models.TextField()
    image = models.ImageField(upload_to ='media/')
    url = models.URLField(blank = True)
    
    # Functions that displays title on the admin page
    def __str__(self):
        return self.title

class Cert(models.Model):
    # Django model fields
    title = models.CharField(max_length = 250)
    date = models.DateField()
    url = models.URLField(blank = True)
    
    # Functions that displays title on the admin page
    def __str__(self):
        return self.title