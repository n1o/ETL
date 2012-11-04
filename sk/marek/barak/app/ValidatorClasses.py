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
        return None
    def validate(self,valueToValidate):
        '''
        Define the validation opperation
        '''
        return None
        
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
    
    def validate(self,valueToValidate):
        return self._util.castToBoolean(valueToValidate)


class PrevzatieValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self._util.isPrevzatie(value)
    
    def validate(self, valueToValidate):
        return self._util.valitedPrevzatie(valueToValidate)
    
class PlatbaValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self._util.isPlatba(value)
    
    def validate(self, valueToValidate):
        return self._util.validatePlatba(valueToValidate)
    
class StavObjednavkyValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
            
    def isValid(self, value):
        return self._util.isStavObjednavky(value)
    
    def validate(self, valueToValidate):
        return self._util.validateStavObjednavky(valueToValidate)
    
class MenoZamestnancaValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
        
    def isValid(self, value):
        return self._util.isValidName(value)
    def validate(self, valueToValidate):
        return  self._util.validateName(valueToValidate)
    
class PriezvyskoZamesntancaValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self._util.isValidName(value)
    
    def validate(self, valueToValidate):
        return self._util.validateName(valueToValidate)

class MailValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isMailValid(value)
    def validate(self, valueToValidate):
        return None
class ValidateText(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isTextValid(value)
    
class ValidateUznanie(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isBoolean(value)
    def validate(self, valueToValidate):
        return self._util.castToBoolean(valueToValidate)
        
    
        
            
        
        
    
    
    

    