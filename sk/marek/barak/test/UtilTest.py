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
        self.assertEquals(self._util.isPrevzatie("kurier"),True)
        self.assertEquals(self._util.isPrevzatie("posta"),True)
        self.assertEquals(self._util.isPrevzatie("osobny odber"),True)
        self.assertEquals(self._util.isPrevzatie("osob odber"),False)
        
    def testIsPlatba(self):
        self.assertEquals(self._util.isPlatba("hotovost"),True)
        self.assertEquals(self._util.isPlatba("online"),True)
        self.assertEquals(self._util.isPlatba("prevod"),True)
        self.assertEquals(self._util.isPlatba("hotoVost"),False)
    def testPlatbaValidate(self):
        self.assertEqual(self._util.validatePlatba("Hotovost"),"hotovost")
        self.assertEqual(self._util.validatePlatba("oNliNe"), "online")
        self.assertEqual(self._util.validatePlatba("otovost"), None)
    
    def testIsStavObjednavky(self):
        self.assertEquals(self._util.isStavObjednavky("pripravena na expediciu"),True)
        self.assertEquals(self._util.isStavObjednavky("priprvena na expediciu"),False)
        
    def testStavObjednavkyValidate(self):
        self.assertEqual(self._util.validateStavObjednavky("Pripravena na expediciu"), "pripravena na expediciu")
        self.assertEqual(self._util.validateStavObjednavky("Priprave na expediciu"), None)
        
    def testNameIsValid(self):
        self.assertEquals(self._util.isValidName("Marek"),True)
        self.assertEquals(self._util.isValidName("jano"),False)
        
    def testNameValidate(self):
        self.assertEqual(self._util.validateName("marek"),"Marek")
        self.assertEqual(self._util.validateName("mar ek"),None)

    def testTextValid(self):
        self.assertEquals(self._util.isTextValid("Ano je valid"),True)
        value = ""
        for i in range(1000):
            value += str(i)
        self.assertEquals(self._util.isTextValid(value),False)
           
if __name__ == "__main__": 
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()