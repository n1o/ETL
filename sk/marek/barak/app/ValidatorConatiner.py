'''
Created on Nov 4, 2012

@author: marek
'''
from sk.marek.barak.app.ValidatorClasses import *
class ValidatorContainer(object):
    '''
    classdocs
    '''


    def __init__(self):
       self._conainer = dict()
       self._conainer["mail"] = MailValidate()
       self._conainer["integer"] = PositiveIntegerValidator()
       
    def getElement(self,elementId):
        if elementId in self._conainer.keys():
            return self._conainer[elementId.lower()]
        else: return None
    def registerElement(self,Id,element):
        if isinstance(element, ValidatorBaseClass):
            self._conainer[Id] = element 