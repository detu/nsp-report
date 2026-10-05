import streamlit as st
import pandas as pd
import numpy as np
import base64


@st.cache_data
def load_data():
    return pd.read_csv("28.09.2026/recording28092026.csv")

# Get camera 1 image
@st.cache_data
def camera1_image(row):
    image_path = '28.09.2026/{0}_{1}/{0}_{1}-1.jpg'.format(row['BarcodeID'], row['Datetime'])
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpg;base64,{encoded_string}"
    except FileNotFoundError:
        return ""

# Get camera 2 image
@st.cache_data
def camera2_image(row):
    image_path = '28.09.2026/{0}_{1}/{0}_{1}-2.jpg'.format(row['BarcodeID'], row['Datetime'])
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpg;base64,{encoded_string}"
    except FileNotFoundError:
        return ""        

# Get camera 3 image
@st.cache_data
def camera3_image(row):
    image_path = '28.09.2026/{0}_{1}/{0}_{1}-3.jpg'.format(row['BarcodeID'], row['Datetime'])
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpg;base64,{encoded_string}"
    except FileNotFoundError:
        return ""        

# Get camera 4 image
@st.cache_data
def camera4_image(row):
    image_path = '28.09.2026/{0}_{1}/{0}_{1}-4.jpg'.format(row['BarcodeID'], row['Datetime'])
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpg;base64,{encoded_string}"
    except FileNotFoundError:
        return ""        


st.set_page_config(
    page_title="NSP Report")

st.title("NSP Report")
st.header("Date: 28.09.2026")
df = load_data()


df["Camera-1"] = df[['BarcodeID', 'Datetime']].apply(camera1_image, axis=1)
df["Camera-2"] = df[['BarcodeID', 'Datetime']].apply(camera2_image, axis=1)
df["Camera-3"] = df[['BarcodeID', 'Datetime']].apply(camera3_image, axis=1)
df["Camera-4"] = df[['BarcodeID', 'Datetime']].apply(camera4_image, axis=1)


rows_per_page = 10
total_pages   = (len(df) + rows_per_page - 1) // rows_per_page

dataframe_slot = st.empty()
with st.container(horizontal_alignment="right"):
    page = st.pagination(num_pages=total_pages)

start_idx = (page - 1) * rows_per_page
end_idx   = start_idx + rows_per_page

# Display inside st.dataframe using ImageColumn configuration
dataframe_slot.dataframe(
        df.iloc[start_idx:end_idx],
    column_config={
        "Camera-1": st.column_config.ImageColumn(
            "Camera-1", width=800
        ),
        "Camera-2": st.column_config.ImageColumn(
            "Camera-2", width=800
        ),
        "Camera-3": st.column_config.ImageColumn(
            "Camera-3", width=800
        ),
        "Camera-4": st.column_config.ImageColumn(
            "Camera-4", width=800
        ),

    },
    hide_index=False
)



