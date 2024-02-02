import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from folium import Marker
from streamlit_folium import st_folium
import branca.colormap as cm

# %% [code] {"execution":{"iopub.status.busy":"2024-02-02T06:21:43.962801Z","iopub.execute_input":"2024-02-02T06:21:43.963221Z","iopub.status.idle":"2024-02-02T06:21:43.978418Z","shell.execute_reply.started":"2024-02-02T06:21:43.963190Z","shell.execute_reply":"2024-02-02T06:21:43.977385Z"}}
df_def = pd.read_csv('/kaggle/input/auberges-map/auberges_app.csv')

# %% [code] {"execution":{"iopub.status.busy":"2024-02-02T06:21:47.642290Z","iopub.execute_input":"2024-02-02T06:21:47.642685Z","iopub.status.idle":"2024-02-02T06:21:47.654360Z","shell.execute_reply.started":"2024-02-02T06:21:47.642654Z","shell.execute_reply":"2024-02-02T06:21:47.653209Z"}}
linear = cm.LinearColormap(["red", "orange", "yellow", "green"], 
                           vmin=df_def['Score'].min(), 
                           vmax=df_def['Score'].max(),
                           index=[0, 100, 350, 1000])

# %% [code] {"execution":{"iopub.status.busy":"2024-02-02T06:21:48.058898Z","iopub.execute_input":"2024-02-02T06:21:48.059374Z","iopub.status.idle":"2024-02-02T06:21:48.158593Z","shell.execute_reply.started":"2024-02-02T06:21:48.059318Z","shell.execute_reply":"2024-02-02T06:21:48.157678Z"}}
m = folium.Map(location=[40.547722,-5.155226], tiles='openstreetmap', zoom_start=6)
for idx, row in df_def.iterrows():
    folium.CircleMarker([row['Latitude'], 
            row['Longitude']], 
           popup=[str('Ville : ') + row['Ville'],
                  str('Score : ') + str(row['Score']), 
                  str('Requetes : ') + str(row['Nombre de requetes mensuelles totales']),
                  str('Nb Hotel : ') + str(row['Nombre etablissement booking'])],
           radius=5,
           fill=True,
           fill_opacity=0.8,
           color = linear(row.Score),).add_to(m)

# %% [code] {"execution":{"iopub.status.busy":"2024-02-02T06:22:34.866413Z","iopub.execute_input":"2024-02-02T06:22:34.866874Z","iopub.status.idle":"2024-02-02T06:22:34.904423Z","shell.execute_reply.started":"2024-02-02T06:22:34.866823Z","shell.execute_reply":"2024-02-02T06:22:34.903136Z"}}
st_data = st_folium(m)
