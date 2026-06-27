#Inventio interface
 
import streamlit as st

st.set_page_config(page_title="Inventio", page_icon=":house:", layout="wide")

add_item_page=st.Page("views/add_item.py",title="Ajouter un objet",icon="➕")
dashboard_page=st.Page("views/dashboard.py",title="Tableau de bord",icon="📊")

pg = st.navigation([add_item_page, dashboard_page])

pg.run()

