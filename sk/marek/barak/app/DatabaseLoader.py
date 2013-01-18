'''
Created on Dec 14, 2012

@author: marek
'''
import psycopg2


#base loader class all loader classes need to extend this class
class BaseLoader(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.conx=psycopg2.connect(database="BI", user="bi",port=5432,host="localhost",password="test") #connection to database
        '''
        Constructor
        '''
    def load(self,elements):
        self.conx.close()
    
    #Each loader is identified with a specific key,
    #the key is made from attribute names
    def getKey(self):
        pass
    
class Dim_ZamestanecLoader(BaseLoader):
    def __init__(self):
        self.__key__ ="['meno', 'priezvisko', 'pozicia', 'id_nadriadeny', 'mail']"
        BaseLoader.__init__(self)
    
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO zamestnanec_dim(meno, priezvisko, pozicia, id_nadriadeny, mail)"
                 "VALUES (%s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
            
        self.conx.commit() #changes are commited only if all values where succesfuly inserted
        self.conx.close()
        
    def getKey(self):
        return self.__key__
        
class Dim_DodavatelLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM DODAVATEL LOADER"
        self.__key__ = "['nazov', 'adresa', 'bankove_spojenie', 'ico', 'dic']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO dodavatel_dim(nazov, adresa, bankove_spojenie, ico, dic)"
                 "VALUES (%s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class Dim_CasLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM CAS LOADER"
        self.__key__= "['cas_znamka', 'rok', 'mesiac', 'den', 'den_v_tyzdni']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO cas_dim(cas_znamka, rok, mesiac, den, den_v_tyzdni)"+
                 "VALUES (%s, %s, %s, %s, %s)")
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
        query = ("INSERT INTO tovar_dim(kategoria, nazov_tovaru, platforma, jazykova_mutacia,"
                 " rozsah, datum_vydania, autor, vydavatel, popis, isbn, cena, vekova_dostupnost)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class DimPobockaLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM POBOCKA LOADER"
        self.__key__ = "['mesto', 'okres', 'kraj', 'adresa', 'telefonne_cislo', 'mail']"
        BaseLoader.__init__(self)
        
    def load(self,elements):
        
        curA = self.conx.cursor()
        query = ("INSERT INTO pobocka_dim(mesto, okres, kraj, adresa, telefonne_cislo, mail)"
                 "VALUES (%s, %s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
    def getKey(self):
        return self.__key__
    
class DimZakaznikLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM ZAKAZNIK LOADER"
        self.__key__ = "['pravna_forma', 'nazov_meno', 'adresa', 'mesto', 'okres', 'kraj', 'telefonne_cislo', 'mail', 'bankove_spojenie', 'ico', 'dic']"            
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO zakaznik_dim(pravna_forma, nazov_meno, adresa, mesto, okres,"
                 " kraj, telefonne_cislo, mail, bankove_spojenie, ico, dic)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
        
class DimFakturaLoader(BaseLoader):
    def __init__(self):
        print "INIT DIM FAKTURA LOADER"
        self.__key__ = "['telo_faktury', 'vystavena', 'zaplatena']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO faktura_dim(telo_faktury, vystavena, zaplatena)"
                 "VALUES (%s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
    
class FaktSluzbyZakaznikomLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT SLUZBY ZAKAZNIKOM LOADER"
        self.__key__= "['id_cas', 'id_tovar', 'id_zamestnanec', 'id_pobocka', 'id_zakaznik', 'druh_otazky', 'text_otazky', 'text_odpovede', 'uspesne_vybavenie']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO sluzby_zakaznikom_fakt(id_cas, id_tovar, id_zamestnanec, id_pobocka, id_zakaznik, druh_otazky, "
                 "text_otazky, text_odpovede, uspesne_vybavenie)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
        
class FaktSkladLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT SKLAD LOADER"
        self.__key__ = "['id_cas', 'id_pobocka', 'id_tovar', 'id_zamestnanec', 'pocet_kusov', 'dostupnost_tovaru']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO sklad_fakt(id_cas, id_pobocka, id_tovar, id_zamestnanec, pocet_kusov, dostupnost_tovaru)"
                 "VALUES (%s, %s, %s, %s, %s, %s);")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
        
    def getKey(self):
        return self.__key__
            
class FaktObjednavkaLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT OBJEDNAVKA LOADER"
        self.__key__ = "['id_faktura', 'id_zamestnanec', 'id_tovar', 'id_zakaznik', 'id_cas', 'id_pobocka', 'suma', 'naklady', 'vybavenie', 'poznamka', 'prevzatie', 'platba', 'stav_objednavky']"
        BaseLoader.__init__(self)
        
    def load(self,elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO objednavka_fakt(id_faktura, id_zamestnanec, id_tovar, id_zakaznik, id_cas, id_pobocka, "
                 "suma, naklady, vybavenie, poznamka, prevzatie, platba, stav_objednavky)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
    
    def getKey(self):
        return self.__key__
    
class FaktDodavkaLoader(BaseLoader):
    def __init__(self):
        print "INIT FAKT DODAVKA LOADER"
        self.__key__ = "['id_zamestnanec', 'id_dodavatel', 'id_cas', 'id_tovar', 'poznamka', 'pocet_kusov']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO dodavka_fakt(id_zamestnanec, id_dodavatel, id_cas, id_tovar, poznamka, pocet_kusov)"
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
        self.__key__ = "['id_zakaznik', 'id_zamestnanec', 'vybavuje_dodavatel', 'id_cas', 'id_tovar', 'popis_chyby', 'uznanie', 'vybavenie', 'zdovodnenie', 'pocet_kusov']"
        BaseLoader.__init__(self)
        
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO reklamacia_fakt(id_zakaznik, id_zamestnanec, vybavuje_dodavatel, id_cas, id_tovar, "
                 "popis_chyby, uznanie, vybavenie, zdovodnenie, pocet_kusov)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
    
    def getKey(self):
        return self.__key__
    
class FaktZamestnanecPobockaLoader(BaseLoader):
    def __init__(self):
        print "INIT ZAMESTNANEC POBOCKA LOADER"
        self.__key__ = "['id_zamestnanec', 'id_pobocka']"
        BaseLoader.__init__(self)
    def load(self, elements):
        curA = self.conx.cursor()
        query = ("INSERT INTO zamestnanec_pobocka_fakt(id_zamestnanec, id_pobocka)"
                 "VALUES (%s, %s);")
        for item in elements:
            curA.execute(query,item)
        self.conx.commit()
        self.conx.close()
    def getKey(self):
        return self.__key__

