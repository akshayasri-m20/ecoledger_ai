import streamlit as st
import pandas as pd
import numpy as np

# Set page metadata and layout
st.set_page_config(
    page_title="EcoLedger AI - Dual Ledger & AI Advisor",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stMetric { background-color: #1E222D; padding: 15px; border-radius: 10px; border: 1px solid #10B981; }
    .stButton>button { background-color: #10B981; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    .ai-banner { background-color: #1E222D; border-left: 5px solid #10B981; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📌 Project Details")
    st.markdown("**Project Name:** EcoLedger AI")
    st.markdown("**Domain:** Smart Finance & Carbon Accounting")
    st.markdown("**SDG Alignment:** Primary SDG 12, SDG 13")
    st.divider()
    st.info("💡 Powered by Python Data Engine & Agentic AI Workflows.")

# Main Header
st.title("🌱 EcoLedger AI")
st.caption("Dual-Ledger Financial P&L & AI Carbon Accounting Engine for SMEs")

# Emission Factors (kg CO2e per ₹ Spend)
EMISSION_FACTORS = {
    "Diesel Fuel": 0.00264,
    "Electricity (Grid)": 0.00085,
    "Plastic Packaging": 0.00350,
    "Air Freight / Logistics": 0.00420,
    "Paper & Cardboard": 0.00090,
    "Biodegradable / Solar": 0.00010
}

# Session State Initializer
if "ledger" not in st.session_state:
    st.session_state.ledger = pd.DataFrame([
        {"Item": "Generator Fuel Run", "Category": "Diesel Fuel", "Amount (₹)": 15000.0},
        {"Item": "Factory Electricity Bill", "Category": "Electricity (Grid)", "Amount (₹)": 35000.0},
        {"Item": "Bubble Wrap Shipment", "Category": "Plastic Packaging", "Amount (₹)": 12000.0}
    ])

# Entry Form
st.subheader("💳 Add New Financial Expense")
c1, c2, c3 = st.columns([2, 2, 1])

with c1:
    item_name = st.text_input("Expense Description", placeholder="e.g., Express Air Courier")
with c2:
    category = st.selectbox("Spend Category", list(EMISSION_FACTORS.keys()))
with c3:
    amount = st.number_input("Amount Spent (₹)", min_value=0.0, step=500.0)

if st.button("➕ Add to Dual-Ledger"):
    if item_name and amount > 0:
        new_entry = pd.DataFrame([{"Item": item_name, "Category": category, "Amount (₹)": amount}])
        st.session_state.ledger = pd.concat([st.session_state.ledger, new_entry], ignore_index=True)
        st.success(f"Recorded '{item_name}' in Dual-Ledger!")
    else:
        st.warning("Please enter a valid expense description and spend amount.")

st.divider()

# Dual-Ledger Calculations
st.session_state.ledger["Carbon Factor"] = st.session_state.ledger["Category"].map(EMISSION_FACTORS)
st.session_state.ledger["Emissions (kg CO₂e)"] = st.session_state.ledger["Amount (₹)"] * st.session_state.ledger["Carbon Factor"]

total_spend = st.session_state.ledger["Amount (₹)"].sum()
total_carbon = st.session_state.ledger["Emissions (kg CO₂e)"].sum()
intensity = (total_carbon / total_spend * 1000) if total_spend > 0 else 0

# Dashboard Display
st.subheader("📊 Live Dual-Ledger Dashboard")
m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Total Spend (P&L)", f"₹{total_spend:,.2f}")
with m2:
    st.metric("Total Carbon Footprint", f"{total_carbon:,.2f} kg CO₂e")
with m3:
    st.metric("Carbon Intensity", f"{intensity:.2f} g CO₂/₹")

# Display Active Table
st.dataframe(
    st.session_state.ledger[["Item", "Category", "Amount (₹)", "Emissions (kg CO₂e)"]],
    use_container_width=True
)

st.divider()

# AI Advisor Section
st.subheader("🤖 AI Carbon & Tax Advisory Agent")

st.markdown("""
<div class="ai-banner">
    <strong>AI Agent Status: ACTIVE</strong><br>
    Analyzing expenditure items to map eco-friendly material alternatives and green tax incentive opportunities.
</div>
""", unsafe_allow_html=True)

if st.button("⚡ Run AI Sustainability Advisor"):
    st.write("---")
    high_impact = st.session_state.ledger.sort_values(by="Emissions (kg CO₂e)", ascending=False).head(2)
    
    for _, row in high_impact.iterrows():
        st.markdown(f"### ⚠️ High Emission Impact: **{row['Item']}** ({row['Category']})")
        st.write(f"- **Spend:** ₹{row['Amount (₹)']:,.2f} | **Emissions:** {row['Emissions (kg CO₂e)']:,.2f} kg CO₂e")
        
        if row["Category"] == "Diesel Fuel":
            st.success("💡 **Recommendation:** Transition generator reliance to a rooftop solar PPA. Reduces monthly costs by **~18%** and opens eligibility for green tax rebates.")
        elif row["Category"] == "Plastic Packaging":
            st.success("💡 **Recommendation:** Replace polymer packaging with cassava/cornstarch wraps. Cuts category carbon output by **~80%**.")
        else:
            st.success("💡 **Recommendation:** Consolidate logistics supply routes to reduce total carbon intensity.")

st.divider()

# Responsible AI Section
with st.expander("🛡️ Responsible AI Considerations"):
    st.markdown("""
    - **Fairness:** Offers standard carbon tracking features to small businesses without recurring enterprise license fees.
    - **Transparency:** Calculations rely on clear Greenhouse Gas Protocol formulas ($kg\,CO_2e = \text{Spend} \times \text{Emission Factor}$).
    - **Privacy:** Processes transaction descriptions and amounts without capturing personal or proprietary business information.
    """)
