import db
import plotly.graph_objects as go
import streamlit as st

def display_loaner_dashboard():
    c1, c2, c3 = st.columns([1,1,1])
    c2.markdown("## Trustworthiness Of Address")
    df = db.getDataSheetCS()

    address = c2.text_input('The SOL wallet address you want to check is ', help="WalletAddress")
    #st.write('The current address is', address)

    score = []
    #score.append(1)
    c2.markdown("#### Is this wallet a good payer?")
    df = df[df.Wallets == address]
    #st.table(df)
    score = df['Credit Scores']
    print("type", type(score))
    if len(score) > 0:
        if score[0] > 20:
            print("print1", score[0])
            c2.success("Yes")
        else:
            c2.error("No")
            c2.image('assets/c94.png')
        #st.write(score)