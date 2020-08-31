# John wood
# Aug 31, 2020

# just pulling in my weather returning the date, time, temp, wind, wind direction
# and forecast # need to find the % for the forecast 
# Web Services

# this takes a minute for it to pull down everything but lots that can be done
# if you want you can replace the print with the print(i) and everything that is in
# the API will be shown
import re
from noaa_sdk import noaa # pip install noaa-sdk  
n = noaa.NOAA()
res = n.get_forecasts('14810', 'US', True)
for i in res:
    print(re.findall('([0-9]?[0-9]-[0-9]?[0-9])T([0-2]?[0-9]:[0-5]?[0-9])', i['startTime']), 
    'Temp', i['temperature'], 'Wind', i['windSpeed'], 'Direction', i['windDirection'], 
    'Forecast', i['shortForecast']) # I did a regex on the start time otherwise it looks like this
                                    # for the time 2020-09-07T03:00:00-04:00 this way it shows
                                    # the date and time 08-31 17:00 easier for me to look at
    #print(i)