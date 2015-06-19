# Notes on pythonScripts

## Abbreviations:
* df(s) = dataframe(s)

## (Somewhat) Useful Files in this Directory:
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
* plotCode.py
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
