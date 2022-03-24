from flask import session
#from models import CountyWiseData
from sqlalchemy import select
from models import CountyPopulation
# from models import db

def getcountydata(zipcode,db):
    res_json = {} 
    zipcode = str(zipcode).lstrip('0')  
    task = db.session.query(CountyPopulation).filter(CountyPopulation.zipCode==int(zipcode)).distinct()
    for row in task:
        print(row)
        res_json['county'] = row.county
        res_json['population'] = row.population
    
        print ("ID:", row.county)
        return res_json

def pigLatinConversion(inputString):
    pigLatindic ={}
    inputString = inputString.split(" ")
    outputString =""
    for x in range(0,len(inputString)):
        if(len(outputString)>0):

            outputString = outputString+ " " +pigLatinwordConverter(inputString[x])     
        else:
            outputString = outputString+pigLatinwordConverter(inputString[x])

    pigLatindic['name'] = outputString
    return pigLatindic



def vowelExists(letterVal):
    vowelList =['a','e','i','o','u']
    if letterVal.lower() in vowelList:
        return True
    else:
        return False    

def pigLatinwordConverter(inputString):
    stringPosition = 0
    for x in range(0,len(inputString)):
        if(vowelExists(inputString[x])==True):
            stringPosition = x
            break
    print(inputString[:x])
    if(stringPosition!=0):
        appendString = inputString[:x]
        inputString = inputString.replace(inputString[:x],'',x)
        inputString = inputString + appendString +"ay"
    else:
        inputString = inputString + "ay"   
    print(inputString)
    return inputString
