


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn import decomposition
from scipy import stats
from sklearn import cluster
from vincenty import vincenty
from h3 import h3
from folium import Map, Marker, GeoJson
from folium.plugins import MarkerCluster
import folium
import branca.colormap as cm
from geojson.feature import *
import json
from IPython.display import Image, display
import calendar
from tqdm import tqdm
from datetime import datetime
import seaborn as sns





import yaml
import requests
url='https://raw.githubusercontent.com/sekhongurkirat/SpatioTemporal-Influx-Detection-Spa.T.I.D-/main/spatid.yml'
download = requests.get(url).content

try:
    with open ('download', 'r') as file:
        config = yaml.safe_load(file)
except Exception as e:
    print('Error reading the config file')





path=config['file_path']
complaint_time=config['complaint_time']
complaint_date=config['complaint_date']


df = pd.read_csv(path)





def spatid(df,time_bin,spatial_resolution):
    df.dropna()
    
    #generating hexid for locations from latitude and Longitude data columns
    df["hex_id"] = df.apply(lambda row: h3.geo_to_h3(row["Latitude"], row["Longitude"], spatial_resolution), axis = 1)
    
    # converting time into number of minutes in the day
    df['time'] = df[complaint_time].apply(lambda x:datetime.strptime(x,'%H:%M:%S'))
    dfhour=df['time'].apply(lambda x:x.hour)*60
    dfmin=df['time'].apply(lambda x:x.minute)
    df['time']=dfhour+dfmin
    df['time']=df['time'].astype(int)
    
    #creating time bins in a day based on 'time_bin' parameter
    df['bin']=df['time']/time_bin+1
    df['bin']=df['bin'].astype(int)
    
    #grouping data based on day, time and location
    srs1=df.groupby([complaint_date, 'hex_id','bin']).size().sort_values(ascending=False) 
    
    df_output=srs1.to_frame()
    df_output.reset_index(inplace=True)  
    df_output.rename({0: 'Incident_count'}, axis=1, inplace=True)
    
    #creating threshold for alarm where incident report increases beyond 95th percentile (2 std deviations) of the reports
    # in the given location within the time bin
    srs2=df_output.groupby('hex_id')['Incident_count'].quantile(.95).sort_values(ascending=False)
    df_threshold=srs2.to_frame()
    df_threshold=df_threshold.rename(columns={'Incident_count':'Threshold'})
    df_threshold.reset_index(inplace=True)
    
    #joining the threshold df with output df
    df_joined=pd.merge(df_output,df_threshold,how='left',on=['hex_id','hex_id'])
    
    #generating alarm based on threshold
    df_alarm=df_joined[df_joined['Incident_count']>=df_joined['Threshold']]
    
    return df_alarm,df_output





df_test,df1=spatid(df,60,7)


df_test['Incident_count'].sum()

df_test.tail(10)




