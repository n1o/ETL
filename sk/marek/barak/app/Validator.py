'''
Created on Nov 4, 2012

@author: marek
'''
import sys
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
    print header
    for row in ls:
        for i in range(len(row)):
            validator = container.getElement(header[i])
            val= validator.isValid(row[i])
            print header[i] +"   " +str(val) + "  " +row[i]
    
if __name__ == '__main__':
    main()