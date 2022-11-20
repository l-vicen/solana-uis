import db
import plotly.graph_objects as go
import streamlit as st

def display_loaner_dashboard():
    """ Whole Customer Page is rendered by this method
          Super Similar to customer.py.
     """
    c1, c2, c3 = st.columns([1,1,1])
    c2.markdown("## Trustworthiness Of Address")
    df = db.getDataSheetCS()

    address = c2.text_input('The SOL wallet address you want to check is ', help="WalletAddress")
    if address == "":
        c2.warning("Enter Wallet Address")

    c2.markdown("#### Is this wallet a good payer?")
    
    # MAtching Address to Credit Score
    dictionary = df.set_index('Wallets').T.to_dict('list')
    score = 0
    for key, value in dictionary.items():
        if (address == key):
            score += value[0] 
            break

    if score > 0:
        if score > 20:
            c2.success("Yes")
            c2.image('assets/toTheMoon.webp')
        else:
            c2.error("No")
            c2.image('assets/c94.png')