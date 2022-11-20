import db
import plotly.graph_objects as go
import streamlit as st

def display_loaner_dashboard():
    c1, c2, c3 = st.columns([1,1,1])
    c2.markdown("## Trustworthiness Of Address")
    df = db.getDataSheetCS()

    address = c2.text_input('The SOL wallet address you want to check is ', help="WalletAddress")
    if address == "":
        c2.warning("Enter Wallet Address")
    
    #st.write('The current address is', address)
    score = []
    #score.append(1)
    c2.markdown("#### Is this wallet a good payer?")
    

    dictionary = df.set_index('Wallets').T.to_dict('list')
    # st.write(dictionary)
    score = 0
    for key, value in dictionary.items():
        if (address == key):
            score += value[0] 
            break

    # st.write(score)
    if score > 0:
        if score > 20:
            # print("print1", score)
            c2.success("Yes")
            c2.image('assets/toTheMoon.webp')
        else:
            c2.error("No")
            c2.image('assets/c94.png')