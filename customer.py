import db
import plotly.graph_objects as go
import streamlit as st

def display_customer_dashboard():
    """ Whole Customer Page is rendered by this method """
    c1, c2, c3 = st.columns([1,1,1]) # Style of page
    c2.markdown("## Customer Credit Score")
    df = db.getDataSheetCS() # Query to own built data hosted in Google Sheets
    #st.table(df)

    address = c2.text_input('Your SOL wallet address') # User Input
    if address == "":
        c2.warning("Enter Wallet Address")
    else:
        c2.success("Credit Score Queried")
        c2.markdown('The current movie title is: ' + address)

    # Matching Score to Wallet Address
    dictionary = df.set_index('Wallets').T.to_dict('list')
    # st.write(dictionary)

    score = 0
    for key, value in dictionary.items():
        if (address == key):
            score += value[0] 
            break

    if score > 0:
        # Plotting
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Score"}))

        c2.plotly_chart(fig)
