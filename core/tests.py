from django.test import TestCase
from django.urls import reverse
from . import models
import datetime

# Create your tests here.
class TestViews(TestCase):
    def test_index_page_works(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)



class TestMiddlewares(TestCase):
    def test_sitedata_middleware_works(self):
        site_data = models.Site.objects.create(name="ogulu's website")
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['site'], site_data)


class TestModels(TestCase):
    def test_site_model_can_only_have_one_instance(self):
        site1 = models.Site.objects.create(name="Website1")
        site2 = models.Site.objects.create(name="Website2")
        self.assertEqual(models.Site.objects.all().count(),1)

    def test_myinformation_model_get_age_logic_works(self):
        site1 = models.Site.objects.create(name="Website1")
        dob = datetime.date(year=1999, month=4, day=29)
        info = models.MyInformation.objects.create(site=site1,dob=dob)
        expected_age = (datetime.date.today() - dob).days / 365
        self.assertEqual(expected_age, info.age)


