# pip install pysph, matplotlib, numpy, etc
import shapefile
import numpy as np
from matplotlib.path import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fname = 'cb_2013_11_bg_500k'

shp = open(fname + '.shp', 'rb')
shx = open(fname + '.shx', 'rb')
dbf = open(fname + '.dbf', 'rb')
prj = open(fname + '.prj', 'rb')

sf = shapefile.Reader(shp=shp, shx=shx, dbf=dbf, prj=prj)

len(sf.shapes())
shapes = sf.shapes()
shapes[0]
# <shapefile._Shape instance at 0x103f09b00>
dir(shapes[0])
# ['__doc__',
#  '__geo_interface__',
#  '__init__',
#  '__module__',
#  'bbox',
#  'parts',
#  'points',
#  'shapeType']

shapes[0].points
# comes in [lon, lat] format
fields = sf.fields
records = sf.records()
# contains the record information, most importantly 

shaperecs = sf.shapeRecords()
dir(shaperecs[0])
# ['__doc__', '__init__', '__module__', 'record', 'shape']

sf.shapeRecord(3)  # the fourth record, for easy access without forming a list
# mostly useful for larger

# check if a point is inside a polygon - this is close enough, we don't really
# need projections for something this small-scale
poly = Path(shapes[0].points)
test_point = [-77.0241, 38.976]
poly.contains_point(test_point)

fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(poly, facecolor='orange', lw=2)
ax.add_patch(patch)
ax.set_xlim(-77.015,-77.028)
ax.set_ylim(38.97,38.98)
plt.show()


# RUN AT THE END, WE NEED THE FILES OPEN TO DO ANY ACCESS WORK

shp.close()
shx.close()
dbf.close()
prj.close()

# now, the TIGER files - much more detailed. probably don't need these

fname = 'tl_2014_11_bg'

shp = open(fname + '.shp', 'rb')
shx = open(fname + '.shx', 'rb')
dbf = open(fname + '.dbf', 'rb')
prj = open(fname + '.dbf', 'rb')

sf = shapefile.Reader(shp=shp, shx=shx, dbf=dbf, prj=prj)

# AGAIN, RUN AT THE END

shp.close()
shx.close()
dbf.close()
prj.close()

