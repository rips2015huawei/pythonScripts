# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
# This code was written just to check to make sure at least
# the sizes of the merged files and the combination of the 
# files individually is the same.

import shapefile

fname11 = 'cb_2013_11_bg_500k'
fname24 = 'cb_2013_24_bg_500k'
fname51 = 'cb_2013_51_bg_500k'

shp11 = open(fname11, '.shp', 'rb')
shp11 = open(fname11+ '.shp', 'rb')
shx11 = open(fname11+ '.shx', 'rb')
dbf11 = open(fname11+ '.dbf', 'rb')
shp24 = open(fname24+ '.shp', 'rb')
shx24 = open(fname24+ '.shx', 'rb')
dbf24 = open(fname24+ '.dbf', 'rb')
shp51 = open(fname51+ '.shp', 'rb')
shx51 = open(fname51+ '.shx', 'rb')
dbf51 = open(fname51+ '.dbf', 'rb')
sf11 = shapefile.Reader(shp = shp11, shx = shx11, dbf = dbf11, prj = dbf11)
sf24 = shapefile.Reader(shp = shp24, shx = shx24, dbf = dbf24, prj = dbf24)
sf51 = shapefile.Reader(shp = shp51, shx = shx51, dbf = db51, prj = dbf51)
sf51 = shapefile.Reader(shp = shp51, shx = shx51, dbf = dbf51, prj = dbf51)
shapes11 = sf11.shapes()
shapes24 = sf24.shapes()
shapes51 = sf51.shapes()
len(shapes11)
len(shapes24)
len(shapes51)
total = len(shapes11) + len(shapes24) + len(shapes51)
print total
