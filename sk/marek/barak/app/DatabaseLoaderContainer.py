'''
Created on Jan 5, 2013

@author: marek
'''
from sk.marek.barak.app.DatabaseLoader import *

class DatabaseLoaderContainer():
    
    def __init__(self):
        self.__zakLoader__  = DimZakaznikLoader()
        self.__zamLoader__ = Dim_ZamestanecLoader()
        self.__dodLoader__ =Dim_DodavatelLoader()
        self.__casLoader__ = Dim_CasLoader()
        self.__tovarLoader__ = DimTovarLoader()
        self.__pobockaLoader__ = DimPobockaLoader()
        self.__fakturaLoader__ = DimFakturaLoader()
        self.__faktSluzbyZakaznikomLoader__ = FaktSluzbyZakaznikomLoader()
        self.__faktSkladLoader__ = FaktSkladLoader()
        self.__faktObjednavkaLoader__ = FaktObjednavkaLoader()
        self.__faktDodavkaLoader__ = FaktDodavkaLoader()
        self.__faktReklamaciaLoader__ = FaktReklamaciaLoader()
        self.__faktZamPobocka__ = FaktZamestnanecPobockaLoader()
        
    def getElement(self,key):
        if key == self.__zakLoader__.getKey():
            return self.__zakLoader__
        
        if key == self.__zamLoader__.getKey():
            return self.__zamLoader__
        
        if key == self.__dodLoader__.getKey():
            return self.__dodLoader__
        
        if key == self.__casLoader__.getKey():
            return self.__casLoader__
        
        if key == self.__tovarLoader__.getKey():
            return self.__tovarLoader__
        
        if key == self.__pobockaLoader__.getKey():
            return self.__pobockaLoader__
        
        if key == self.__fakturaLoader__.getKey():
            return self.__fakturaLoader__
        
        if key == self.__faktSluzbyZakaznikomLoader__.getKey():
            return self.__faktSluzbyZakaznikomLoader__
        
        if key == self.__faktSkladLoader__.getKey():
            return self.__faktSkladLoader__
        
        if key == self.__faktObjednavkaLoader__.getKey():
            return self.__faktObjednavkaLoader__
        
        if key == self.__faktDodavkaLoader__.getKey():
            return self.__faktDodavkaLoader__
        
        if key == self.__faktReklamaciaLoader__.getKey():
            return self.__faktReklamaciaLoader__
        
        if key == self.__faktZamPobocka__.getKey():
            return self.__faktZamPobocka__
