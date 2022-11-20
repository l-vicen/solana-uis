# Dependencies
import streamlit as st
import pandas as pd

def display_home():
    st.title('S-Moody')
    col1, col2 = st.columns([1,2])

    col1.header('About')
    col1.info('Web3 first credit rating for the Solana Ecosystem. Building credit based on day-to-day transactions via Solana-Pay')

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