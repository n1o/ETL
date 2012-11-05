'''
Created on Nov 4, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.ValidatorConatiner import ValidatorContainer
from sk.marek.barak.app.ValidatorClasses import BooleanValidator


class Test(unittest.TestCase):
    validatorContainer =ValidatorContainer()

    def testValidatorConainer(self):
        validator  = self.validatorContainer.getElement("mail")
        self.assertEquals(validator.isValid("mrk.barak@gmail.com"),True)
        
    def testValidatorContainerGetNonExistingElement(self):
        self.assertEquals(self.validatorContainer.getElement("NotExisting"), None)
        
    
    def testRegisterValidator(self):
        validator = BooleanValidator()
        self.validatorContainer.registerElement("vypredane",validator)
        self.assertEquals(self.validatorContainer.getElement("vypredane"),validator)
        
    def testRegisterInvalidValidator(self):
        self.validatorContainer.registerElement("thing", dict())
        self.assertEquals(self.validatorContainer.getElement("thing"), None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()