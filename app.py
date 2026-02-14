import streamlit as st
from utils.validators import validate_url
from agent.core import process_url

st.set_page_config(page_title="Universal Profile Analyzer", layout="wide")

st.title("🌐 Universal Public Profile Intelligence Agent")

url = st.text_input("Enter Public URL")

if st.button("Analyze"):
    if not validate_url(url):
        st.error("Invalid URL")
    else:
        with st.spinner("Analyzing..."):
            result = process_url(url)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Analysis Complete")

            if "report" in result:
                st.markdown(result["report"])
            else:
                st.write(result)
