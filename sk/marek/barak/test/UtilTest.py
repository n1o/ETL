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
        self.assertTrue(self._util.isBoolean("FALSE"))
        self.assertTrue(self._util.isBoolean("true"))
        self.assertFalse(self._util.isBoolean("Tkrue"))
    
        
        


if __name__ == "__main__": 
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()