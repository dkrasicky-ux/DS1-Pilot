import streamlit as st

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
    st.write(risk)


if __name__ == "__main__":
    main()
