import streamlit as st
import time
import random
from ds1_core import process_order, inventory, station_load

st.set_page_config(page_title="DS1 Pilot Dashboard", layout="wide")
st.title("DS1 Pilot Dashboard")
st.caption("Live kitchen intelligence powered by DS1 core engines.")

def get_live_orders(n=8):
    items = ["Brisket Sandwich", "Pulled Pork", "Mac & Cheese"]
    orders = []
    for _ in range(n):
        item = random.choice(items)
        orders.append(process_order(item))
    return orders

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
    for k, v in inventory.items():
        if v < 10:
            status = "🔴 LOW"
        elif v < 25:
            status = "🟡 WATCH"
        else:
            status = "🟢 OK"
        st.markdown(f"**{k}**: {v} units — {status}")
        st.progress(min(v / 100, 1.0))

col3, col4 = st.columns(2)
with col3:
    st.subheader("Station Load")
    total_load = sum(station_load.values()) or 1
    for station, load in station_load.items():
        pct = round((load / total_load) * 100, 1)
        st.markdown(f"**{station} Station** — {load} orders ({pct}%)")
        st.progress(min(load / total_load, 1.0))

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

st.caption(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")

