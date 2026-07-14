from ds1_menu import get_menu
from ds1_utils import format_time
from ds1_time import current_timestamp
from ds1_math import risk_level
from ds1_station import calculate_station_load
from ds1_core import calculate_station_load_from_orders, inventory
import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

st.set_page_config(page_title="DS1 Pilot Dashboard", layout="wide")
st.title("DS1 Pilot Dashboard")
st.caption("Live kitchen intelligence powered by DS1 core engines.")

# ⭐ Cache definition — MUST come before use
@st.cache_data(ttl=60)
def get_live_orders(n=8):
    """Pull live orders from DS1 menu with real prep times and stations."""
    menu = get_menu()
    orders = []

    for _ in range(n):
        item = random.choice(menu)
        orders.append({
            "item": item["name"],
            "station": item["station"],
            "prep_time": item["prep_time"],
            "timestamp": current_timestamp()
        })

    return orders

# ⭐ Call cached function
orders = get_live_orders()

col1, col2 = st.columns(2)
with col1:
    st.subheader("🔥 Live Orders (Linked to Menu)")
    orders_df = pd.DataFrame(orders)
    st.table(orders_df)

with col2:
    st.subheader("Inventory Levels")
    inventory_data = []
    for k, v in inventory.items():
        if v < 10:
            status = "🔴 LOW"
        elif v < 25:
            status = "🟡 WATCH"
        else:
            status = "🟢 OK"
        inventory_data.append({"Item": k, "Units": v, "Status": status})
    st.table(pd.DataFrame(inventory_data))

col3, col4 = st.columns(2)
with col3:
    st.subheader("📊 Station Load (Based on Menu + Orders)")
    station_load_data = calculate_station_load_from_orders(orders)
    station_data = [
        {"Station": station, "Total Prep Time": load} 
        for station, load in station_load_data.items()
    ]
    st.table(pd.DataFrame(station_data))

with col4:
    st.subheader("Kitchen Status")
    total_orders = len(orders)
    total_prep_time = sum(o["prep_time"] for o in orders)
    avg_prep_time = total_prep_time / total_orders if total_orders > 0 else 0
    
    st.metric("Total Active Orders", total_orders)
    st.metric("Combined Prep Time", f"{total_prep_time} min")
    st.metric("Average Prep Time", f"{avg_prep_time:.1f} min")

# ⭐ Optional: Add a manual refresh button
if st.button("🔄 Refresh Live Orders"):
    st.cache_data.clear()
    st.rerun()

st.divider()
st.subheader("🧪 DS1 Module Test")

test_data = {
    "Timestamp": current_timestamp(),
    "Formatted Time": format_time(8),
    "Risk Level (variance 4)": risk_level(4),
}

col_test1, col_test2 = st.columns(2)
with col_test1:
    st.write("**Module Outputs:**")
    for key, value in test_data.items():
        st.markdown(f"- **{key}:** {value}")

with col_test2:
    st.write("**Station Load Percentages:**")
    station_pct = calculate_station_load({"Cutting": 5, "Assembly": 3, "Sides": 2})
    pct_data = [{"Station": k, "Load %": v} for k, v in station_pct.items()]
    st.table(pd.DataFrame(pct_data))

st.divider()
st.subheader("📋 DS1 Menu Reference")
menu = get_menu()
st.table(pd.DataFrame(menu))
