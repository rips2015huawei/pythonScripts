# Import data from folder containing set of .CSV files.
import pandas as pd 
import datetime 
import glob  
 
# Column names: 
c1 = "Duration" 
c2 = "Start date" 
c3 = "Start Station" 
c4 = "End date" 
c5 = "End Station" 
c6 = "Bike#" 
c7 = "Subscription Type" 

# Read in all csv files.  
# PATH_TO_CSV should be modified. 
# *.csv pulls all cvs files in the directory PATH_TO_CSV.
allFiles = glob.glob('PATH_TO_CSV/*.csv');
data = pd.DataFrame() 
combinedData = [] 
 
# Pull the data from all the files. 
for file_ in allFiles: 
    df = pd.read_csv(file_ 
           ,names=[c1,c2, c3, c4, c5, c6, c7] 
           ,index_col=False 
           ,header = 0) 
    format_ = '%m/%d/%y %H:%M' 
    df[c2] = pd.to_datetime(df[c2], format = format_) 
    df[c4] = pd.to_datetime(df[c4], format = format_) 
    combinedData.append(df) 
 
# Combine all the data into one data frame. 
data = pd.concat(combinedData); 

# Sample output to check the data was read in correctly. 
print ' nChecking data................nPrinting head....  n' 
print data.head()

