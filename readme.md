# Notes on pythonScripts

## Abbreviations:
    * df(s) = dataframe(s)

## (Somewhat) Useful Files in this Directory:
    * handleBikeshare.py  ~  reads in the Capital Bikeshare data
        - gives two dfs: casuals    ~ df of casual riders
                         registered ~ df of registered users
    * readWeatherData.py  ~  reads in the Wunderground data
        - gives two dfs: df_weatherObserved ~ df of observed instances
                         df_weatherSummary  ~ df of daily summaries  

## In ipython Interactive Shell:
```
    %run ./handleBikeshare.py # reads in bikeshare data
    %run ./readWeatherData.py # reads in weather data

    # Example indices:
    casuals.index = casuals['Start date'] # index by Start time
    df_weatherObserved.index = df_weatherObserved['date']
    df_weatherSummary.index = df_weatherObserved['date']
```
