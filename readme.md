# Notes on pythonScripts
## Abbreviations:
* df(s) = dataframe(s)
* wrt   = with respect to

## Directories:
* RidershipVWeather\_plots
    - contains the folders code and plots, which contain the plotting code and the img files, respectively.
* SystemData
    - contains the Capital Bikeshare Data for years 2012 and 2014
* shapeFiles
    - contains the basic shapefiles from the US Census Data for the three areas of interest
        + basic_full           -- all of the .shp files together, individually
        + basic_merged         -- all of the .shp files merged into one .shp file
        + merging_shp_files.py -- python code run for merging the .shp files
* site\_shapes\_dc
    - contains the JSON data from Yelp and the Bikeshare Stations (in .txt), including shp
        + note: the 'shape' number is the index in the list of shapes for DC
        + note: need to run on the merged list of shapes to get all the sites' locations wrt shape 
* sitesJson
    - JSON data from Yelp and for the Bike Stations (in .JSON)
* xml\_files
    - contains:
        + Capital Bikeshare station info in xml
        + read\_bikeshare\_xml.py -- python script run to read in xml data with python

## (Somewhat) Useful Files:
* handleBikeshare.py  
    - reads in the Capital Bikeshare data
    - instantiates and fills two dataframes
          + casuals    ~ df of casual riders
          + registered ~ df of registered users
* readWeatherData.py 
    - reads in the Wunderground data
    - instantiates and populates two dfs:
          + df\_weatherObserved ~ df of observed instances
          + df\_weatherSummary  ~ df of daily summaries  
* RidershipVWeather\_plots/code/plotCode.py
    - Defines the function   plotObserved(df1, df2)
        + PARAMETERS:
            - df1: dataframe ASSUMED to be of same type as casuals OR registered from handleBikeshare
            - df2: dataframe ASSUMED to be of same type as df\_weatherObserved or df\_weatherSummary
        + PURPOSE:
            - To output a plot of Ridership versus Rain (m).
        + NOTES:
            - Honestly just coded this up so I could mess around in the interactive shell. I put it up so one can see some plotting code. 

## In ipython Interactive Shell:
```
    %run ./handleBikeshare.py # reads in bikeshare data
    %run ./readWeatherData.py # reads in weather data

    # Example indices:
    casuals.index = casuals['Start date'] # index by Start time
    df_weatherObserved.index = df_weatherObserved['date']
    df_weatherSummary.index = df_weatherObserved['date']

    plotObserved(casuals, df_weatherObserved)
```
