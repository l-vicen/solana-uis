import db as db
import streamlit as st

def display_customer_dashboard():
    st.title('Customer Credit Score')
    df = db.getDataSheetCS()
    st.table(df)