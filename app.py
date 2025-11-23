#libraries

import requests
import streamlit as st
import numpy as np
import pandas as pd

import plotly.express as px





#data and files
df= pd.read_csv('india.csv')
list_of_state= list(df['State'].unique())
list_of_state[0]='Overall India'

#page
st.set_page_config(layout="wide")

st.title('This is My project')
st.sidebar.title("India's visuals")
selected_item= st.sidebar.selectbox('Select State',list_of_state)


primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary= st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))
btn1= st.sidebar.button('Search')
if btn1:
    if selected_item== 'Overall India':
        import plotly.express as px

        # Create the map
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            zoom=3.5,
            hover_name="District",
            hover_data=["State", "literacy_rate", "Muslim_rate"],
            size_max=30,
            mapbox_style="carto-positron",
            height=700,
            title="District-wise Demographics (Size=Pop, Color=Sex Ratio)"
        )



        st.plotly_chart(fig,use_container_width=True)
    else:

        state_df= df[df['State'] == selected_item]
        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            zoom=5.5,
            color_continuous_scale=px.colors.diverging.Spectral,
            hover_name="District",
            hover_data=["State", "literacy_rate", "Muslim_rate"],
            #size_max=30,
            mapbox_style="carto-positron",
            height=700,
            title="District-wise Demographics (Size=Pop, Color=Sex Ratio)"
        )

        st.plotly_chart(fig,use_container_width=True)



