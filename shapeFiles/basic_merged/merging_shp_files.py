# coding: utf-8
files = glob.glob("basic_full/*.shp")
files
w = shapefile.Writer()
for f in files:
    r = shapefile.Reader(f)
    w._shapes.extend(r.shapes())
    w.records.extend(r.records())
    w.fields = list(r.fields)
    
w.save('mergedShp')
