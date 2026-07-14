import streamlit as st

try:
    from streamlit_autorefresh import st_autorefresh
except ImportError:  # pragma: no cover - fallback for minimal environments
    def st_autorefresh(*args, **kwargs):
        return None

# Refresh every 5 seconds
st_autorefresh(interval=5000, key="ds1_refresh")

from ds1_menu import get_menu
from ds1_risk import assess_station_risk
from ds1_station import calculate_station_load
from ds1_time import current_timestamp


def main():
    st.set_page_config(page_title="DS1 Sandbox Dashboard", layout="wide")
    st.title("DS1 Sandbox Dashboard")

    st.subheader("🔥 Live Orders (Linked to Menu)")
    menu = get_menu()

    def get_live_orders():
        return [
            {
                "item": menu[0]["name"],
                "station": menu[0]["station"],
                "prep_time": 12,
                "timestamp": current_timestamp(),
            },
            {
                "item": menu[0]["name"],
                "station": menu[0]["station"],
                "prep_time": 12,
                "timestamp": current_timestamp(),
            },
            {
                "item": menu[1]["name"],
                "station": menu[1]["station"],
                "prep_time": 10,
                "timestamp": current_timestamp(),
            },
            {
                "item": menu[2]["name"],
                "station": menu[2]["station"],
                "prep_time": 25,
                "timestamp": current_timestamp(),
            },
        ]

    orders = get_live_orders()
    st.write(orders)

    st.subheader("📊 Station Load")
    station_load = calculate_station_load(orders)
    st.write(station_load)

    st.subheader("⚠️ DS1 Risk Engine")
    risk = assess_station_risk(station_load)

    risk_colors = {
        "LOW": "#2ecc71",
        "MEDIUM": "#f1c40f",
        "HIGH": "#e74c3c",
    }

    st.markdown(
        "<div style='background-color:#555;padding:8px;border-radius:6px;margin-bottom:10px'>"
        "<span style='color:yellow;font-size:20px'>⚠️</span>"
        "<span style='color:white;font-size:20px;font-weight:bold'> DS1 Risk Engine</span>"
        "</div>",
        unsafe_allow_html=True,
    )

    for station, level in risk.items():
        color = risk_colors[level]
        st.markdown(
            f"""
            <div style='background-color:{color};padding:10px;border-radius:8px;margin-bottom:8px'>
                <strong style='color:white;font-size:16px'>{station}</strong>
                <span style='float:right;color:white;font-weight:bold'>{level}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
