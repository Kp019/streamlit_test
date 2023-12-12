import streamlit as st
from st_supabase_connection import SupabaseConnection

st.title('host')

st.subheader('Host your event')

name = st.text_input('Event Name')
date = st.text_input('Event Date')
description = st.text_input('Event Description')


conn = st.connection("supabase",type=SupabaseConnection)
rows = conn.query("*", table="eve", ttl="0").execute()

for row in rows.data:
    st.write(f"{row['event_name']}")