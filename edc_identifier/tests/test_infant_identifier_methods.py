from django.test import TestCase
from django.db import models
from ..classes import InfantIdentifier, SubjectIdentifier

from ..models import BaseIdentifierModel

from ..exceptions import IdentifierError

class StudySite(object):
    def __init__(self,site_code=None,site_name=None):
        self.site_code = site_code
        self.site_name = site_name 
    
    class Meta:
        app_label = 'edc_identifier'

class InfantIdentifierModel(BaseIdentifierModel):

    objects = models.Manager()

    class Meta:
        app_label = 'edc_identifier'
        ordering = ['-created']

class TestModelTestCase(TestCase):
    
    def setUp(self):
        
        study_site = StudySite(site_code='19', site_name='Molepolole')
        
        is_derived = False
        add_check_digit = False
        self.identifier = SubjectIdentifier(model_name = 'subjectidentifier', app_name = 'edc_identifier', identifier_prefix = '066',
                                            is_derived=is_derived, site_code='19', add_check_digit=add_check_digit)
        self.identifier.modulus = 7
        maternalId = self.identifier.get_identifier(add_check_digit=True)
        self.infantId = InfantIdentifier(model_name = 'infantidentifiermodel', app_name = 'edc_identifier',maternal_identifier=maternalId, 
                                         study_site=study_site, birth_order=2, live_infants=3,live_infants_to_register=3,modulus=7)
        
    
    def test_get_identifier_prep(self):
        idPrep = {'suffix': 56, 'maternal_identifier': '066-19990001-2'}
        self.assertEqual(self.infantId.get_identifier_prep(),idPrep)
    
    def test_get_identifier_prep0(self):
        """asserts the maternal identifier exists as a subject identifier object"""
        self.infantId.maternal_identifier='056-19800001-3'
        self.assertRaises(IdentifierError,self.infantId.get_identifier_prep)
    
    def test_get_identifier_prep1(self):
        """asserts the method guards against trying to register more infants than are alive"""
        self.infantId.live_infants_to_register=4
        self.assertRaises(IdentifierError,self.infantId.get_identifier_prep)
        
    def test_get_identifier_prep2(self):
        """asserts the method guards against registering deceased infants"""
        self.infantId.live_infants=0
        self.assertRaises(IdentifierError,self.infantId.get_identifier_prep)
        
    def test_get_suffix(self):
        self.assertEqual(self.infantId._get_suffix(),56)
        
    def test_base_suffix(self):
        self.assertEqual(self.infantId._get_base_suffix(),36)
           
    def test_get_identifier_post(self):
        self.identifier = SubjectIdentifier(model_name = 'subjectidentifier', app_name = 'edc_identifier', identifier_prefix = '066',
                                             is_derived=False, site_code='19', add_check_digit=False)
        self.identifier.modulus = 7
        subjectId1 = self.identifier.get_identifier(add_check_digit=True)
        print(self.infantId.get_identifier_post(new_identifier=subjectId1))