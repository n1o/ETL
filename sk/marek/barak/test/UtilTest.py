'''
Created on Nov 2, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.UtilClass import Util


class Test(unittest.TestCase):
    
    def setUp(self):
        self._util = Util()

    def testIsInteger(self):
        self.assertTrue(self._util.isInteger(10))
    
    def testIsNotINteger(self):
        self.assertFalse(self._util.isInteger("a"));
        
    def testCanConvertToInteger(self):
        self.assertTrue(self._util.canBeCastedToInteger("10"))
    
    def testCanNotConvertToInteger(self):
        self.assertFalse(self._util.canBeCastedToInteger("b1"))
    
    def testCastToInteger(self):
        self.assertTrue(self._util.castToInteger("100"))
    
    def testIsPositive(self):
        self.assertTrue(self._util.isPositive(10))
    
    def testIsBoolean(self):
        self.assertTrue(self._util.isBoolean("False"))
        self.assertTrue(self._util.isBoolean("True"))
        self.assertFalse(self._util.isBoolean("Tkrue"))
        self.assertFalse(self._util.isBoolean("nie"))
    
    def testCastStringIntegerToBoolean(self):
        self.assertTrue(self._util.castStringIntegerToBoolean("1"))
        self.assertFalse(self._util.castStringIntegerToBoolean("0"))
    
    def testCastStringToBoolean(self):
        self.assertTrue(self._util.castStringToBoolean("tRue"))
        self.assertFalse(self._util.castStringToBoolean("falSe"))
        self.assertEquals(self._util.castStringToBoolean("fsa"),None)
        self.assertTrue(self._util.castStringToBoolean("Ano"))
    
    def testCanCastStringToBoolean(self):
        self.assertTrue(self._util.canCastStringToBoolean("true"))
        self.assertTrue(self._util.canCastStringToBoolean("false"))
        self.assertFalse(self._util.canCastStringToBoolean("trssd"))
        self.assertTrue(self._util.canCastStringToBoolean("ano"))
        
    def testIsPrevzatie(self):
        self.assertTrue(self._util.isPrevzatie("kurier"))
        self.assertTrue(self._util.isPrevzatie("posta"))
        self.assertTrue(self._util.isPrevzatie("osobny odber"))
        self.assertFalse(self._util.isPrevzatie("osob odber"))
        
    def testIsPlatba(self):
        self.assertTrue(self._util.isPlatba("hotovost"))
        self.assertTrue(self._util.isPlatba("online"))
        self.assertTrue(self._util.isPlatba("prevod"))
        self.assertFalse(self._util.isPlatba("hotoVost"))
    def testPlatbaValidate(self):
        self.assertEqual(self._util.validatePlatba("Hotovost"),"hotovost")
        self.assertEqual(self._util.validatePlatba("oNliNe"), "online")
        self.assertEqual(self._util.validatePlatba("otovost"), None)
    
    def testIsStavObjednavky(self):
        self.assertTrue(self._util.isStavObjednavky("pripravena na expediciu"))
        self.assertFalse(self._util.isStavObjednavky("priprvena na expediciu"))
        
    def testStavObjednavkyValidate(self):
        self.assertEqual(self._util.validateStavObjednavky("Pripravena na expediciu"), "pripravena na expediciu")
        self.assertEqual(self._util.validateStavObjednavky("Priprave na expediciu"), None)
    def testNameIsValid(self):
        self.assertTrue(self._util.isValidName("Marek"))
        self.assertFalse(self._util.isValidName("jano"))
        
    def testNameValidate(self):
        self.assertEqual(self._util.validateName("marek"),"Marek")
        self.assertEqual(self._util.validateName("mar ek"),None)
    def testMailIsValid(self):
        self.assertTrue(self._util.isMailValid("mrk.barak@gmail.com"))
        
    def testTextValid(self):
        self.assertTrue(self._util.isTextValid("Ano je valid"))
        self.assertTrue(self._util.isTextValid("NO"))
                         
        
if __name__ == "__main__": 
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()