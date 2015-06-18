from django.test import TestCase

from edc_base.model.models import BaseUuidModel
from ..classes import InfantIdentifier

from django.db import models

class StudySite(BaseUuidModel):
    
    site_code = models.CharField(max_length=4, unique=True)
    site_name = models.CharField(max_length=35, unique=True)
    
    class Meta:
        app_label = 'edc_identifier'

class TestModelTestCase(TestCase):

    def setUp(self):
        app_name='edc_identifier'
        model_name='subjectidentifier'
        studySite = StudySite(site_code = 19, site_name = "Molepolole")
        self.infantId = InfantIdentifier(app_name=app_name, model_name=model_name, maternal_identifier = '056-19800001-3',
                                             study_site = studySite,birth_order=1, live_infants=1, live_infants_to_register=1)
         
#     def test_get_identifier_prep(self):
#         self.maternal_identifier = '056-19800001-3'
#         print(self.infantId.get_identifier_prep())
    
    def test_get_identifier_post(self):
        print(self.infantId.get_identifier_post(new_identifier='027-19900002-2'))
      
    def test_get_base_suffix(self):
        self.assertEqual(self.infantId._get_base_suffix(),10)
         
    def test_get_suffix(self):
        self.assertEqual(self.infantId._get_suffix(),20)