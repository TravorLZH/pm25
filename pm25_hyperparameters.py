# For partitioning the dataset
train_test_boundary="2015-10-01 00:00:00"

# For lagged features
lag_hours=48

# For statistics over rolling window
stat_wnd=lag_hours

# For PM2.5's frequency domain
stft_period=24*7*4
stft_upper=0.2

# Primitive features used for feature engineering
prim_fea=[
    "TEMP",# Temperature
    "DEWP",# Dew point
    "HUMI",# Humidity
    "PRES",# Air pressure
    "precipitation",# Precipitation (as the name suggests)
    "Iws",# Wind speed
    "PM"# PM2.5 concentration
]
