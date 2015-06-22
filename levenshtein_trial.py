import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import gridspec
import datetime
import Levenshtein


# FUNCTION: checkInit
# PARAMETERS: str i
# RETURNS: float object
# PURPOSE: to change object type from str or (value) 'None' to a float.



# FUNCTION: plotObserved
# PARAMETERS:
#    * riders  -- dataframe assumed to be of riders
#    >>deleting>>* listOfStations
# RETURNS: nothing
# PURPOSE: to output a plot of ridership versus rainfall.
#
# MISC: This method can clearly be improved. For one, can look up
#       axes and subplots to see how to put them together on one
#       figure. I just wanted a quick plot.
#       Secondly, the function itself can be made more generic. It's
#       clearly targeted for specific input. Again, just wanted to work
#       in ipython quickly.
def plotStations(riders)#, listOfStations):


fig = plt.figure() # to be used to plot the figure
    
    max_ = 0 # will store max # of riders; to be used for limits on the plot
    
    # Storage containers for the data:
    xs = []
    ys = []
    
    
    
   