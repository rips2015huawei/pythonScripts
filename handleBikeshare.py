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
    info = str_.split('h');
    numHours = int(info[0])
    if (numHours > 23):
        noDays = int(np.floor(numHours/24))
        numHours = numHours % 24 
        if (noDays > 30):
            noMonths = int(np.floor(noDays/31))
            noDays = noDays % 31 + 1;
            str_ = str(noMonths) + '/' + str(noDays)+ ' ' + str(numHours) + 'h' + info[1] 
        else:
            str_ = '12/' + str(noDays) + ' ' + str(numHours) + 'h' + info[1]
    else:
        str_ = '11/1 ' + str_ # if no days, then set month as 11 --> false
    str_ = str_.replace('h', ':')
    str_ = str_.replace('sec.', '')
    str_ = str_.replace('s','')
    str_ = str_.replace('m',':')
    return str_

# Read in all csv files from current directoryy
allFiles = glob.glob("SystemData/2012/*.csv");
data = pd.DataFrame()
combinedData = []
for file_ in allFiles:
    df = pd.read_csv(file_
           ,names=[c1,c2, c3, c4, c5, c6, c7]
           ,index_col=False
           ,header = 0)
    format_ = '%m/%d/%y %H:%M'
    df[c1] = df[c1].apply(formatDuration)
    print df[c1]
    df[c1] = pd.to_datetime(df[c1], format = '%m/%d %H:%M:%S')
    df[c2] = pd.to_datetime(df[c2], format = format_)
    df[c4] = pd.to_datetime(df[c4], format = format_)
    combinedData.append(df)

data = pd.concat(combinedData);
print '\nChecking data................\nPrinting head....\n'
print data.head()

casuals = pd.DataFrame(data.loc[data[c7] == 'Casual'])
registered = pd.DataFrame(data.loc[data[c7]=='Registered'])

print 'Casual Mean Duration:'
print casuals.mean(axis = 1)
print '\nRegistered Mean Duration:'
print registered.mean(axis = 1)


