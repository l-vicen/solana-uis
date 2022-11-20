import db
import plotly.graph_objects as go
import streamlit as st

def display_customer_dashboard():

    c1, c2, c3 = st.columns([1,1,1])
    c2.markdown("## Customer Credit Score")
    df = db.getDataSheetCS()
    #st.table(df)

    address = c2.text_input('Your SOL wallet address')
    if address == "":
        c2.warning("Enter Wallet Address")
    else:
        c2.success("Credit Score Queried")
        c2.markdown('The current movie title is: ' + address)

    score = []
    #score.append(1)

    dictionary = df.set_index('Wallets').T.to_dict('list')
    st.write(dictionary)

    score = 0
    for key, value in dictionary.items():
        if (address == key):
            score += value[0] 
            break

    # df = df[df.Wallets == address]
    # c2.table(df)
    # score = df['Credit Scores']
    # print("type", type(score))
    if score > 0:
        # print("print1", score[0])
        #st.write(score)

        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Score"}))

        c2.plotly_chart(fig)
