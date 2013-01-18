'''
Created on Nov 4, 2012

@author: marek
'''
import csv
import sys
from sk.marek.barak.app.ValidatorConatiner import ValidatorContainer
from sk.marek.barak.app.DatabaseLoaderContainer import DatabaseLoaderContainer

def getCsvContaint(file):
    lst = []
    with open(file, 'rb') as csvFile:
        dialect = csv.Sniffer().sniff(csvFile.read(1024)) #find csv dialect
        csvFile.seek(0) #start at the beginning
        reader = csv.reader(csvFile, dialect)
        for row in reader:
            lst.append(row)
        return lst
    
def main():
    print "Start"
    container = ValidatorContainer()
    file = sys.argv[1] #first argument csv file name
    ls = getCsvContaint(file)
    header = ls.pop(0) 
    invalidLines = list() 
    validLine = list()
    validLines = list()
    
    print header
    
    for row in ls: #for each row in csv files excluding header
        for i in range(len(row)): #for each element in an row
            validator = container.getElement(header[i]) #getting the appropiate
            if validator is not None:    
                if not validator.isValid(row[i]):
                    validateValue = validator.validate(row[i]) #try to validate
                    if validateValue is None:
                        invalidElement = "Invalid "+header[i]+str(row) 
                        invalidLines.append(invalidElement) #append the invalid element
                    else:
                        validLine.append(str(validateValue))
                else:
                    validLine.append(row[i]) #append valid element
            else: validLine.append(row[i]) #if a validator does't exist elements are not validated
        if len(validLine)==len(row): #append validated row, only if all items where valid
            validLines.append(validLine)
        validLine=list() # get clear list
       
    dbLoaderContainer = DatabaseLoaderContainer() #get database container
    dbLoader = dbLoaderContainer.getElement(str(header).lower()) #get database loader for csv based on header.
    print "Start to load: " + dbLoader.getKey()
    dbLoader.load(validLines)
    print "Load succesfull"
    
    #show invalid files
    for line in validLines:
        print line
        
    print "-----------INVALID------------"
    print header
    for line in invalidLines:
        print line
        
if __name__ == '__main__':
    main()