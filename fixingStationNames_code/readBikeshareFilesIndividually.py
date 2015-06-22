import pandas as pd



c1 = "Duration"; c2 = "Start date"; c3 = "Start Station"; c4 = "End date"; c5 = "End Station"; c6 = "Bike#"; c7 =  "Subscription Type"

df_2012q1 = pd.read_csv("../SystemData/2012Q1.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)

df_2012q2 = pd.read_csv("../SystemData/2012Q2.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)

df_2012q3 = pd.read_csv("../SystemData/2012Q3.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)

df_2012q4 = pd.read_csv("../SystemData/2012Q4.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)

df_2014q4 = pd.read_csv("../SystemData/2014Q4.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)

df_2014q3 = pd.read_csv("../SystemData/2014Q3.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)

df_2014q2 = pd.read_csv("../SystemData/2014Q2.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)

df_2014q1 = pd.read_csv("../SystemData/2014Q1.csv", 
names = [c1, c2, c3, c4, c5, c6, c7],
index_col = False,
header = 0)


