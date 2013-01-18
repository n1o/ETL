'''
Created on Nov 1, 2012

@author: marek
'''

from sk.marek.barak.app.UtilClass import Util

#Validator base class all validator classes need to exted this class
class ValidatorBaseClass(object):
    __util__ = Util()
        
    def __init__(self):

        '''
        Constructor
        '''
    #returns True if data is valid
    #else return False
    def isValid(self,value):
        '''
        Define the validating codition for value
        '''
        raise NotImplementedError
    
    #this method tries to validated given item, if it success it returns
    #validated value if not returns None
    def validate(self,valueToValidate):
        '''
        Define the validation opperation
        '''
        raise NotImplementedError
    
    
        
class SumaValidatorImpl(ValidatorBaseClass):
    '''
    Dont use depreciated. Use rather PositiveIntegerValidator
    '''


    def __init__(self):
       
        '''
        Constructor
        '''
    def isValid(self,value):
        return self.__util__.isValidInteger(value)
    
    def validate(self, valueToValidate): 
        return self.__util__.validateInteger(valueToValidate)
    
class VybaveneValidate(ValidatorBaseClass):
    def __init__(self):
            '''
            '''
    def isValid(self,value):
        return self.__util__.isBoolean(value)
    
    def validate(self,valueToValidate):
        return self.__util__.castToBoolean(valueToValidate)

class PrevzatieValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self.__util__.isPrevzatie(value)
    
    def validate(self, valueToValidate):
        return self.__util__.valitedPrevzatie(valueToValidate)
    
class PlatbaValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self.__util__.isPlatba(value)
    
    def validate(self, valueToValidate):
        return self.__util__.validatePlatba(valueToValidate)
    
class StavObjednavkyValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
            
    def isValid(self, value):
        return self.__util__.isStavObjednavky(value)
    
    def validate(self, valueToValidate):
        return self.__util__.validateStavObjednavky(valueToValidate)
    
class MenoZamestnancaValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
        
    def isValid(self, value):
        return self.__util__.isValidName(value)
    def validate(self, valueToValidate):
        return  self.__util__.validateName(valueToValidate)
    
class PriezvyskoZamesntancaValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self.__util__.isValidName(value)
    
    def validate(self, valueToValidate):
        return self.__util__.validateName(valueToValidate)

class MailValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isMailValid(value)
    def validate(self, valueToValidate):
        return None
class ValidateText(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isTextValid(value)
    
class ValidateUznanie(ValidatorBaseClass):
    '''
    Depreciated dont use
    '''
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isBoolean(value)
    def validate(self, valueToValidate):
        return self.__util__.castToBoolean(valueToValidate)
    
class PocetKSValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    
    def isValid(self, value):
        return self.__util__.isValidInteger(value)
    
    def validate(self, valueToValidate):
        return self.__util__.validateInteger(valueToValidate)
    
class CisloUctuValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isValidCisloUctu(value)
    def validate(self, valueToValidate):
        return ValidatorBaseClass.validate(self, valueToValidate)
    
class ICOValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isValidICO(value)
    
class BooleanValidator(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isBoolean(value)
    def validate(self, valueToValidate):
        return self.__util__.castToBoolean(valueToValidate)
    
class PositiveIntegerValidator(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isValidInteger(value)
    def validate(self, valueToValidate):
        return self.__util__.validateInteger(valueToValidate)
    
class DostupnostValidate(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isDostupnostTovaru(value)
    def validate(self, valueToValidate):
        return self.__util__.validateDostupnost(valueToValidate)
    
class DateValidator(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isValidDate(value)
    def validate(self, valueToValidate):
        return self.__util__.validateDate(valueToValidate)
class IsbnValidator(ValidatorBaseClass):
    
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isISBN(value)
    def validate(self, valueToValidate):
        return None
    
class FloatValidator(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isFloat(value);
    def validate(self, valueToValidate):
        return self.__util__.validateFloat(valueToValidate);
    
class XMLValidator(ValidatorBaseClass):
    def __init__(self):
        ValidatorBaseClass.__init__(self)
    def isValid(self, value):
        return self.__util__.isValidXML(value)
    def validate(self, valueToValidate):
        return self.__util__.validateXML(valueToValidate)
    