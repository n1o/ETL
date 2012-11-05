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
        return self._util.isValidInteger(value)
    
    def validate(self, valueToValidate): 
        return self._util.validateInteger(valueToValidate)
    
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
    '''
    Depreciated dont use
    '''
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isBoolean(value)
    def validate(self, valueToValidate):
        return self._util.castToBoolean(valueToValidate)
    
class PocetKSValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self._util.isValidInteger(value)
    
    def validate(self, valueToValidate):
        return self._util.validateInteger(valueToValidate)
    
class CisloUctuValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isValidCisloUctu(value)
    def validate(self, valueToValidate):
        return ValidatorBaseClass.validate(self, valueToValidate)
    
class ICOValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isValidICO(value)
    
class BooleanValidator(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isBoolean(value)
    def validate(self, valueToValidate):
        return self._util.castToBoolean(valueToValidate)
    
class PositiveIntegerValidator(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isValidInteger(value)
    def validate(self, valueToValidate):
        return self._util.validateInteger(valueToValidate)
class DostupnostValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self._util.isDostupnostTovaru(value)
    def validate(self, valueToValidate):
        return self._util.validateDostupnost(valueToValidate)

    