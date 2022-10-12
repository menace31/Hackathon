from hackathon import *

def cleanData(data_B,minDate,maxDate):

    err = data_B[(data_B[" Q_FG"] != 0)]
    err += data_B[(data_B["    DATE"]<minDate)]
    err += data_B[(data_B["    DATE"]>maxDate)]

    print("erreur tri database = " + str(len(err)))

def allTest(data_B,minDate,maxDate):
    cleanData(data_B,minDate,maxDate)
    
allTest(data_B,minDate,maxDate)