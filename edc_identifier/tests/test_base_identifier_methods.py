from django.test import TestCase

from ..classes import SubjectIdentifier

class TestModelTestCase(TestCase):
    
    def setUp(self):
        is_derived = False
        add_check_digit = False
        self.identifier = SubjectIdentifier(model_name = 'subjectidentifier', app_name = 'edc_identifier', identifier_prefix = '066',
                                            is_derived=is_derived, site_code='12', add_check_digit=add_check_digit)
        self.identifier.modulus = 7
        
    def test_get_sequence_app_label(self):
        self.assertEqual(self.identifier._get_sequence_app_label(), 'edc_identifier')
        
    def test_get_identifier_post(self):
        self.assertEqual(self.identifier.get_identifier_post(identifier='038-12990001-1'),'038-12990001-1')
        
    def test_get_identifier_prep(self):
        self.assertEqual(self.identifier._get_identifier_prep(),
                         {'identifier_prefix': '066', 'site_code': '12', 'device_id': '99'})
        
    def test_get_check_digit(self):
        self.assertEqual(self.identifier.get_check_digit(base_new_identifier = '038-12990002'),'038-12990002')
        
    def test_get_check_digit1(self):
        self.identifier.add_check_digit = True
        self.assertEqual(self.identifier.get_check_digit(base_new_identifier = '038-12990002'),'038-12990002-3')
    
    def test_get_identifier(self):
        add_check_digit = True
        """assert that the first identifier created is 066-12990001-2"""
        self.assertEqual(self.identifier.get_identifier(add_check_digit=add_check_digit),'066-12990001-2')
    
    def test_get_identifier1(self):
        add_check_digit = False
        self.assertEqual(self.identifier.get_identifier(add_check_digit=add_check_digit),'066-12990001')
        
    def test_get_identifier2(self):
        self.identifier.add_check_digit = None
        self.assertRaises(AttributeError,self.identifier.get_identifier,self.identifier.add_check_digit)
        
    def test_get_identifier3(self):
        self.identifier.is_derived = None
        self.assertRaises(AttributeError,self.identifier.get_identifier,self.identifier.add_check_digit)
        
    def test_get_identifier4(self):
        add_check_digit = True
        identifier1 = self.identifier.get_identifier(add_check_digit=add_check_digit)
        self.assertNotEqual(self.identifier.get_identifier(add_check_digit=add_check_digit),identifier1)
        
