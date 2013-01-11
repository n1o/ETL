'''
Created on Jan 11, 2013

@author: marek
'''
import unittest
from sk.marek.barak.app.DatabaseLoader import *


class Test(unittest.TestCase):


    def testGetZakaznikKeys(self):
        zam = list()
        zam.append("pravna_forma")
        zam.append("nazov_meno")
        zam.append("adresa")
        zam.append("mesto")
        zam.append("okres")
        zam.append("kraj")
        zam.append("telefonne_cislo")
        zam.append("mail") 
        zam.append("bankove_spojenie")
        zam.append("ico")
        zam.append("dic")
        dbLoader = DimZakaznikLoader()
        self.assertEquals(str(zam),dbLoader.getKey())
        
    def testCasKeys(self):
        cas = list()
        cas.append("cas_znamka")
        cas.append("rok") 
        cas.append("mesiac")
        cas.append("den")
        cas.append("den_v_tyzdni")
        dbLoader = Dim_CasLoader()
        self.assertEquals(str(cas), dbLoader.getKey())
    
    def testDodavatelKeys(self):
        dod = list()
        dod.append("nazov")
        dod.append("adresa")
        dod.append("bankove_spojenie")
        dod.append("ico")
        dod.append("dic")
        dbLoader = Dim_DodavatelLoader()
        self.assertEquals(str(dod), dbLoader.getKey())
        
    def testDodavkaKeys(self):
        key = list()
        key.append("id_zamestnanec")
        key.append("id_dodavatel")
        key.append("id_cas")
        key.append("id_tovar")
        key.append("poznamka") 
        key.append("pocet_kusov")
        dbLoader = FaktDodavkaLoader()
        self.assertEquals(str(key),dbLoader.getKey())
    
    def testFakturaKey(self):
        key = list()
        key.append("telo_faktury")
        key.append("vystavena")
        key.append("zaplatena")
        dbLoader = DimFakturaLoader()
        self.assertEqual(str(key), dbLoader.getKey())
    
    def testObjednavkaKey(self):
        key = list()
        key.append("id_faktura")
        key.append("id_zamestnanec")
        key.append("id_tovar")
        key.append("id_zakaznik")
        key.append("id_cas")
        key.append("id_pobocka")
        key.append("suma")
        key.append("naklady")
        key.append("vybavenie")
        key.append("poznamka") 
        key.append("prevzatie") 
        key.append("platba")
        key.append("stav_objednavky")
        dbLoader = FaktObjednavkaLoader()
        self.assertEquals(str(key), dbLoader.getKey())
        
    def testPobockaKey(self):
        key = list()
        key.append("mesto") 
        key.append("okres")
        key.append("kraj") 
        key.append("adresa")
        key.append("telefonne_cislo")
        key.append("mail")
        dbLoader = DimPobockaLoader()
        self.assertEquals(str(key),dbLoader.getKey())
    
    def testReklamaciaKey(self):
        key = list()
        key.append("id_zakaznik")
        key.append("id_zamestnanec")
        key.append("vybavuje_dodavatel")
        key.append("id_cas")
        key.append("id_tovar") 
        key.append("popis_chyby")
        key.append("uznanie")
        key.append("vybavenie")
        key.append("zdovodnenie")
        key.append("pocet_kusov")
        dbLoader =  FaktReklamaciaLoader()
        self.assertEquals(str(key),dbLoader.getKey())
        
    def testSkladKey(self):
        key = list()
        key.append("id_cas")
        key.append("id_pobocka")
        key.append("id_tovar")
        key.append("id_zamestnanec")
        key.append("pocet_kusov")
        key.append("dostupnost_tovaru")
        dbLoader = FaktSkladLoader()
        self.assertEquals(str(key),dbLoader.getKey())
        
    def testSluzbyZakaznikomKey(self):
        key = list()
        key.append("id_cas")
        key.append("id_tovar")
        key.append("id_zamestnanec")
        key.append("id_pobocka")
        key.append("id_zakaznik")
        key.append("druh_otazky")
        key.append("text_otazky") 
        key.append("text_odpovede")
        key.append("uspesne_vybavenie")
        dbLoader = FaktSluzbyZakaznikomLoader()
        self.assertEquals(str(key),dbLoader.getKey())
    
    def testTovarDim(self):
        key = list()
        key.append("kategoria")
        key.append("nazov_tovaru") 
        key.append("platforma") 
        key.append("jazykova_mutacia")
        key.append("rozsah")
        key.append("datum_vydania")
        key.append("autor")
        key.append("vydavatel")
        key.append("popis")
        key.append("isbn")
        key.append("cena")
        key.append("vekova_dostupnost")
        dbLoader = DimTovarLoader()
        self.assertEquals(str(key),dbLoader.getKey())
    
    def testZamestaneckey(self):
        key = list()
        key.append("meno") 
        key.append("priezvisko")
        key.append("pozicia")
        key.append("id_nadriadeny")
        key.append("mail")
        dbLoader = Dim_ZamestanecLoader()
        self.assertEquals(str(key),dbLoader.getKey())
        
    def testZamPobockaKey(self):
        key = list()
        key.append("id_zamestnanec")
        key.append("id_pobocka")
        dbLoader = FaktZamestnanecPobockaLoader()
        self.assertEquals(str(key),dbLoader.getKey())
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetZamestnanecKeys']
    unittest.main()