# This is a temp python file to play with things before they go to a category
# John wood
# Aug 31, 2020

#just pulling in my weather 
# Web Services

#this takes a minute for it to pull down everything but lots that can be done
from noaa_sdk import noaa # pip install noaa-sdk  
n = noaa.NOAA()
res = n.get_forecasts('14810', 'US', True)
for i in res:
    print(i)