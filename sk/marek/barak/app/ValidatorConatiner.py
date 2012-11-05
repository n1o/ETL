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
        self._container = dict()
        self.registerElement("mail", MailValidate())
        self.registerElement("integer", PositiveIntegerValidator())
       
    def getElement(self,elementId):
        if elementId.lower() in self._container.keys():
            validator = self._container[elementId.lower()]
            if validator is not None:
                return validator
        else: return None
    def registerElement(self,Id,element):
        if isinstance(element, ValidatorBaseClass):
            self._container[Id] = element 