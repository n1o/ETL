'''
Created on Nov 2, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.ValidatorClasses import SumaValidatorImpl
from sk.marek.barak.app.ValidatorClasses import VybaveneValidate

class Test(unittest.TestCase):
    sumValidator = SumaValidatorImpl()
    vybaveneValidator = VybaveneValidate()

    
    
    def testSumaIsValid(self):
       
        self.assertEqual(self.sumValidator.isValid('15'), True)
        self.assertEqual(self.sumValidator.isValid("16c"), False)
    
    def testSumaValidate(self):
        self.assertEqual(self.sumValidator.validate(-16),16)
        self.assertEqual(self.sumValidator.validate("+15"), 15)
        self.assertEqual(self.sumValidator.validate("-15"), 15)
        self.assertFalse(self.sumValidator.validate("c15"), 15)
    
    def testVybaveneIsValid(self):
        self.assertTrue(self.vybaveneValidator.isValid("True"))
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()