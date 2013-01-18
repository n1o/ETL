'''
Created on Nov 4, 2012

@author: marek
'''
from sk.marek.barak.app.ValidatorClasses import *
#Holds all validator classes
#Wraped HashMap
class ValidatorContainer(object):
    '''
    classdocs
    '''


    def __init__(self):
        self._container = dict()
        self.registerElement("mail", MailValidate())
        self.registerElement("integer", PositiveIntegerValidator())
        self.registerElement("uznanie", BooleanValidator())
        self.registerElement("c_uctu", CisloUctuValidate())
        self.registerElement("ico", ICOValidate())
        self.registerElement("meno", MenoZamestnancaValidate())
        self.registerElement("priezvisko",PriezvyskoZamesntancaValidate())
        self.registerElement("vystavena", BooleanValidator())
        self.registerElement("zaplatena", BooleanValidator())
        self.registerElement("pocet_ks",PositiveIntegerValidator())
        self.registerElement("telo_faktury", XMLValidator())
        self.registerElement("vybavenie", BooleanValidator())
        self.registerElement("uznanie", BooleanValidator)
        self.registerElement("pocet_kusov", PositiveIntegerValidator())
        self.registerElement("cas_znamka", DateValidator())
    
    #returns element only if it is contained inside validator container elese retruns
    #None
    def getElement(self,elementId):
        if elementId.lower() in self._container.keys():
            validator = self._container[elementId.lower()]
            if validator is not None:
                return validator
        else: return None
    #Registers element but onnly if it is a subclass of BaseValidator
    def registerElement(self,Id,element):
        if isinstance(element, ValidatorBaseClass):
            self._container[Id] = element 