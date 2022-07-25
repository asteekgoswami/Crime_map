import pandas as pd
import folium
from folium import plugins

df=pd.read_csv(r'Project\Book1.csv')

stationArr=df[['Y','X']].values

m=folium.Map(location=[stationArr[0][0],stationArr[0][1]],zoom_start=15)
m.add_child(plugins.HeatMap(stationArr[:50000],radius=15))
m.save('crimemap.html')