'''
Created on Nov 4, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.UtilClass import Util
import datetime

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
    
    def testIsDate(self):
        self.assertEquals(self._util.isValidDate("24.12.2012"), True)
        self.assertEquals(self._util.isValidDate("34.12.2012"), False)
    def validateDate(self):
        self.assertEquals(self._util.validateDate("24-12-2012"),"24.12.2012")
        self.assertEquals(self._util.validateDate("34-25-2004"),None)
    def testIsISBN(self):
        self.assertEquals(self._util.isISBN("1234567891012"), True)
        self.assertEquals(self._util.isISBN("123456"), False)
    def testIsFloat(self):
        self.assertEqual(self._util.isFloat("17,15555"), True)
        self.assertFalse(self._util.isFloat("15,15,2"),False)
    def testValidateFloat(self):
        self.assertEqual(self._util.validateFloat("1'117.5555"),"1117,5555")
    def testIsValidVekovaDostupnost(self):
        self.assertEqual(self._util.isValidVekovaDostupnost("20"),True)
        self.assertEqual(self._util.isValidVekovaDostupnost("250"),False)
    def testValidateVekovaDostupnost(self):
        self.assertEquals(self._util.validateVekovaDostupnost("+50"),50)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()