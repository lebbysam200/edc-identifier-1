from django.test import TestCase

from ..exceptions import IdentifierError
from ..models import BaseIdentifierModel
from edc_base.model.models import BaseUuidModel
from ..classes import InfantIdentifier, SubjectIdentifier

from django.db import models

class StudySite(BaseUuidModel):
    
    site_code = models.CharField(max_length=4, unique=True)
    site_name = models.CharField(max_length=35, unique=True)
    
class TestInfantIdentifier(BaseIdentifierModel):
    
    objects = models.Manager()
    
    class Meta:
        app_label = 'edc_identifier'
        ordering = ['-created']

class TestModelTestCase(TestCase):

    def setUp(self):
        app_name='edc_identifier'
        model_name='subjectidentifier'
        is_derived = False
        add_check_digit = False
        self.identifier = SubjectIdentifier(model_name='subjectidentifier', app_name=app_name, identifier_prefix = '066',
                                            is_derived=is_derived, site_code='12', add_check_digit=add_check_digit)
        self.identifier.modulus = 7
        studySite = StudySite(site_code = 19, site_name = "Molepolole")
        self.infantId = InfantIdentifier(app_name=app_name,model_name=model_name,maternal_identifier=self.identifier.get_identifier
                                        (add_check_digit=True),study_site = studySite,birth_order=2, live_infants=3, 
                                        live_infants_to_register=3)
         
    def test_get_identifier_prep(self):
        self.assertEqual(self.infantId.get_identifier_prep(),{'suffix': 56, 'maternal_identifier': '066-12990001-2'})
        
    def test_get_identifier_prep1(self):
        self.infantId.live_infants_to_register=0
        self.assertRaises(IdentifierError, self.infantId._get_identifier_prep)

    def test_get_identifier_prep2(self):
        self.infantId.live_infants=1
        self.assertRaises(IdentifierError, self.infantId._get_identifier_prep)
    
    def test_get_base_suffix(self):
        self.assertEqual(self.infantId._get_base_suffix(),36)
          
    def test_get_suffix(self):
        self.assertEqual(self.infantId._get_suffix(),56)
    
    def test_get_identifier_post(self, **kwargs):
        print(self.infantId.get_identifier_post(new_identifier=self.identifier.get_identifier(add_check_digit=True),**kwargs))