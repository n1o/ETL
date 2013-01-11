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
    def testLoaderContainerGetExistingKey(self):
        key = list()
        key.append("telo_faktury")
        key.append("vystavena")
        key.append("zaplatena")
        dbLoader = self.__container__.getElement(str(key))
        self.assertEqual(str(key), dbLoader.getKey())
    
    def testLoaderContainerForNotExistingKey(self):
        key = list()
        key.append("id_zakaznik")
        key.append("vystavena")
        dbLoader = self.__container__.getElement(str(key))
        self.assertIsNone(dbLoader)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoaderContainer']
    unittest.main()