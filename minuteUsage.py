import pandas as pd
import datetime
import glob 
import pygmaps
import matplotlib.pyplot as plt
import matplotlib

# Column names:
c1 = "Duration"
c2 = "Start date"
c3 = "Start Station"
c4 = "End date"
c5 = "End Station"
c6 = "Bike#"
c7 = "Subscription Type"

# Read in all csv files from current directoryy
allFiles = glob.glob("SystemData/2012/*.csv");
data = pd.DataFrame()
combinedData = []
for file_ in allFiles:
    df = pd.read_csv(file_
           ,names=[c1,c2, c3, c4, c5, c6, c7]
           ,index_col=False
           ,header = 0)
    format_ = '%m/%d/%y %H:%M'
    df[c2] = pd.to_datetime(df[c2], format = format_)
    df[c4] = pd.to_datetime(df[c4], format = format_)
    combinedData.append(df)

data = pd.concat(combinedData);
print '\nChecking data................\nPrinting head....\n'
print data.head()

casuals = pd.DataFrame(data.loc[data[c7] == 'Casual'])
registered = pd.DataFrame(data.loc[data[c7]=='Registered'])

print 'Casual Mean Duration:'
print casuals[c1].mean()
print '\nRegistered Mean Duration:'
print registered[c1].mean()



start_date = datetime.datetime(2012, 1, 1,0, 0, 0, 0)
end_date = datetime.datetime(2013,1,1,0,0,0,0)
t = datetime.timedelta(hours = 1)

date = start_date;
times =[]
times.append(start_date);
df = [0]
while date != end_date:
    date = date + t
    times.append(start_date)
    inTime = subs.loc[(subs[c2] >= start_date) & (subs[c4] < date)]
    start_date = date
    df.append(len(inTime))

smallFrame = pd.DataFrame(columns = ['date','count'])
smallFrame['date'] = times;
smallFrame['count'] = df;
smallFrame.index = smallFrame['date'];
smallFrame.drop('date', 1)
print smallFrame.head()
grouped = smallFrame.groupby(lambda x: x.month);

nrows = 6;
ncol = 2;
fig, axes = plt.subplots(nrows = nrows, ncols = ncol)

ax_row = 0;
ax_col = 0;
for name, group in grouped:
    group.plot(ax = axes[ax_row, ax_col], legend = False);
    ax_col = ax_col +1
    if ax_col >= ncol:
        ax_col = ax_col % ncol
        ax_row = ax_row + 1

plt.show()
