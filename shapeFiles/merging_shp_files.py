# coding: utf-8
import shapefile
import glob

# Take all .shp files from the folder 'basic_full'.
files = glob.glob("basic_full/*.shp")
files

# Open a writer module.
w = shapefile.Writer()
# Iterate over the files, extending the writer module 
# by the elements in each shapefile.
for f in files:
    r = shapefile.Reader(f)
    w._shapes.extend(r.shapes())
    w.records.extend(r.records())
    w.fields = list(r.fields)
    
# Save the writer module to a file named 'margedShp.'
w.save('mergedShp')
