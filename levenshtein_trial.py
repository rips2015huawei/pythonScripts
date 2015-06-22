import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime
import Levenshtein
import glob
import xml.etree.ElementTree as ET

def plotStations(riders):

    stationNames      = []
    stationNamesSplit = []

    tree = ET.parse('xml_files/bikeStations.xml')
    root = tree.getroot()

    for station in root.findall('station'):
        name = station.find('name').text
        stationNames.append(name)



    for x in stationNames:
        print x
        stationNamesSplit.append(x.split(' & '))
    for x in stationNamesSplit:
        print x
     


    fig = plt.figure() # to be used to plot the figure
    
    max_ = 0 # will store max # of riders; to be used for limits on the plot
    
    # Storage containers for the data:
    xs = []
    ys = []
    
    
    
   
