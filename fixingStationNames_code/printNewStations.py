def printNewStations(df, col, listNames, listNew):

    for x in range(0, len(df)):
        if df[col][x] not in listNames:            
            listNew.append(df[col][x])

    for i in set(listNew):
    	print i
