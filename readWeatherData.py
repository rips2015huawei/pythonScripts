# coding: utf-8
import json
import pandas as pd;
import datetime

weatherSummary = open('wundergroundData_dailySummary.json', 'r')
w = json.loads(weatherSummary.read())
df_weatherSummary = pd.io.json.read_json(json.dumps(w))
df_weatherSummary = pd.DataFrame(df_weatherSummary)


weatherObserved = open('wundergroundObserved.json', 'r')
w = json.loads(weatherObserved.read())
df_weatherObserved = pd.io.json.read_json(json.dumps(w))
df_weatherObserved = pd.DataFrame(df_weatherObserved)

df_weatherSummary.head()
df_weatherObserved.head()



def returnDatestamp(yr, mnth, day, hr, min):
    return pd.to_datetime(str(yr) + str(mnth) + str(day) + ' ' + str(hr) + str(min), format = "%Y%m%d %H%M")

def returnDatestampDate(yr, mnth, day):
    return pd.to_datetime(str(yr) +' '+ str(mnth)+ ' '+ str(day), format = "%Y %m %d")

o = df_weatherObserved
# Initialize to any date, don't care, just necessary ot run the loop.
o['date'] = datetime.datetime(2012,1,12)
for i in range (0, len(o)):
    o['date'][i] = returnDatestamp(o['year'][i], o['month'][i], o['day'][i], o['hour'][i], o['min'][i])

df_weatherObserved['date'] # check to see if datetime success

df_weatherSummary['date'] = datetime.datetime(2012, 1, 12)
o = df_weatherSummary
for i in range (0, len(o)):
    o['date'][i] = returnDatestampDate(o['year'][i], o['month'][i], o['day'][i])
df_weatherSummary = o
df_weatherSummary['date'] # check to see if datetime success
