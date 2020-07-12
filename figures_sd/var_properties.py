var_properties = {
  "long_name_lower":
  {"sst":"sea surface temperature","at":"air temperature","slp":"sea level pressure","wd":"wind direction","ws":"wind speed"
  ,"dpt":"dew point temperature","wbt":"wet bulb temperature"},
  "long_name_upper":
  {"sst":"Sea Surface Temperature","at":"Air Temperature","slp":"Sea Level Pressure","wd":"Wind Direction","ws":"Wind Speed"
   ,"dpt":"Dew Point Temperature","wbt":"Wet Bulb Temperature"},
   "short_name_upper":
  {"sst":"SST","at":"AT","slp":"SLP","wd":"WD","ws":"WS","dpt":"DPT","wbt":"WBT"},
  "short_name_lower":
  {"sst":"sst","at":"at","slp":"slp","wd":"wd","ws":"ws","dpt":"dpt","wbt":"wbt"},
  "color":
  {"sst":"OrangeRed","at":"DarkRed","slp":"BlueViolet","wd":"DeepSkyBlue","ws":"SteelBlue","dpt":"DarkSeaGreen","wbt":"Chartreuse"},
  "colormap":
  {"sst":"jet","at":"jet","slp":"jet","wd":"jet","ws":"jet","dpt":"jet","wbt":"jet","counts":"winter"},
  "scale":
  {"ws":1,"wd":1,"slp":0.01,"at":1,"sst":1,"dpt":1,"wbt":1},
  "offset":
  {"ws":0,"wd":0,"slp":0,"at":-273.15,"sst":-273.15,"dpt":-273.15,"wbt":-273.15},
  "units":{
    "sst":"$^\\circ$C","at":"$^\\circ$C","counts":"counts","slp":"hPa",
           "wd":"degrees","ws":"ms$^{-1}$","dpt":"$^\\circ$C","wbt":"$^\\circ$C"
  },
  "saturation":{
       "ws":[0,70],"wd":[0,370],"slp":[870,1060],"at": [-30,50],"sst":[-5,35],"dpt": [-30,50],"wbt": [-30,50]
  }
}
