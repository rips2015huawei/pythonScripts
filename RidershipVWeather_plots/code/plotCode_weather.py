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
    weather['precipm']= weather['precipm'].apply(checkInt) 


    fig = plt.figure() # to be used to plot the figure

    max_ = 0 # will store max # of riders; to be used for limits on the plot

    # Storage containers for the data:
    xs = []
    ys = []

    # Loop over months (1, 2, ... 12):
    for i in range(1, 13):

        # First find all instances that belong to the month i.
        ridMonths = pd.DataFrame(riders.loc[riders.index.month == i]);
        weatherMonths = weather.loc[weather.index.month == i]

        
        xs.append(weatherMonths['precipm']) # store the rainfall (m) for the instances 
        counts = [] # this container will be used to store the number of bikes in use for each timeframe during month i

        # Loop over all the instances of weather in the month i and determine the number of riders during the rainfall level observed.
        for x in range(0, len(weatherMonths['date'])): 
            date = weatherMonths['date'][x] # date is now a datetime object, just for less writing

            buff_less = datetime.timedelta(minutes = 15);
            buff_over = buff_less
            if x > 0:
                buff_less = date - weatherMonths['date'][x-1]
            if x < (len(weatherMonths['date'])-1): # i.e., if we're not on the last element (because we access the next element)
                buff_over = weatherMonths['date'][x+1] - date # create a buffer for the timeframe to view ridership

            # Find all bikes in use during the timeframe.
            bikesInUse = (ridMonths.loc[(ridMonths['Start date'] >= (date-buff_less)) & (ridMonths['End date'] < (date + buff_over))])
            if len(bikesInUse) > max_:
                max_ = len(bikesInUse)
            counts.append(len(bikesInUse)) # store the number of bikes in use during the timeframe
        ys.append(counts) # store the number of bikes in use for all timeframes in month i

    colors = cm.rainbow(np.linspace(0, 1, len(xs))) # vector of colors for use in scatter plot

    scatters = [] # container for the plots, so that we may associate each plot of data with its appropriate month in the plt.legend() call
    months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'] # list of months

    # Plot the data, giving each set (corresponding to each month) a different color.
    for x, y, c in zip(xs, ys, colors): # zip() puts all the data together. Nice for parallel iterations.
        scatters.append(plt.scatter(x, y, color = c))

    # Fix up the plot.
    x_max = 5
    x_min = 0.1
    y_max = 10000#max_
    y_min = 0.1

    plt.legend(scatters, months)
    plt.title("Riders vs Rain, 2012 and 2014")
    plt.ylabel("Number of Riders")
    plt.xlabel("Precipitation (m)")
    plt.xlim([x_min,x_max]) 
    plt.ylim([y_min, y_max])
    #plt.axis('tight') # This line will set the axis so that all data, and just all data, is shown. 

    # Show the plot.
    plt.show()
