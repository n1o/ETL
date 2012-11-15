'''
Created on Nov 4, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.ValidatorClasses import *

class Test(unittest.TestCase):
    booleanValidate = BooleanValidator()
    primeNumber = PositiveIntegerValidator()
    dateValidator = DateValidator()
    isbnValidator = IsbnValidator()
    floatValidator = FloatValidator()
    
    
    def testbooleanIsValid(self):
        self.assertTrue(self.booleanValidate.isValid("False"))
        self.assertFalse(self.booleanValidate.isValid("false"))
    def testbooleanvalidate(self):
        
        self.assertTrue(self.booleanValidate.validate("Ano"))
    def testIsValidPrimeNumber(self):
        self.assertFalse(self.primeNumber.isValid("-15"))
    def testIsValidDate(self):
        self.assertEquals(self.dateValidator.isValid("10.5.2004"),True)
        self.assertEquals(self.dateValidator.isValid("29.2.2011"),False)
    def testValidateDate(self):
        self.assertEquals(self.dateValidator.validate("10-5-2004"),"10.5.2004")
    def testIsValidISBN(self):
        self.assertEquals(self.isbnValidator.isValid("1234567891234"), True)
        self.assertEquals(self.isbnValidator.isValid("12345671234"), False)
    def testValidateISBN(self):
        self.assertEqual(self.isbnValidator.validate("1544548785525"),None)
    def testIsFloat(self):
        self.assertEqual(self.floatValidator.isValid("1,35"), True)
        self.assertEqual(self.floatValidator.isValid("14.5"), False)
    def testValidateFloat(self):
        self.assertEqual(self.floatValidator.validate("15.5"),"15,5")
        self.assertEquals(self.floatValidator.validate("14 14.5"), "1414,5")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()