import streamlit as st
import pandas as pd

from google.oauth2 import service_account
from gspread_dataframe import get_as_dataframe
from gsheetsdb import connect
import gspread

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows

# def getDataSheetCS():
#     gsheet_url = "https://docs.google.com/spreadsheets/d/1TscPz0hQe8PbnS3gfssrYM21K_n4N1RR4kxAnWHjodc/edit?usp=sharing"
#     rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
#     df_gsheet = pd.DataFrame(rows)
#     return df_gsheet

def getDataSheetCS():
    sa = gspread.service_account("credentials.json")
    sh = sa.open("hackaTUM")
    worksheet = sh.get_worksheet(1)
    df_read = get_as_dataframe(worksheet, usecols=[0,1], nrows=20)
    return df_read

    
