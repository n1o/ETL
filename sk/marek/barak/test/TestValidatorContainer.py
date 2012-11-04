'''
Created on Nov 4, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.ValidatorConatiner import ValidatorContainer

class Test(unittest.TestCase):
    validatorContainer =ValidatorContainer()

    def testValidatorConainer(self):
        validator  = self.validatorContainer.getElement("mail")
        self.assertTrue(validator.isValid("mrk.barak@gmail.com"))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()