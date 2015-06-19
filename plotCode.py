import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import gridspec
import datetime

# FUNCTION: checkInit
# PARAMETERS: str i
# RETURNS: float object
# PURPOSE: to change object type from str or (value) 'None' to a float.
def checkInt(i):
    if (i == None):
        return 0
    elif i < 0:
        return 0
    else:
        return float(i)


# FUNCTION: plotObserved
# PARAMETERS: 
#    * riders  -- dataframe assumed to be of riders
#    * weather -- dataframe assumed to be of weather
# RETURNS: nothing
# PURPOSE: to output a plot of ridership versus rainfall.
#
# MISC: This method can clearly be improved. For one, can look up
#       axes and subplots to see how to put them together on one
#       figure. I just wanted a quick plot.
#       Secondly, the function itself can be made more generic. It's
#       clearly targeted for specific input. Again, just wanted to work
#       in ipython quickly.
def plotObserved(riders, weather):

    # First, convert the values stored from the JSON into float objects.
    df_weatherObserved['precipm']=df_weatherObserved['precipm'].apply(checkInt) 


    fig = plt.figure() # to be used to plot the figure

    max_ = 0 # will store max # of riders; to be used for limits on the plot

    # Storage containers for the data:
    xs = []
    ys = []

    # Loop over months (1, 2, ... 12):
    for i in range(1, 13):

        # First find all instances that belong to the month i.
        casMonths = pd.DataFrame(casuals.loc[casuals.index.month == i]);
        weatherMonths = df_weatherObserved.loc[df_weatherObserved.index.month == i]

        
        xs.append(weatherMonths['precipm']) # store the rainfall (m) for the instances 
        counts = [] # this container will be used to store the number of bikes in use for each timeframe during month i

        # Loop over all the instances of weather in the month i and determine the number of riders during the rainfall level observed.
        for x in range(0, len(weatherMonths['date'])): 
            date = weatherMonths['date'][x] # date is now a datetime object, just for less writing
            if x < (len(weatherMonths['date'])-1): # i.e., if we're not on the last element (because we access the next element)
                buff = weatherMonths['date'][x+1] - date # create a buffer for the timeframe to view ridership

            # Find all bikes in use during the timeframe.
            bikesInUse = (casMonths.loc[(casMonths['Start date'] >= (date-buff)) & (casMonths['End date'] < (date + buff))])
            if len(bikesInUse) > max_:
                max_ = len(bikesInUse)
            counts.append(len(bikesInUse)) # store the number of bikes in use during the timeframe
        ys.append(counts) # store the number of bikes in use for all timeframes in month i

    colors = cm.rainbow(np.linspace(0, 1, len(xs))) # vector of colors for use in scatter plot

    scatters = [] # container for the plots, so that we may associate each plot of data with its appropriate month in the plt.legend() call
    months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'] # list of months

    # Plot the data, giving each set (corresponding to each month) a different color.
    for x, y, c in zip(xs, ys, colors):
        scatters.append(plt.scatter(x, y, color = c))

    # Fix up the plot.
    plt.legend(scatters, months)
    plt.title("Riders vs Rain, 2012 and 2014")
    plt.ylabel("Number of Riders")
    plt.xlabel("Precipitation (m)")
    plt.xlim([-0.1,2]) 
    plt.ylim([-1, max_])
    # plt.axis('tight') # This line will set the axis so that all data, and just all data, is shown. 

    # Show the plot.
    plt.show()
