import pandas as pd
import numpy as np

def cleanData(data_B,minDate,maxDate):
    data_B = data_B[(data_B[" Q_FG"]==0)]
    data_B = data_B[(data_B["    DATE"]>=minDate)]
    data_B = data_B[(data_B["    DATE"]<=maxDate)]
    return data_B

# open and read data
data_E = pd.read_csv("../database/Elsenborn.csv", sep = ',')
data_B = pd.read_csv("../database/Beauvechain.csv", sep = ',')

minDate = 20170101
maxDate = 20210101

# sort the database to remove wrong data
data_B = cleanData(data_B,minDate,maxDate)