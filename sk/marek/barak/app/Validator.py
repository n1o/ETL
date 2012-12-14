'''
Created on Nov 4, 2012

@author: marek
'''
import csv
from sk.marek.barak.app.ValidatorConatiner import ValidatorContainer

def getCsvContaint():
    lst = []
    with open("in.csv", 'rb') as csvFile:
        dialect = csv.Sniffer().sniff(csvFile.read(1024))
        csvFile.seek(0)
        reader = csv.reader(csvFile, dialect)
        for row in reader:
            lst.append(row)
        return lst
    
def main():
    print "Start"
    container = ValidatorContainer()
    ls = getCsvContaint()
    header = ls.pop(0)
    invalidLines = []
    validLine = []
    validLines = []
    
    print header
    for row in ls:
        for i in range(len(row)):
            validator = container.getElement(header[i])
            if validator is not None:    
                if not validator.isValid(row[i]):
                    validateValue = validator.validate(row[i])
                    if validateValue is None:
                        invalidElement = "Invalid "+header[i]+str(row)
                        invalidLines.append(invalidElement)
                    else:
                        validLine.append(str(validateValue))
                else:
                    validLine.append(row[i])
            else: validLine.append(row[i])
        if len(validLine)==len(row):
            validLines.append(validLine)
        validLine=[]
        
    for line in validLines:
        print line
    print "-----------INVALID------------"
    print header
    for line in invalidLines:
        print line
        
if __name__ == '__main__':
    main()