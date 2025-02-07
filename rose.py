import streamlit as st


st.set_page_config(page_title="Rose_for_roseday", page_icon="🌹", layout="wide")


rose_ascii = """
⠀⠀⠀⠀⠀⠀⣴⣿⠋⢠⣟⣼⣷⠾⣎⣼⢇⣿⣄⠱⣄
⠀⠀⠀⠀⠀⠀⠹⣿⡀⣆⠙⠢⠐⠉⠉⣴⣾⣽⢟⡰⠃
⠀⠀⠀⠀⠀⠀⠀⡾⣿⣿⣦⠀⠤⢴⣿⠿⢋⣴⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠠⡦⣿⡙⠻⣿⣶⣦⣭⣉⠁⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣽⣷⠀⠈⠉⠉⠉⠉⠇⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠀⢹⣿⣦⣀⠀⠀⣀⡴⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⢻⣿⣿⣿⣿⢻⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣯⣿⠉⠻⣿⣿⣷⣂⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡃⠀⠈⢹⠻⣿⢇⠀
⢶⣾⣿⣿⣿⣿⣶⣤⣄⠀⠀⣿⣿⠀⠀⠀⠀⠉⠀⠈⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⠠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⠻⢿⣿⣿⠿⠻⣯⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀This rose is for you... from Hritesh :) :)⠀⠀"""


st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 80vh; font-size: 20px; white-space: pre;">
        <pre>{rose_ascii}</pre>
    </div>
    """,
    unsafe_allow_html=True
)