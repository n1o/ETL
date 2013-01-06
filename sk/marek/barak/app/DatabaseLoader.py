'''
Created on Dec 14, 2012

@author: marek
'''
import psycopg2

class BaseLoader(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.conx=psycopg2.connect(database="BI", user="bi",port=5432,host="localhost",password="test")
        '''
        Constructor
        '''
    def load(self,elements):
        self.conx.close()
        
    def getKey(self):
        pass
    
class Dim_ZamestanecLoader(BaseLoader):
    def __init__(self):
        self.__key__ ="['meno', 'priezvisko', 'pozicia', 'nadriadeny', 'mail']"
        BaseLoader.__init__(self)
    
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into DIM_Zamestnanec(Meno,Priezvisko,Pozicia,Nadriadeny,mail)"
                 "values(%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
            
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
        
class Dim_DodavatelLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM DODAVATEL LOADER"
        self.__key__ = "['nazov', 'sidlo', 'c_uctu', 'ico']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into DIM_Dodavatel(Nazov,Sidlo,C_uctu,ICO)"
                 "values(%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class Dim_CasLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM CAS LOADER"
        self.__key__= "['rok', 'mesiac', 'den']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into Dim_Cas(ROK,MESIAC,DEN)"
                 "values(%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class DimTovarLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM TOVAR LOADER"
        self.__key__ ="['kategoria', 'nazov_tovaru', 'platforma', 'jazykova_mutacia', 'rozsah', 'datum_vydania', 'autor', 'vydavatel', 'popis', 'isbn', 'cena', 'vekova_dostupnost']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into DIM_Tovar(KATEGORIA,Nazov_tovaru,Platforma,Jazykova_mutacia,Rozsah,Datum_vydania,Autor,Vydavatel,Popis,ISBN,Cena,Vekova_dostupnost)"
                 "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class DimPobockaLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM POBOCKA LOADER"
        self.__key__ = "['id_zamestnanca', 'mesto', 'okres', 'kraj', 'adresa', 'tel_kontakt', 'id_manazera', 'mail']"
        BaseLoader.__init__(self)
        
    def load(self,elements):
        
        curA = self.conx.cursor()
        query = ("insert into DIM_Pobocka(ID_ZAMESTNANCA,Mesto,Okres,Kraj,Adresa,Tel_Kontakt,ID_Manazera,mail)"
                 "values(%s,%s,%s,%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,(item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0),item.pop(0)))
        self.conx.commit()
        self.conx.close()
    def getKey(self):
        return self.__key__
    
class DimZakaznikLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM ZAKAZNIK LOADER"
        self.__key__ = "['typ_zakaznika', 'pravna_forma', 'nazov_meno', 'adresa', 'mesto', 'tel_kontakt', 'mail', 'bankove_spojenie', 'ico', 'dic']"            
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into DIM_Zakaznik(typ_zakaznika,Pravna_forma,Nazov_Meno,Adresa,Mesto,Tel_kontakt,mail,Bankove_spojenie,ICO,DIC)"
                 "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
        
class DimFakturaLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM FAKTURA LOADER"
        self.__key__ = "['xml_generated', 'vystavena', 'zaplatena']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into DIM_Faktura(XML_generated,vystavena,zaplatena)"
                 "values(%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class FaktSluzbyZakaznikomLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT SLUZBY ZAKAZNIKOM LOADER"
        self.__key__= "['cas', 'id_tovaru', 'id_zamestnanca', 'id_pobocky', 'id_zakaznika', 'popis', 'text_dotazu', 'text_odpovede', 'uspesne_vybavenie']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into FAKT_Sluzby_zakaznikom(Cas,ID_Tovaru,ID_Zamestnanca,ID_Pobocky,ID_Zakaznika,Popis,Text_dotazu,Text_odpovede,Uspesne_vybavenie)"
                 "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
        
class FaktSkladLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT SKLAD LOADER"
        self.__key__ = "['id_zamestnanca', 'id_pobocky', 'id_tovaru', 'cas', 'pocet_kusov', 'dostupnost_tovaru']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("insert into fakt_sklad(id_zamestnanca,id_pobocky,id_tovaru,cas,pocet_kusov,dostupnost_tovaru) values (%s,%s,%s,%s,%s,%s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
            
class FaktObjednavkaLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT OBJEDNAVKA LOADER"
        self.__key__ = "['id_faktury', 'id_zamestnanca', 'id_tovaru', 'cas', 'id_objednavky', 'suma', 'vybavenie', 'poznamka', 'prevzatie', 'platba', 'stav_objednavky']"
        BaseLoader.__init__(self)
        
    def load(self,elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO fakt_objednavka(id_faktury, id_zamestnanca, id_tovaru, cas, id_objednavky,"+
                 "suma, vybavenie, poznamka, prevzatie, platba, stav_objednavky)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
    
    def getKey(self):
        return self.__key__
    
class FaktDodavkaLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT DODAVKA LOADER"
        self.__key__ = "['id_zamestnanca', 'id_tovaru', 'id_dodavatela', 'cas', 'poznamka', 'pocet_ks']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO fakt_dodavka(id_zamestnanca, id_tovaru, id_dodavatela, cas, poznamka, pocet_ks)"+
                 "VALUES (%s, %s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class FaktReklamaciaLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT REKLAMACIA LOADER"
        self.__key__ = "['id_dodavatela', 'id_zamestnanca', 'cas', 'popis_chyby', 'uznanie', 'vybavenie', 'zdovodnenie', 'pocet_ks']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO fakt_reklamacia(id_dodavatela, id_zamestnanca, cas, popis_chyby,"+
                 " uznanie, vybavenie, zdovodnenie, pocet_ks)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
    
    def getKey(self):
        return self.__key__