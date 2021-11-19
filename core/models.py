from django.db import models
import datetime

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    favicon = models.ImageField()
    appleicon = models.ImageField()

    def __str__(self) -> str:
        return self.name

    def has_one_or_more_instance(self):
        return Site.objects.all().count() >= 1

    def save(self, *args, **kwargs):
        if self.has_one_or_more_instance():
            return
        super().save(*args, **kwargs)


class MyInformation(models.Model):
    site = models.OneToOneField(Site, related_name='my_info', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, help_text='Your name')
    lastname = models.CharField(max_length=100, help_text='Your surname')
    display_text = models.TextField(max_length=200, help_text='What text should appear on your site\'s landing page', default="The <span>top</span> feels so much better than the bottom.")
    dob = models.DateField('Date of birth')
    age = models.PositiveIntegerField(blank=True)
    bio = models.TextField(help_text='Some information about you')
    background_image = models.ImageField(help_text="The image that appears at the background of your site")
    about_image = models.ImageField(help_text="The image that appears at the about")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20, help_text="Where you're based at the moment")


    def get_age(self):
        """
        Returns age based on the `dob` supplied
        """
        age = datetime.date.today() - self.dob
        return age.days / 365

    def save(self, *args, **kwargs):
        self.age = self.get_age()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

class Interest(models.Model):
    info = models.ForeignKey(MyInformation, related_name='interests', on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)

class PhoneNumber(models.Model):
    info = models.ForeignKey(MyInformation, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)

class Email(models.Model):
    info = models.ForeignKey(MyInformation, related_name='emails', on_delete=models.CASCADE)
    email = models.CharField(max_length=15)