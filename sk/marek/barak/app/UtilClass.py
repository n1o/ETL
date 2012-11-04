'''
Created on Nov 2, 2012

@author: marek
'''
import re
from sre_parse import Pattern
class Util(object):
    
    def __init__(self):
        '''
        '''
    
    def isInteger(self,value):
        return isinstance(value, int)
    
    def canBeCastedToInteger(self, value):
        ex = re.compile("^\d+$|^[-+]\d+$" )
        return re.match(ex, value)
    
    def castToInteger(self,value):
        return int(value)
    
    def isPositive(self,value):
        return value>0
    
    def isBoolean(self,value):
        if isinstance(value, bool):
            return True
        else:
            ex = re.compile("True|False")
            if re.match(ex, value): return True
            else: return False
    
    def castStringToBoolean(self,value):
        exTrue = re.compile("true",re.IGNORECASE)
        exFalse = re.compile("false", re.IGNORECASE)
        exAno = re.compile("ano", re.IGNORECASE)
        exNie = re.compile("nie", re.IGNORECASE)
        if re.match(exTrue, value): return True
        elif re.match(exFalse, value): return False
        elif re.match(exAno, value): return True
        elif re.match(exNie, value): return False
        else: return None
    
    def canCastStringToBoolean(self,value):
        ex = re.compile("true|false|ano|nie", re.IGNORECASE)
        res = re.match(ex,value)
        if res != None:
            return res
        else : return False
        
         
    def castStringIntegerToBoolean(self,value):
        val = self.castToInteger(value)
        if val == 0:
            return False
        if val == 1:
            return True
        else:
            return None
        
    def isPrevzatie(self,values):
        pattern = re.compile("osobny odber|kurier|posta")
        ret = re.match(pattern, values)
        if ret !=None:
            return ret
        else : return False
        
    def valitedPrevzatie(self, values):
        pat1 = re.compile("osobny odber", re.IGNORECASE)
        pat2 = re.compile("kurier",re.IGNORECASE)
        pat3 = re.compile("posta", re.IGNORECASE)
        
        if re.match(pat1, values):
            return "osobny odber"
        if re.match(pat2, values):
            return "kurier"
        if re.match(pat3, values):
            return "posta"
        else:
            return None
    
    def isPlatba(self,values):
        pattern = re.compile("hotovost|prevod|online")
        ret = re.match(pattern, values)
        if ret !=None:
            return ret
        else: return False
    
    def validatePlatba(self,values):
        pat1 = re.compile("hotovost", re.IGNORECASE)
        pat2= re.compile("prevod", re.IGNORECASE)
        pat3 = re.compile("online", re.IGNORECASE)
        
        if re.match(pat1, values):
            return "hotovost"
        if re.match(pat2, values):
            return "prevod"
        if re.match(pat3, values):
            return "online"
        return None
    def isStavObjednavky(self,values):
        pattern = re.compile("vybavena|pripravena na expediciu|pripravuje sa|zrusena|prijata")
        ret = re.match(pattern, values)
        if ret !=None:
            return ret
        else: return False
        
    def validateStavObjednavky(self,value):
        pat1 = re.compile("vybavena", re.IGNORECASE)
        pat2= re.compile("pripravena na expediciu", re.IGNORECASE)
        pat3 = re.compile("pripravuje sa", re.IGNORECASE)
        pat4 = re.compile("zrusena", re.IGNORECASE)
        pat5 = re.compile("prijata", re.IGNORECASE)
        
        if re.match(pat1, value):
            return "vybavena"
        if re.match(pat2, value):
            return "pripravena na expediciu"
        if re.match(pat3, value):
            return "pripravuje sa"
        if re.match(pat4, value):
            return "zrusena"
        if re.match(pat5, value):
            return "prijata"
        return None
            
    def isValidName(self,value):
        pat = re.compile("^[A-Z][a-z]+$")
        ret = re.match(pat,value)
        if ret!=None:
            return ret
        else: return False
        
    def validateName(self,value):
        pat = re.compile("^[a-z]+$",re.IGNORECASE)
        if re.match(pat, value):
            print "match"
            val = value.lower()
            return val.capitalize()
        else : return None
        
    def isMailValid(self,mail):
        pat = re.compile("^[a-z0-9]+[._a-z0-9]+@[a-z0-9]+[._a-z0-9]*\.[a-z]{2,4}$",re.IGNORECASE)
        ret = re.match(pat,mail)
        if ret!=None:
            return ret
        else : return False
    def isTextValid(self,text):
        if len(text)<250:
            return True
        else : return False
        
    def castToBoolean(self,valueToValidate):
        if self.canBeCastedToInteger(valueToValidate): 
            val = self.castToInteger(valueToValidate)
            if val == 0:
                return False
            if val == 1:
                return True
        elif self.canCastStringToBoolean(valueToValidate):
            return self.castStringToBoolean(valueToValidate)
        else: return None
        
        
    