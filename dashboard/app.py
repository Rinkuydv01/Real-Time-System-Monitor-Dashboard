import streamlit as st
import requests
from datetime import datetime

st.set_page_config(layout="wide", page_title="Real-Time System Monitor")
st.title("Real-Time System Resource Monitor")

API_URL = st.sidebar.text_input("API URL", "http://127.0.0.1:5000/api/latest")

def fetch_data():
    try:
        res = requests.get(API_URL)
        data = res.json()
        if "msg" in data:
            return None
        data['ts'] = datetime.fromtimestamp(data['ts'])
        return data
    except:
        return None

placeholder = st.empty()
while True:
    metric = fetch_data()
    if metric:
        placeholder.metric("CPU %", f"{metric['cpu']:.1f}")
        placeholder.metric("Memory %", f"{metric['memory']:.1f}")
        placeholder.metric("Disk %", f"{metric['disk']:.1f}")
    st.experimental_rerun()
