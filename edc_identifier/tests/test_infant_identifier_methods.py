from django.test import TestCase
from ..classes import BaseIdentifier, InfantIdentifier
from edc.core.bhp_variables.models import StudySite


class TestInfantIdentifer(BaseIdentifier):
    
    class Meta:
        app_label = 'edc_identifier'

class TestModelTestCase(TestCase):

    def setUp(self):
        studySite = StudySite(site_code = 19, site_name = "Molepolole")
        self.infantId = InfantIdentifier(self, maternal_identifier = '056-19800001-3 ', study_site = studySite,
                                          birth_order=1, live_infants=1, live_infants_to_register=1, user=None)
        
    def test_get_identifier_prep(self):
        
        print(self.infantId.get_identifier_prep())