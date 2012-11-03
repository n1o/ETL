'''
Created on Nov 1, 2012

@author: marek
'''

from sk.marek.barak.app.UtilClass import Util

class ValidatorBaseClass(object):
    _util = Util()
        
    def __init__(self):

        
        '''
        Constructor
        '''
    def isValid(self,value):
        '''
        Define the validating codition for value
        '''
    def validate(self,valueToValidate):
        '''
        Define the validation opperation
        '''
        
class SumaValidatorImpl(ValidatorBaseClass):
    '''
    classdocs
    '''


    def __init__(self):
       
        '''
        Constructor
        '''
    def isValid(self,value):
        if self._util.isInteger(value) and self._util.isPositive(value):
            return True
        elif self._util.canBeCastedToInteger(value) and self._util.isPositive(self._util.castToInteger(value)):
            return True
        else : return False
    
    def validate(self, valueToValidate): 
        if  self._util.isInteger(valueToValidate) and not self._util.isPositive(valueToValidate):
            return valueToValidate *(-1)
        elif self._util.canBeCastedToInteger(valueToValidate) and not self._util.isPositive(self._util.castToInteger(valueToValidate)):
            return self._util.castToInteger(valueToValidate) * (-1)
        elif self._util.canBeCastedToInteger(valueToValidate):
            return self._util.castToInteger(valueToValidate)
        else: return None
    
class VybaveneValidate(ValidatorBaseClass):
    def __init__(self):
            '''
            '''
        
    def isValid(self,value):
        return self._util.isBoolean(value)
    
            
        
        
    
    
    

    