'''
Created on Dec 14, 2012

@author: marek
'''
import mysql.connector
from lib2to3.pytree import Base
from lxml.html.builder import BASE

class BaseLoader(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
        '''
        Constructor
        '''
    def load(self,elements):
        pass
    
class Dim_ZamestanecLoader(BaseLoader):
    def load(self, elements):
        conx = mysql.connector.connect(user='bi',database='BI')
        curA = conx.cursor(buffered=True)
        query = ("insert into DIM_Zamestnanec(Meno,Priezvisko,Pozicia,Nadriadeny,mail)"
                 "values(%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,(item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0)))
            conx.commit()
        conx.close()    
    def __init__(self):
        print "INIT ZAMESTNANEC LOADER"
        
class Dim_DodavatelLoader(BaseLoader):
    def __init__(self):
        print "INIT DODAVATEL LOADER"
    def load(self, elements):
        conx = mysql.connector.connect(user='bi',database='BI')
        curA = conx.cursor(buffered=True)
        query = ("insert into DIM_Dodavatel(Nazov,Sidlo,C_uctu,ICO)"
                 "values(%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,(item.pop(0),item.pop(0),item.pop(0),item.pop(0)))
            conx.commit()
        conx.close()
class Dim_CasLoader(BaseLoader):
    def __init__(self):
        print "INIT CAS LOADER"
    def load(self, elements):
        conx = mysql.connector.connect(user='bi',database='BI')
        curA = conx.cursor(buffered=True)
        query = ("insert into Dim_Cas(ROK,MESIAC,DEN)"
                 "values(%s,%s,%s)")
        for item in elements:
            curA.execute(query,(item.pop(0),item.pop(0),item.pop(0)))
            conx.commit()
        conx.close()
class DimTovarLoader(BaseLoader):
    def __init__(self):
        print "INIT TOVAR LOADER"
    def load(self, elements):
        conx = mysql.connector.connect(user='bi',database='BI')
        curA = conx.cursor(buffered=True)
        query = ("insert into DIM_Tovar(KATEGORIA,Nazov_tovaru,Platforma,Jazykova_mutacia,Rozsah,Datum_vydania,Autor,Vydavatel,Popis,ISBN,Cena,Vekova_dostupnost)"
                 "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,(item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0)))
            conx.commit()
        conx.close()
class DimPobockaLoader(BaseLoader):
    def __init__(self):
        print "INTI POBOCKA LOADER"
    def load(self,elements):
        conx = mysql.connector.connect(user='bi',database='BI')
        curA = conx.cursor(buffered=True)
        query = ("insert into DIM_Pobocka(ID_ZAMESTNANCA,Mesto,Okres,Kraj,Adresa,Tel_Kontakt,mail)"
                 "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,(item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0)))
            conx.commit()
        conx.close()