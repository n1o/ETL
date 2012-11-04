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
        return self._conainer[elementId.lower()]
    