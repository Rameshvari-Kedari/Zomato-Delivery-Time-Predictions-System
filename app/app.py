import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Zomato Delivery Time Prediction",
    page_icon="🚴",
    layout="wide"
)


# ============================================================
# MODEL PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "final_model.pkl"


@st.cache_resource
def load_model():

    return joblib.load(MODEL_PATH)


model = load_model()


# ============================================================
# HEADER
# ============================================================

st.title("🚴 Zomato Delivery Time Prediction")

st.markdown(
    """
    **Predict delivery time and identify potential delivery risk
    before dispatch.**
    """
)

st.divider()


# ============================================================
# ORDER PROFILE
# ============================================================

st.subheader("📦 Order Profile")

col1, col2, col3 = st.columns(3)


with col1:

    delivery_person_age = st.number_input(
        "👤 Delivery Person Age",
        min_value=18,
        max_value=60,
        value=25,
        step=1
    )


with col2:

    delivery_person_rating = st.number_input(
        "⭐ Delivery Person Rating",
        min_value=1.0,
        max_value=5.0,
        value=4.5,
        step=0.1
    )


with col3:

    distance_km = st.number_input(
        "📏 Restaurant → Customer Distance (km)",
        min_value=0.1,
        max_value=50.0,
        value=3.0,
        step=0.1
    )


st.divider()


# ============================================================
# OPERATIONAL CONDITIONS
# ============================================================

st.subheader("🚦 Operational Conditions")

col1, col2 = st.columns(2)


with col1:

    traffic = st.selectbox(
        "🚗 Road Traffic Density",
        options=[
            "Low",
            "Medium",
            "High",
            "Jam"
        ]
    )


with col2:

    vehicle_condition = st.selectbox(
        "🔧 Vehicle Condition",
        options=[
            0,
            1,
            2
        ]
    )


col1, col2 = st.columns(2)


with col1:

    multiple_deliveries = st.selectbox(
        "📦 Multiple Deliveries",
        options=[
            0,
            1,
            2,
            3
        ]
    )


with col2:

    vehicle = st.selectbox(
        "🛵 Type of Vehicle",
        options=[
            "motorcycle",
            "scooter",
            "electric_scooter",
            "bicycle"
        ]
    )


st.divider()


# ============================================================
# EXTERNAL CONDITIONS
# ============================================================

st.subheader("🌦️ External Conditions")

col1, col2, col3 = st.columns(3)


with col1:

    weather = st.selectbox(
        "🌤️ Weather Conditions",
        options=[
            "Sunny",
            "Stormy",
            "Sandstorms",
            "Cloudy",
            "Windy",
            "Fog"
        ]
    )


with col2:

    festival = st.selectbox(
        "🎉 Festival",
        options=[
            "No",
            "Yes"
        ]
    )


with col3:

    city = st.selectbox(
        "🏙️ City",
        options=[
            "Metropolitian",
            "Urban",
            "Semi-Urban"
        ]
    )


# ============================================================
# ORDER DAY
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    order_dayofweek = st.selectbox(
        "📅 Order Day",
        options=[
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )


st.divider()


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.subheader("🎯 Delivery Prediction")

predict_button = st.button(
    "🚀 Check Delivery ETA",
    use_container_width=True
)


# ============================================================
# MODEL INPUT
# ============================================================

if predict_button:

    input_data = pd.DataFrame({

        "Delivery_person_Ratings": [
            delivery_person_rating
        ],

        "distance_km": [
            distance_km
        ],

        "Delivery_person_Age": [
            delivery_person_age
        ],

        "Road_traffic_density": [
            traffic
        ],

        "Vehicle_condition": [
            vehicle_condition
        ],

        "multiple_deliveries": [
            multiple_deliveries
        ],

        "Weather_conditions": [
            weather
        ],

        "Type_of_vehicle": [
            vehicle
        ],

        "Festival": [
            festival
        ],

        "City": [
            city
        ],

        "order_dayofweek": [
            order_dayofweek
        ]
    })


    # ========================================================
    # PREDICTION
    # ========================================================

    prediction = model.predict(input_data)[0]

    prediction = round(float(prediction), 1)


    # ========================================================
    # DELIVERY STATUS
    # ========================================================

    if prediction <= 30:

        status = "🟢 NORMAL"

        status_message = (
            "The predicted delivery time is relatively low. "
            "Normal delivery operations can be followed."
        )

    elif prediction <= 45:

        status = "🟡 MONITOR"

        status_message = (
            "The predicted delivery time is moderate. "
            "The order should be monitored for possible delay."
        )

    else:

        status = "🔴 HIGH DELAY RISK"

        status_message = (
            "The predicted delivery time is high. "
            "Consider proactive operational monitoring."
        )


    # ========================================================
    # RESULT SECTION
    # ========================================================

    st.divider()

    st.subheader("📊 Prediction Result")


    # ========================================================
    # MAIN RESULT
    # ========================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "⏱️ Predicted Delivery Time",
            f"{prediction} min"
        )


    with col2:

        st.metric(
            "📏 Delivery Distance",
            f"{distance_km:.1f} km"
        )


    with col3:

        st.metric(
            "🚦 Delivery Status",
            status
        )


    st.divider()


    # ========================================================
    # OPERATIONAL INSIGHT
    # ========================================================

    st.subheader("💡 Operational Recommendation")

    if prediction <= 30:

        st.success(status_message)

    elif prediction <= 45:

        st.warning(status_message)

    else:

        st.error(status_message)


    # ========================================================
    # INPUT SUMMARY
    # ========================================================

    with st.expander("🔎 View Model Input"):

        st.dataframe(
            input_data,
            use_container_width=True
        )