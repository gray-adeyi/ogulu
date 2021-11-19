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
    OPTIONS = (
        ('olevel','Olevel'),
        ('undergrad','Undegraduate'),
        ('beng','B.Eng'),
        ('bsc','B.Sc'),
        ('meng','Master'),
        ('phd','PHD')
    )
    site = models.OneToOneField(Site, related_name='my_info', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, help_text='Your name')
    lastname = models.CharField(max_length=100, help_text='Your surname')
    nickname = models.CharField(max_length=50)
    display_text = models.TextField(max_length=200, help_text='What text should appear on your site\'s landing page', default="The <span>top</span> feels so much better than the bottom.")
    dob = models.DateField('Date of birth')
    age = models.PositiveIntegerField(blank=True)
    bio = models.TextField(help_text='Some information about you')
    occupation = models.CharField(max_length=50, help_text="what you do for a living")
    quote = models.TextField(help_text='your favourite quote')
    background_image = models.ImageField(help_text="The image that appears at the background of your site")
    about_image = models.ImageField(help_text="The image that appears at the about")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20, help_text="Where you're based at the moment")
    degree = models.CharField(max_length=15, choices=OPTIONS)


    def get_age(self):
        """
        Returns age based on the `dob` supplied
        """
        age = datetime.date.today() - self.dob
        return age.days / 365
    
    def is_birthday(self):
        """
        Returns boolean value of if it's `MyInfomation`
        instance birthday based on the `self.dob`
        """
        today = datetime.date.today()
        return (today.day == self.dob.day) and (today.month == self.dob.month)

    def save(self, *args, **kwargs):
        self.age = self.get_age()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

class Interest(models.Model):
    info = models.ForeignKey(MyInformation, related_name='interests', on_delete=models.CASCADE)
    interest = models.CharField(max_length=100, help_text="things that you're attracted to")

class Service(models.Model):
    info = models.ForeignKey(MyInformation, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="name of the service you're providing")
    description = models.CharField(max_length=100, help_text="brief info of what the service is about")

class Skill(models.Model):
    info = models.ForeignKey(MyInformation, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="the name of the skill")
    proficiency = models.PositiveIntegerField(help_text="how good you are at doing it in percentage(Note: Do not include `%`)")

class Testimonial(models.Model):
    """
    Model stores what clients are saying about `MyInformation` instance
    """
    info = models.ForeignKey(MyInformation, related_name='testimonials', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    testimony = models.TextField()

class PhoneNumber(models.Model):
    info = models.ForeignKey(MyInformation, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)

class Email(models.Model):
    info = models.ForeignKey(MyInformation, related_name='emails', on_delete=models.CASCADE)
    email = models.CharField(max_length=15)

class SocialAccount(models.Model):
    OPTIONS = (
        ('facebook','Facebook'),
        ('instagram','Instagram'),
        ('twitter','Twitter'),
        ('tiktok','Tik Tok'),
        ('telegram','Telegram'),
    )
    info = models.ForeignKey(MyInformation, related_name='social_accounts', on_delete=models.CASCADE)
    name = models.CharField(max_length=15, choices=OPTIONS)
    link = models.URLField()


class BirthdayWish(models.Model):
    info = models.ForeignKey(MyInformation, related_name='wishes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    relationship = models.CharField(max_length=50)
    message = models.TextField()