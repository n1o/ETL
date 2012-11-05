'''
Created on Nov 2, 2012

@author: marek
'''
import unittest
from sk.marek.barak.app.ValidatorClasses import *


class Test(unittest.TestCase):
    sumValidator = SumaValidatorImpl()
    vybaveneValidator = VybaveneValidate()
    validatePrevzatie = PrevzatieValidate()
    platbaValidate = PlatbaValidate()
    stavObjednavky = StavObjednavkyValidate()
    menoZamestnancaValidate = MenoZamestnancaValidate()
    mailValidate = MailValidate()
    textValidator = ValidateText()
    uznanieValidate = ValidateUznanie()
    pocetKsValid = PocetKSValidate()
    dostupnostValid = DostupnostValidate()
    
    
    def testSumaIsValid(self):
       
        self.assertEqual(self.sumValidator.isValid('15'), True)
        self.assertEqual(self.sumValidator.isValid("16c"), False)
    
    def testSumaValidate(self):
        self.assertEqual(self.sumValidator.validate(-16),16)
        self.assertEqual(self.sumValidator.validate("+15"), 15)
        self.assertEqual(self.sumValidator.validate("-15"), 15)
        self.assertFalse(self.sumValidator.validate("c15"), 15)
    
    def testVybaveneIsValid(self):
        self.assertTrue(self.vybaveneValidator.isValid("True"))
        
    def testVybaveneValidate(self):
        self.assertEqual(self.vybaveneValidator.validate("1"),True)
        self.assertFalse(self.vybaveneValidator.validate("0"))
    
    def testPrevzatieIsValid(self):
        self.assertEquals(self.validatePrevzatie.isValid("osobny odber"),True)
        self.assertEquals(self.validatePrevzatie.isValid("kurier"),True)
        self.assertEquals(self.validatePrevzatie.isValid("posta"),True)
        self.assertEquals(self.validatePrevzatie.isValid("osobny Odber"),False)
    
    def tesPrevzatieValidate(self):
        self.assertEquals(self.validatePrevzatie.validate("Osobny odber"), "osobny odber")
        self.assertEquals(self.validatePrevzatie.isValid("osoy odber"),None)
        
    def testIsPlatba(self):
        self.assertEquals(self.platbaValidate.isValid("hotovost"),True)
        self.assertEquals(self.platbaValidate.isValid("Hotovost"),False)
    def testPlatbaValidate(self):
        self.assertEqual(self.platbaValidate.validate("Hotovost"), "hotovost")
        self.assertEqual(self.platbaValidate.validate("oNliNe"), "online")
        self.assertEqual(self.platbaValidate.validate("otovost"), None)
    
    def testStavObjednavkyIsValid(self):
        self.assertTrue(self.stavObjednavky.isValid("vybavena"))
        self.assertFalse(self.stavObjednavky.isValid("vBavena"))
    
    def testStavObjednavkyValidate(self):
        self.assertEqual(self.stavObjednavky.validate("VYbavena"), "vybavena")
        self.assertEqual(self.stavObjednavky.validate("zrusnena"), None)
    
    def testMenoZamestnancaIsValid(self):
        self.assertTrue(self.menoZamestnancaValidate.isValid("Marek"))
        self.assertFalse(self.menoZamestnancaValidate.isValid("marek"))
    def testMenoZamestnancaValidate(self):
        self.assertEqual(self.menoZamestnancaValidate.validate("marek"), "Marek")
        
    def testMailIsValid(self):
        self.assertTrue(self.mailValidate.isValid("mrk.barak@gmail.com"))
        self.assertFalse(self.mailValidate.isValid("mrk.&barak@gmail.com"))
    
    def testTextIsValid(self):
        self.assertTrue(self.textValidator.isValid("Haleluja"))
    
    def testUznanieIsValid(self):
        self.assertTrue(self.uznanieValidate.isValid("True"))
        self.assertFalse(self.uznanieValidate.isValid("false"))
    
    def tesUznanieValidate(self):
        self.assertTrue(self.uznanieValidate.validate("1"))
        self.assertFalse(self.uznanieValidate.validate("0"))
        self.assertTrue(self.uznanieValidate.validate("ano"))
    
    def testPocetKsIsValid(self):
        self.assertTrue(self.pocetKsValid.isValid("15"))
        self.assertFalse(self.pocetKsValid.isValid("16c"))
    
    def testPocetKsValidate(self):
        self.assertEqual(self.pocetKsValid.validate(-16),16)
        self.assertEqual(self.pocetKsValid.validate("+15"), 15)
        self.assertEqual(self.pocetKsValid.validate("-15"), 15)
        self.assertFalse(self.pocetKsValid.validate("c15"), 15)
        
    def testIsDotupnostTovaru(self):
        self.assertTrue(self.dostupnostValid.isValid("dostupne"))
        self.assertFalse(self.dostupnostValid.isValid("Na cEste"))
    def testValidateDostupnostTovaru(self):
        self.assertEqual(self.dostupnostValid.validate("NA obJedNavKu"), "na objednavku")
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()