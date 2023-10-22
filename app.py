# app.py
import streamlit as st
from chatbot import handle_conversion

def main():
    st.title("Solidity to Clarity Converter")

    # Text area for user to input Solidity code
    solidity_code = st.text_area("Enter your Solidity code here:")

    if st.button("Convert"):
        if solidity_code:
            # Convert Solidity code to Clarity code and explain the changes
            clarity_code, explanation = handle_conversion(solidity_code)

            # Display the converted Clarity code
            st.subheader("Converted Clarity Code")
            st.code(clarity_code, language='clarity')

            # Display the explanation of changes
            st.subheader("Explanation of Changes")
            st.write(explanation)
        else:
            st.error("Please enter Solidity code to convert.")

if __name__ == "__main__":
    main()

