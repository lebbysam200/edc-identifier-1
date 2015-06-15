import re
from django.test import TestCase
from ..classes import CheckDigit

class TestCheckDigitMethods(TestCase): 
    
    def setUp(self):
        self.identifier = '066-12980443'
        self.number = int(re.search(r'\d+', self.identifier).group())
   
    def test_check_digit_with_correct_output(self):
        """test if the expected check digit is returned"""
        checkDigit = self.number % 7
        self.assertEqual(CheckDigit.calculate(self.identifier, self.number),checkDigit)

    def test_check_digit_with_wrong_output(self):
        """test if method guards against unexpected output"""
        checkDigit = self.number % 10
        self.assertNotEqual(CheckDigit.calculate(self.identifier,self.number),checkDigit)

    def test_check_digit_with_incorrect_input(self):
        """check if method guards against incorrect input"""
        self.number = "something"
        self.assertRaises(ValueError,CheckDigit.calculate,self.identifier,self.number)
        
