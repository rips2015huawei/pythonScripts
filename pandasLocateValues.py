import pandas as pd
 
# FUNCTION: groupData() 
# PARAMETERS: 
#    -  df  ~ DataFrame 
#    -  columnNames ~ array of column names to be grouped by 
#    -  dataChecks     ~ values to sift through column for 
def groupData(df, columnNames, dataChecks) 
    subset = df.copy() 
    range_ = len(columnNames) 
    if range ~= len(dataChecks):  
        print  '\nWarning! Lists of column names and values not same size!'
    for x in range(0, range_) 
        subset = subset.loc[subset[columnNames[x] == dataChecks[x]]] 
    print  '\nChecking data....Printing sample....'
    print subset.head()

    print  '\nYou can use the groupby function to group the selected data further.'
    print ' For example grouped = data.groupby(lambda x: x.month), where x is the index'
 
    return subset