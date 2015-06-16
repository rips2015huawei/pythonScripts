import pandas as pd
import glob 
import pygmaps
import numpy
from bs4 import BeautifulSoup
import lxml.etree as et
import xml.etree.ElementTree as ET

bikeStations_url = "https://www.capitalbikeshare.com/data/stations/bikeStations.xml"

tree = ET.parse('bikeStations.xml') 
root = tree.getroot();
#print root[0][1].text
pos = []

for station in root.findall('station'):
    lat = float(station.find('lat').text)
    long_ = float(station.find('long').text)
    name = station.find('name').text
    pos.append([lat, long_, name]);
    
mymap = pygmaps.maps(38.9047, -77.0164, 14)

for p in pos:
    print p
    mymap.addpoint(p[0], p[1], '#0000FF', p[2])

mymap.draw('mymap.html')
