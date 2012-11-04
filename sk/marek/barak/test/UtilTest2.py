'''
Created on Nov 4, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.UtilClass import Util

class Test(unittest.TestCase):
    def setUp(self):
        self._util = Util()

    def testAdress(self):
        '''self.assertTrue(self._util.isValidAdress("Komarnanska 29"))
        '''
    def testCisloUctu(self):
        self.assertTrue(self._util.isValidCisloUctu("1234567891/1000"))
    def testICO(self):
        self.assertTrue(self._util.isValidICO("12345678"))
    def testIsDostupnost(self):
        self.assertTrue(self._util.isDostupnostTovaru("dostupne"))
        self.assertFalse(self._util.isDostupnostTovaru("Dostupne"))
    def testValidateDostupne(self):
        self.assertTrue(self._util.validateDostupnost("Dostupne"))
        self.assertTrue(self._util.validateDostupnost("Nedostupne"))
        self.assertTrue(self._util.validateDostupnost("NA obJedNavKu"))
    def testIsMutacia(self):
        self.assertTrue(self._util.isMutacia("CZE"))
        self.assertFalse(self._util.isMutacia("cze"))
    def testValidateMutacia(self):
        self.assertEqual(self._util.validateMutacia("cze"), "CZE")
    def testMailIsValid(self):
        self.assertTrue(self._util.isMailValid("mrk.barak@gmail.com"))
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()