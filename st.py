import streamlit as st
import snowflake.connector
import os


def connect(account, user):
    
    conn = snowflake.connector.connect(
        user=user,
        account=account,
        authenticator = 'externalbrowser'
        #warehouse=WAREHOUSE,
        #database=DATABASE,
        #schema=SCHEMA
        )

    (col1,) = conn.cursor().execute("select 'Hello from Snowflake' col").fetchone()
    st.write(col1)


st.write('This is streamlit.')

account = st.text_input(label = "account", value = "")
user = st.text_input(label = "user", value = "")
btn_connect = st.button(label = "Connect", on_click=connect, args=(account, user))
