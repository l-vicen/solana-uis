import db as db
import streamlit as st

def display_customer_dashboard():
    df = db.getDataSheetCS()
    st.table(df)