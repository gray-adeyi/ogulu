from django.db import models
import datetime

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    favicon = models.ImageField()
    appleicon = models.ImageField()

class MyInformation(models.Model):
    site = models.OneToOneField(Site, related_name='my_info', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, help_text='Your name')
    lastname = models.CharField(max_length=100, help_text='Your surname')
    display_text = models.TextField(max_length=200, help_text='What text should appear on your site\'s landing page')
    dob = models.DateField('Date of birth')
    age = models.PositiveIntegerField(blank=True)
    bio = models.TextField(help_text='Some information about you')
    background_image = models.ImageField(help_text="The image that appears at the background of your site")
    about_image = models.ImageField(help_text="The image that appears at the about")
    address = models.CharField(max_length=200)


    def get_age(self):
        """
        Returns age based on the `dob` supplied
        """
        age = datetime.timedelta(datetime.date()) - self.dob
        return age

    def save(self, *args, **kwargs):
        self.age = self.get_age()
        super().save(*args, **kwargs)

class Interest(models.Model):
    info = models.ForeignKey(MyInformation, related_name='interests', on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)