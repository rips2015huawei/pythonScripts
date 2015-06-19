import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import gridspec
import datetime


def checkInt(i):
    if (i == None):
        return 0
    elif i < 0:
        return 0
    else:
        return float(i)

def plotObserved(casuals, df_weatherObserved):
    nrows = 6
    ncol = 2

    ax_row = 0
    ax_col = 0

    #df_weatherObserved['precipm'] = df_weatherObserved['precipm'].apply(lambda x: float(x))
    df_weatherObserved['precipm']=df_weatherObserved['precipm'].apply(checkInt) 

    min_h = df_weatherObserved['date'][0] - df_weatherObserved['date'][1]
    for x in range(2, len(df_weatherObserved)):
        if df_weatherObserved['date'][x] - df_weatherObserved['date'][x-1] < min_h:
            min_h = df_weatherObserved['date'][x] - df_weatherObserved['date'][x-1]

    #if min_h < datetime.timedelta(minutes = 1):

    max_ = 0;
    fig = plt.figure()
    xs = []
    ys = []
    pairs = []

    for i in range(1, 13):
        #axes = fig.add_subplot(gs[ax_row, ax_col])
        casMonths = pd.DataFrame(casuals.loc[casuals.index.month == i]);
        weatherMonths = df_weatherObserved.loc[df_weatherObserved.index.month == i]
        counts = []
        xs.append(weatherMonths['precipm'])
        for x in range(0, len(weatherMonths['date'])): 
            date = weatherMonths['date'][x]  
            if x < (len(weatherMonths['date'])-1):
                buff = weatherMonths['date'][x+1] - weatherMonths['date'][x]
            bikesInUse = (casMonths.loc[(casMonths['Start date'] >= (date-buff)) & (casMonths['End date'] < (date + buff))])
            if len(bikesInUse) > max_:
                max_ = len(bikesInUse)
            #print len(bikesInUse)
            counts.append(len(bikesInUse))
        #weatherMonths['riders'] = counts;
        ys.append(counts)
        pairs.append([weatherMonths['precipm'], counts])
        ax_col = ax_col +1
        if ax_col >= ncol:
           ax_col = ax_col % ncol
           ax_row = ax_row + 1

    #plt.scatter(xs[0], ys[0], 'k', xs[1], ys[1], 'k-', xs[2], ys[2], 'r', xs[3], ys[3], 'b--', xs[4], ys[4],'b', xs[5], ys[5],'g-' ,xs[6], ys[6], 'c',xs[7], ys[7], 'k', xs[8], ys[8], 'c-', xs[9], ys[9],'b', xs[10], ys[10], 'g-', xs[11], ys[11], 'm') 
    colors = cm.rainbow(np.linspace(0, 1, len(xs))) 
    scatters = [];
    months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    for x, y, c in zip(xs, ys, colors):
        scatters.append(plt.scatter(x, y, color = c))
    plt.legend(scatters, months)
    plt.title("Riders vs Rain, 2012 and 2014")
    plt.ylabel("Number of Riders")
    plt.xlabel("Precipitation (m)")
    plt.xlim([-0.1,2]) 
    #plt.xticks(np.linspace(0.1, 2.0,num= 31))
    plt.ylim([-1, max_])
    # >> Shows all data >>  #plt.axis('tight')
    plt.show()

    print len(xs), len(ys)
