from ds1_menu import get_menu
from ds1_utils import format_time
from ds1_time import current_timestamp
from ds1_math import risk_level
from ds1_station import calculate_station_load
import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime
from ds1_core import process_order, inventory, station_load

st.set_page_config(page_title="DS1 Pilot Dashboard", layout="wide")
st.title("DS1 Pilot Dashboard")
st.caption("Live kitchen intelligence powered by DS1 core engines.")

# ⭐ Cache definition — MUST come before use
@st.cache_data(ttl=60)
def get_live_orders(n=8):
    items = ["Brisket Sandwich", "Pulled Pork", "Mac & Cheese"]
    orders = []
    for _ in range(n):
        item = random.choice(items)
        orders.append(process_order(item))
    return orders

# ⭐ Call cached function
orders = get_live_orders()
failures = [o for o in orders if o["failure"]]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Live Prep Status")
    for o in orders:
        risk_color = "🔴" if o["failure"] else "🟢"
        st.markdown(
            f"**{o['item']}** | Station: `{o['station']}` {risk_color}\n"
            f"- Expected: **{o['prep_time']} min**\n"
            f"- Actual: **{o['adjusted_time']} min**\n"
            f"- Variance: **{o['variance']} min**"
        )
        st.divider()

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
    st.subheader("Station Load")
    station_data = []
    total_load = sum(station_load.values()) or 1
    for station, load in station_load.items():
        pct = round((load / total_load) * 100, 1)
        station_data.append({"Station": station, "Orders": load, "Load %": pct})
    st.table(pd.DataFrame(station_data))

with col4:
    st.subheader("Failure-Point Alerts")
    if not failures:
        st.success("No active failure points. Kitchen flow is stable. 🟢")
    else:
        for f in failures:
            st.error(
                f"{f['item']} at `{f['station']}` — "
                f"Expected {f['prep_time']} min, Actual {f['adjusted_time']} min "
                f"(+{f['variance']} min)"
            )

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
st.subheader("📋 DS1 Menu Simulation")
menu = get_menu()
st.table(pd.DataFrame(menu))
