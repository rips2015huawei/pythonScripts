import pandas as pd
import datetime
import glob 
import pygmaps
import matplotlib.pyplot as plt
import matplotlib
import time
import numpy as np


# Column names:
c1 = "Duration"
c2 = "Start date"
c3 = "Start Station"
c4 = "End date"
c5 = "End Station"
c6 = "Bike#"
c7 = "Subscription Type"

def formatDuration(str_):
    str_ = str_.replace(' ','')
    str_ = str_.replace('h', ':')
    str_ = str_.replace('sec.','')
    str_ = str_.replace('s','')
    str_ = str_.replace('m',':')

    info = str_.split(':')
    noHours = int(info[0])
    noMin   = int(info[1])
    noSec   = int(info[2])
    
    time = float(noHours * 60 + noMin + (noSec * (1/60)))
   
    return time

def changeYearFormat(str_):
    str_ = str_.replace('-','/')
    str_ = str_.replace('2014','14')
    str_ = str_.replace('2015','15')
    info = str_.split('/');
    info2 = info[2].split(' ');
    if ((info[0] == '14') | (info[0] == '15')):
        str_ = info[1] + '/' + info2[0] +'/'+ info[0] + ' ' + info2[1]
    return str_


# Read in all csv files from current directoryy
allFiles = glob.glob("SystemData/*.csv");
data = pd.DataFrame()
combinedData = []
for file_ in allFiles:
    df = pd.read_csv(file_
           ,names=[c1,c2, c3, c4, c5, c6, c7]
           ,index_col=False
           ,header = 0)
    format_ = '%m/%d/%y %H:%M'
    df[c1] = df[c1].apply(formatDuration)
    df[c2] = df[c2].apply(changeYearFormat)
    df[c4] = df[c4].apply(changeYearFormat)
    df[c2] = pd.to_datetime(df[c2], format = format_)
    df[c4] = pd.to_datetime(df[c4], format = format_)
    combinedData.append(df)

data = pd.concat(combinedData);
print '\nChecking data................\nPrinting head....\n'
print data.head()

casuals = pd.DataFrame(data.loc[data[c7] == 'Casual'])
registered = pd.DataFrame(data.loc[data[c7]=='Registered'])


print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
print "\nYou now have three dataframes:\n"
print "\n 1. data       ~ contains all data from bikeshare data\n"
print "\n 2. casuals    ~ contains all data on casuals from data\n"
print "\n 3. registered ~ contains all data on registered from data\n"
print "\nCan run e.g. shortTrips = data.loc[data[c1] < 120]\nto get all trips less than 120 mins in duration.\n"
print "\nCan also run e.g. casuals.index = Casuals['Start date'] to index casuals by start date.\n"
print "\nColumn Listings, in order:" c1, ",", c2, ",", c3, ",", c4, ",", c5,",",c6,",",c7
