# coding: utf-8
import json
import pandas

weatherSummary = open('wundergroundData_dailySummary.json', 'r')
w = json.loads(weatherSummary.read())
df_weatherSummary = pandas.io.json.read_json(json.dumps(w))
df_weatherSummary = pandas.DataFrame(df_weatherSummary)


weatherObserved = open('wundergroundObserved.json', 'r')
w = json.loads(weatherObserved.read())
df_weatherObserved = pandas.io.json.read_json(json.dumps(w))
df_weatherObserved = pandas.DataFrame(df_weatherObserved)

df_weatherSummary.head()
df_weatherObserved.head()
