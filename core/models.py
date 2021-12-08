from django.db import models
import uuid
import datetime
import logging
from pypaystack import Transaction as PSTransaction
from django.conf import settings

logger = logging.getLogger(__name__)

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    favicon = models.ImageField()
    appleicon = models.ImageField()

    def __str__(self) -> str:
        return self.name

    def has_one_or_more_instance(self): # TODO: create a mixin that allows a model to have only one instance 
        return Site.objects.all().count() > 1

    def save(self, *args, **kwargs):
        if self.has_one_or_more_instance():
            logger.info('`Site` already has an instance.')
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
    age = models.PositiveIntegerField(blank=True, help_text="leave empty. it is automatically generated")
    bio = models.TextField(help_text='Some information about you')
    occupation = models.CharField(max_length=50, help_text="what you do for a living")
    quote = models.TextField(help_text='your favourite quote')
    background_image = models.ImageField(help_text="The image that appears at the background of your site", blank=True)
    about_image = models.ImageField(help_text="The image that appears at the about", blank=True)
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
    
    def has_one_or_more_instance(self): # TODO: create a mixin that allows a model to have only one instance 
        return MyInformation.objects.all().count() > 1

    def save(self, *args, **kwargs):
        if self.has_one_or_more_instance():
            logger.info('`MyInformation` already has an instance.')
            return
        self.age = self.get_age()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

class Interest(models.Model):
    info = models.ForeignKey(MyInformation, related_name='interests', on_delete=models.CASCADE)
    interest = models.CharField(max_length=100, help_text="things that you're attracted to")

    def __str__(self):
        return self.interest

class Service(models.Model):
    info = models.ForeignKey(MyInformation, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="name of the service you're providing")
    description = models.CharField(max_length=100, help_text="brief info of what the service is about")

    def __str__(self):
        return self.name

class Skill(models.Model):
    info = models.ForeignKey(MyInformation, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="the name of the skill")
    proficiency = models.PositiveIntegerField(help_text="how good you are at doing it in percentage(Note: Do not include `%`)")

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    """
    Model stores what clients are saying about `MyInformation` instance
    """
    info = models.ForeignKey(MyInformation, related_name='testimonials', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    testimony = models.TextField()

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    info = models.ForeignKey(MyInformation, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number

class Email(models.Model):
    info = models.ForeignKey(MyInformation, related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email

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

    def __str__(self):
        return self.get_name_display()


class BirthdayWish(models.Model):
    info = models.ForeignKey(MyInformation, related_name='wishes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    relationship = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    info = models.OneToOneField(MyInformation, related_name='resume', on_delete=models.CASCADE)

    def __str__(self):
        return self.info.firstname

class Summary(models.Model):
    """
    Model hold the resume summary
    """
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name='summary')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    resume_summary = models.TextField()
    address = models.TextField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.get_fullname()


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree_acquired = models.CharField(max_length=30)
    duration = models.CharField(max_length=15, help_text="e.g 2019-2021")
    institution = models.CharField(max_length=30)
    brief_info = models.TextField(help_text="A brief summary of what the education acquired entailed")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.degree_acquired

class ProfessionalExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=30)
    duration = models.CharField(max_length=15, help_text="e.g 2019-2021")
    location = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.job_title

class Highlight(models.Model):
    """
    Stores highlights of personal experiences
    """
    experience = models.ForeignKey(ProfessionalExperience, on_delete=models.CASCADE, related_name='highlights')
    highlight = models.CharField(max_length=200)

    def __str__(self):
        return self.highlight


class Message(models.Model):
    """
    Stores messages sent to `MyInformation` instance
    """
    info = models.ForeignKey(MyInformation, related_name='messages', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PictureCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "picture categories"

    def __str__(self):
        return self.name

class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "project categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    OPTIONS = (
        ('completed','Completed'),
        ('in_progress','In Progress')
    )
    info = models.ForeignKey(MyInformation, related_name='projects', on_delete=models.CASCADE)
    categories = models.ManyToManyField(ProjectCategory)
    name = models.CharField(max_length = 100)
    client = models.CharField(max_length=50)
    client_logo = models.ImageField(blank=True)
    date = models.DateField()
    status = models.CharField(max_length=15, choices=OPTIONS, default=OPTIONS[1][0])
    url = models.URLField(blank=True)
    description =models.TextField()

    def __str__(self):
        return self.name
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.project.name


class MyImage(models.Model):
    info = models.ForeignKey(MyInformation, related_name='pictures', on_delete=models.CASCADE)
    categories = models.ManyToManyField(PictureCategory)
    image = models.ImageField()
    caption = models.CharField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on',]

    def __str__(self):
        return self.image.name



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +   Models For payments
# +
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Transaction(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    def verify_payment(self):
        transaction = PSTransaction(authorization_key=settings.PAYSTACK_SECRET_KEY)
        status_code, status, message, data = transaction.verify(self.transaction_id)
        logger.info(f"{status_code} {status} {message} {data}")
        if status_code == 200:
            logger.info(message)
            self.is_verified = True
            self.save()