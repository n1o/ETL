'''
Created on Nov 4, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.ValidatorClasses import BooleanValidator

class Test(unittest.TestCase):
    booleanValidate = BooleanValidator()

    def testbooleanIsValid(self):
        self.assertTrue(self.booleanValidate.isValid("False"))
        self.assertFalse(self.booleanValidate.isValid("false"))
    def testbooleanvalidate(self):
        
        self.assertTrue(self.booleanValidate.validate("Ano"))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()