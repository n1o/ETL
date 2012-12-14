'''
Created on Dec 14, 2012

@author: marek
INTEGRACNE TESTY
'''

import unittest
from sk.marek.barak.app.DatabaseLoader import *


class TestZamestnanecLoader(unittest.TestCase):
    
    @unittest.skip("Skip zam test")
    def testZamLoad(self):
        print "Zam loader test"
        dbLoader = Dim_ZamestanecLoader()
        l = list()
        l.append("Marek")
        l.append("Barak")
        l.append("Programator")
        l.append(1)
        l.append("mrk.barak@gmail.com")
        rows = list()
        s=list()
        s.append("Jaroslav")
        s.append("Hoblak")
        s.append("Ozran")
        s.append(1)
        s.append("jaroslav.hoblak@gmail.com")
        
        rows.append(l)
        rows.append(s)
        dbLoader.load(rows)
        self.assertEqual("A", "A")
        
    @unittest.skip("Skip Dod test")
    def testDodLoader(self):
        print "Dod loader test"
        dbLoader = Dim_DodavatelLoader()
        l = list()
        l.append("Prvy")
        l.append("Prve miesto")
        l.append("123456789/4587")
        l.append("12345678")
        s = list()
        s.append("Second")
        s.append("Druhe miesto")
        s.append("987654321/3216")
        s.append("98765432")
        row = list()
        row.append(l)
        row.append(s)
        dbLoader.load(row)
        
    @unittest.skip("Already tested")
    def testCasLoad(self):
        print "CAS load Test"
        dbLoad = Dim_CasLoader()
        l = list()
        s = list()
        l.append("2012")
        l.append("5")
        l.append("4")
        s.append("2011")
        s.append("12")
        s.append("13")
        row = list()
        row.append(s)
        row.append(l)
        dbLoad.load(row)
    @unittest.skip("Already tested")
    def testTovarLoader(self):
        dbLoader = DimTovarLoader()
        l = list()
        l.append("Kategoria Horor")
        l.append("Nazov T Kniha")
        l.append("Platforma 1")
        l.append("Mutacia CZE")
        l.append(600)
        l.append("1.12.2012")
        l.append("Marek Barak")
        l.append("Slov art")
        l.append("Volaco hlupeho")
        l.append("Prve ISBN")
        l.append(1525.5)
        l.append(18)
        row = list();
        row.append(l)
        s= list(l)
        row.append(s)
        dbLoader.load(row)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()