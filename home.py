# Dependencies
import streamlit as st
import pandas as pd

def display_home():
    st.title('S-Moody')
    st.markdown("##### First credit rating project for Solana Ecosystem.")
    col1, col2 = st.columns([1,1])

    col1.header('About')
    col1.info('Our approach to the @hackTUM Challenge is to work on the incentives of the agents participating in a Solana Pay Transaction. We believe one way to approach this incentive dilemma is by providing the Customer with one way to keep track of his Credit Score and providing Merchants the opportunity to have analytics of products & transaction-related data. Least but not least, the Loaner is incentivized by having the opportunity to allocate his capital with more information and sometime security.')

    col2.header('App Features')
    col2.info(
        """
        * Solana Pay: On-chain Referecing
        * Helius-Listener Integration:
            * Credit Scoring Mechanism
            * Analytics Aggregador (Sheets)
        * Agents UIs: 
            * Customer
            * Merchant
            * Loaner
        """
    )
    st.markdown('---')

class Sidebar: 

    # Sidebar attribute Logo
    def sidebar_functionality(self):
        st.sidebar.image('assets/solana.png')
        st.sidebar.markdown('---')

    def sidebar_contact(self):
        st.sidebar.markdown('##### Contributors')
        st.sidebar.markdown('Lucas Perasolo')
        st.sidebar.markdown('Kirill Molchanov')
        st.sidebar.markdown('Yulan Xie')
        st.sidebar.markdown('---')
sidebar = Sidebar()