'''
Created on Nov 2, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.UtilClass import Util


class Test(unittest.TestCase):
    
    def setUp(self):
        self.__util__ = Util()

    def testIsInteger(self):
        self.assertTrue(self.__util__.isInteger(10))
    
    def testIsNotINteger(self):
        self.assertFalse(self.__util__.isInteger("a"));
        
    def testCanConvertToInteger(self):
        self.assertTrue(self.__util__.canBeCastedToInteger("10"))
    
    def testCanNotConvertToInteger(self):
        self.assertFalse(self.__util__.canBeCastedToInteger("b1"))
    
    def testCastToInteger(self):
        self.assertTrue(self.__util__.castToInteger("100"))
    
    def testIsPositive(self):
        self.assertTrue(self.__util__.isPositive(10))
    
    def testIsBoolean(self):
        self.assertTrue(self.__util__.isBoolean("False"))
        self.assertTrue(self.__util__.isBoolean("True"))
        self.assertFalse(self.__util__.isBoolean("Tkrue"))
        self.assertFalse(self.__util__.isBoolean("nie"))
    
    def testCastStringIntegerToBoolean(self):
        self.assertTrue(self.__util__.castStringIntegerToBoolean("1"))
        self.assertFalse(self.__util__.castStringIntegerToBoolean("0"))
    
    def testCastStringToBoolean(self):
        self.assertTrue(self.__util__.castStringToBoolean("tRue"))
        self.assertFalse(self.__util__.castStringToBoolean("falSe"))
        self.assertEquals(self.__util__.castStringToBoolean("fsa"),None)
        self.assertTrue(self.__util__.castStringToBoolean("Ano"))
    
    def testCanCastStringToBoolean(self):
        self.assertTrue(self.__util__.canCastStringToBoolean("true"))
        self.assertTrue(self.__util__.canCastStringToBoolean("false"))
        self.assertFalse(self.__util__.canCastStringToBoolean("trssd"))
        self.assertTrue(self.__util__.canCastStringToBoolean("ano"))
        
    def testIsPrevzatie(self):
        self.assertEquals(self.__util__.isPrevzatie("kurier"),True)
        self.assertEquals(self.__util__.isPrevzatie("posta"),True)
        self.assertEquals(self.__util__.isPrevzatie("osobny odber"),True)
        self.assertEquals(self.__util__.isPrevzatie("osob odber"),False)
        
    def testIsPlatba(self):
        self.assertEquals(self.__util__.isPlatba("hotovost"),True)
        self.assertEquals(self.__util__.isPlatba("online"),True)
        self.assertEquals(self.__util__.isPlatba("prevod"),True)
        self.assertEquals(self.__util__.isPlatba("hotoVost"),False)
    def testPlatbaValidate(self):
        self.assertEqual(self.__util__.validatePlatba("Hotovost"),"hotovost")
        self.assertEqual(self.__util__.validatePlatba("oNliNe"), "online")
        self.assertEqual(self.__util__.validatePlatba("otovost"), None)
    
    def testIsStavObjednavky(self):
        self.assertEquals(self.__util__.isStavObjednavky("pripravena na expediciu"),True)
        self.assertEquals(self.__util__.isStavObjednavky("priprvena na expediciu"),False)
        
    def testStavObjednavkyValidate(self):
        self.assertEqual(self.__util__.validateStavObjednavky("Pripravena na expediciu"), "pripravena na expediciu")
        self.assertEqual(self.__util__.validateStavObjednavky("Priprave na expediciu"), None)
        
    def testNameIsValid(self):
        self.assertEquals(self.__util__.isValidName("Marek"),True)
        self.assertEquals(self.__util__.isValidName("jano"),False)
        
    def testNameValidate(self):
        self.assertEqual(self.__util__.validateName("marek"),"Marek")
        self.assertEqual(self.__util__.validateName("mar ek"),None)

    def testTextValid(self):
        self.assertEquals(self.__util__.isTextValid("Ano je valid"),True)
        value = ""
        for i in range(1000):
            value += str(i)
        self.assertEquals(self.__util__.isTextValid(value),False)
           
if __name__ == "__main__": 
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()