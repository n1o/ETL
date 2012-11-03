'''
Created on Nov 2, 2012

@author: marek
'''
import re
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
        ex = re.compile("true|false", re.IGNORECASE)
        return re.match(ex, value)
    
     
        
        
        
    
        
        
    