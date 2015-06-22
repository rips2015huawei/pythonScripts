import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.font_manager import FontProperties


# FUNCTION: plotRidership_month
# PARAMETERS: 
#    * riders  -- dataframe assumed to be of riders
# RETURNS: nothing
# PURPOSE: to output a plot of ridership over the months in a year.#
def plotRidership_monthYear(riders):#, listOfStations):
    fig = plt.figure() # to be used to plot the figure

    max_ = 0 # will store max # of riders; to be used for limits on the plot

    # Storage containers for the data:
    xs = []
    ys_2012 = []
    ys_2014 = []
    

    # Loop over months (1, 2, ... 12):
    for i in range(1, 13):

        # First find all instances that belong to the month i.
        ridMonths_2012 = pd.DataFrame(riders.loc[(riders.index.year == 2012) & (riders.index.month == i)]);
        ridMonths_2014 = pd.DataFrame(riders.loc[(riders.index.year == 2014) & (riders.index.month == i)]);

        xs.append(i) # store the rainfall (m) for the instances
        ys_2012.append(len(ridMonths_2012))
        ys_2014.append(len(ridMonths_2014))
 
    colors = cm.rainbow(np.linspace(0, 1, len(xs))) # vector of colors for use in scatter plot

    #scatters = [] # container for the plots, so that we may associate each plot of data with its appropriate month in the plt.legend() call
    months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'] # list of months

    ax = fig.add_subplot(111)

    # Plot the data, giving each set (corresponding to each month) a different color.
    #for x, y, c in zip(xs, ys, colors): # zip() puts all the data together. Nice for parallel iterations.
    ax.plot(xs, ys_2012, 'k-',xs, ys_2014, 'b' )


    
    #fontP = FontProperties()
    #fontP.set_size('small')
    ax.legend( ['2012', '2014'], loc = 1, fancybox = True)

    ax.set_title("Riders by Month, 2012 and 2014")
    ax.set_ylabel("Number of Riders")
    ax.set_xlabel("Month")
    plt.xticks(xs, months)
    #ax.legend(loc='upper center', fancybox = True)
#plt.xlim([x_min,x_max])
#plt.ylim([y_min, y_max])
    #plt.axis('tight') # This line will set the axis so that all data, and just all data, is shown.

    # Show the plot.
    plt.show()
