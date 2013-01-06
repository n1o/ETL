'''
Created on Jan 5, 2013

@author: marek
'''
import unittest
from sk.marek.barak.app.DatabaseLoaderContainer import *

class Test(unittest.TestCase):
    
    def setUp(self):
        self.__container__ = DatabaseLoaderContainer()
        
    @unittest.skip("TESTED")
    def testLoaderContainerZakaznik(self):
        l = list()
        l.append("typ_zakaznika")
        l.append("pravna_forma")
        l.append("nazov_meno")
        l.append("adresa")
        l.append("mesto")
        l.append("tel_kontakt")
        l.append("mail")
        l.append("bankove_spojenie")
        l.append("ico")
        l.append("dic")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(),str(l))
    
    @unittest.skip("TESTED")    
    def testLoaderContainerCas(self):
        l = list()
        l.append("rok")
        l.append("mesiac")
        l.append("den")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(),str(l))
    
    @unittest.skip("TESTED")    
    def testLoaderContainerDodavatel(self):
        l = list()
        l.append("nazov")
        l.append("sidlo")
        l.append("c_uctu")
        l.append("ico")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(),str(l))
    
    @unittest.skip("TESTED")    
    def testLoaderContainerFaktura(self):
        l = list()
        l.append("xml_generated")
        l.append("vystavena")
        l.append("zaplatena")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEqual(dbLoader.getKey(), str(l))
    
    @unittest.skip("TESTED")
    def testLoaderContainerPobocka(self):
        l = list()
        l.append("id_zamestnanca")
        l.append("mesto")
        l.append("okres")
        l.append("kraj")
        l.append("adresa")
        l.append("tel_kontakt")
        l.append("id_manazera")
        l.append("mail")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEqual(dbLoader.getKey(), str(l))
    
    @unittest.skip("TESTED")
    def testLoaderContainerTovar(self):
        l=list()
        l.append("kategoria")
        l.append("nazov_tovaru")
        l.append("platforma")
        l.append("jazykova_mutacia")
        l.append("rozsah")
        l.append("datum_vydania")
        l.append("autor")
        l.append("vydavatel")
        l.append("popis")
        l.append("isbn")
        l.append("cena")
        l.append("vekova_dostupnost")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEqual(dbLoader.getKey(), str(l))
    
    @unittest.skip("TESTED")
    def testLoaderContainerZamestnanec(self):
        l=list()
        l.append("meno")
        l.append("priezvisko")
        l.append("pozicia")
        l.append("nadriadeny")
        l.append("mail")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(),str(l))
    
    @unittest.skip("TESTED")
    def testLoaderContainerDodavka(self):
        l = list()
        l.append("id_zamestnanca")
        l.append("id_tovaru")
        l.append("id_dodavatela")
        l.append("cas")
        l.append("poznamka")
        l.append("pocet_ks")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(),str(l))
    
    @unittest.skip("TESTED")
    def testLoaderContainerObjednavka(self):
        l= list()
        l.append("id_faktury")
        l.append("id_zamestnanca")
        l.append("id_tovaru")
        l.append("cas")
        l.append("id_objednavky")
        l.append("suma")
        l.append("vybavenie")
        l.append("poznamka")
        l.append("prevzatie")
        l.append("platba")
        l.append("stav_objednavky")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(), str(l))
    
    @unittest.skip("TESTED")
    def testLoaderContainerReklamacia(self):
        l = list()
        l.append("id_dodavatela")
        l.append("id_zamestnanca")
        l.append("cas")
        l.append("popis_chyby")
        l.append("uznanie")
        l.append("vybavenie")
        l.append("zdovodnenie")
        l.append("pocet_ks")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(),str(l))
        
    @unittest.skip("TESTED")
    def testLoaderContainerSklad(self):
        l = list()
        l.append("id_zamestnanca")
        l.append("id_pobocky")
        l.append("id_tovaru")
        l.append("cas")
        l.append("pocet_kusov")
        l.append("dostupnost_tovaru")
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(), str(l))
    
    def testLoaderContainerSluzbyZakaznikom(self):
        l = list()
        l.append("cas")
        l.append("id_tovaru")
        l.append("id_zamestnanca")
        l.append("id_pobocky")
        l.append("id_zakaznika")
        l.append("popis")
        l.append("text_dotazu")
        l.append("text_odpovede")
        l.append("uspesne_vybavenie")
        print str(l)
        dbLoader = self.__container__.getElement(str(l))
        self.assertEquals(dbLoader.getKey(), str(l))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoaderContainer']
    unittest.main()