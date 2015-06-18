Abbreviations:
    * df(s) = dataframe(s)

Notes on this directory:
    * handleBikeshare.py  ~  reads in the Capital Bikeshare data
        - gives two dfs: casuals    ~ df of casual riders
                         registered ~ df of registered users
    * readWeatherData.py  ~  reads in the Wunderground data
        - gives two dfs: df_weatherObserved ~ df of observed instances
                         df_weatherSummary  ~ df of daily summaries  

In ipython interactive shell:
    %run ./handleBikeshare.py
    %run ./readWeatherData.py
