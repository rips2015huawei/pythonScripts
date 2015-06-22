# coding: utf-8
for i in range(1, 13):
    casMonths = casuals.loc[casuals.index.month == i]
    weatherMonths = pd.DataFrame(df_weatherObserved.loc[df_weatherObserved.index.month == i])
    counts = []
    for dates in weatherMonths['date']:
        bikesInUse = casMonths.loc[(casMonths['Start date'] > (dates - buff)) & (casMonths['End date'] < (dates + buff))]
        count = len(bikesInUse)
        counts.append(count)
    weatherMonths['riders'] = counts
    weatherMonths.plot(x='date', y='riders', axes = [ax_row, ax_col], legend = False)
    ax_col = ax_col + 1
    if ax_col >= ncol:
        ax_col = ax_col %ncol
        ax_row = ax_row+1
        
