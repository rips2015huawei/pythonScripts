import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime
import Levenshtein
import glob
import xml.etree.ElementTree as ET


def checkDataForPeriods(s):
    if '.' in s:
        print 'Found .'
        return s.replace('.','')



def plotStations(stationNames):

    col1 = 'Start Station'
    col2 = 'End Station'

   # stationNames      = []
    stationNamesSplit = []

    tree = ET.parse('../xml_files/bikeStations.xml')
    root = tree.getroot()

    #riders[col1] = riders[col1].apply(checkDataForPeriods)
    #riders[col2] = riders[col2].apply(checkDataForPeriods)


    for station in root.findall('station'):
        name = station.find('name').text
        stationNames.append(name)
    stationNames.sort()
    i = 0;

    for x in stationNames:
        i = i+1
        print x
        #name = x.split(' ');
        #if name[0] == "18th":
            #print x
        if '-' in x:
            print x
    #    stationNamesSplit.append(x.split(' & '))
    #for x in stationNamesSplit:
    #    print x
     
    print i

  #  fig = plt.figure() # to be used to plot the figure
    
    max_ = 0 # will store max # of riders; to be used for limits on the plot
    
    # Storage containers for the data:
    xs = []
    ys = []
    
    
    
   
