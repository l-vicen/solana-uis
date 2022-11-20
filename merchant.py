import streamlit as st
import pandas as pd
import db as db
import plotly.express as px
from datetime import datetime

def display_merchant_dashboard():
    st.title('Merchant Analytics')
    df = db.getDataSheetMA()
    st.write('---')
    st.write('## Dashboard')
    st.table(df)
    st.write('---')
    st.write('## Analytics')
    st.info("KPIs that might incentivize the Merchant to adopt Solana-Pay could be: Total Sales over Time, Preferred Goods, Number of Solana-Pay Clients etc ...")
    col1, col2 = st.columns([2,1])

    df["Products"] = df["Products"].astype(object)
    product = df["Products"].tolist()
    # st.write(product)

    # Edge case testing would be to provide a transaction with no product reference.
    count = []
    for t in range(len(product)):
        sum = 0
        s = product[t]
        for i in range(0, len(s)):
            if s[i] == " ":
                sum += 1
        count.append(sum + 1)
    # st.write(count)

    timestamps = df["Timestamp"].tolist()
    timestamps = [datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') for t in timestamps]
    # st.write(timestamps)
    f = px.line(timestamps, count)
    col1.subheader("Total Sales over Time")
    col1.plotly_chart(f)

    count = df["Solana_Payment"].value_counts()
    types = list(set(df["Solana_Payment"].tolist()))
    fig = px.pie(values = count, names = types)
    col2.subheader("Solana-Pay Users")
    col2.plotly_chart(fig)