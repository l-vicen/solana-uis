# All dependencies
import streamlit as st
import pandas as pd

from google.oauth2 import service_account
from gspread_dataframe import get_as_dataframe
from gsheetsdb import connect
import gspread

# Create a connection object and config
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials) # Connection

# Get Request to own built DB -> Data containing <Wallet | Credit Score>
def getDataSheetCS():
    sa = gspread.service_account("credentials.json")
    sh = sa.open("hackaTUM")
    worksheet = sh.get_worksheet(1)
    df_read = get_as_dataframe(worksheet, usecols=[0,1], nrows=20)
    return df_read

# Get Request to own built DB -> Data containing Merchant Insights
def getDataSheetMA():
    sa = gspread.service_account("credentials.json")
    sh = sa.open("hackaTUM")
    worksheet = sh.get_worksheet(2)
    df_read = get_as_dataframe(worksheet, usecols=[0,1,2,3], nrows=9)
    return df_read

    
