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
        self.assertEquals(self._util.isValidCisloUctu("1234567891/1000"),True)
    def testICO(self):
        self.assertEquals(self._util.isValidICO("12345678"),True)
    def testIsDostupnost(self):
        self.assertEquals(self._util.isDostupnostTovaru("dostupne"),True)
        self.assertEquals(self._util.isDostupnostTovaru("Dostupne"),False)
    def testValidateDostupne(self):
        self.assertEquals(self._util.validateDostupnost("Dostupne"),"dostupne")
        self.assertEquals(self._util.validateDostupnost("Nedostupne"),"nedostupne")
        self.assertEquals(self._util.validateDostupnost("NA obJedNavKu"),"na objednavku")
    def testIsMutacia(self):
        self.assertEquals(self._util.isMutacia("CZE"),True)
        self.assertEquals(self._util.isMutacia("cze"),False)
    def testValidateMutacia(self):
        self.assertEqual(self._util.validateMutacia("cze"), "CZE")
    def testMailIsValid(self):
        self.assertEquals(self._util.isMailValid("mrk.barak@gmail.com"),True)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()