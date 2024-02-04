import streamlit as st
import urllib
from PyPDF2 import PdfReader
from openNyaiSummariser import openNyaiSummarise

#https://raw.githubusercontent.com/OpenNyAI/Opennyai/master/samples/sample_judgment1.txt

st.set_page_config(
    page_title="ATTICUS AI",
    page_icon="👋",
)

st.write("# Welcome to Atticus AI's Summariser - Your personal Legal Assistant! 👋")

inputText = ""#variable that catches text for summarization

input_Selection = st.selectbox('Please select your input method', ('Select', 'Text Input', 'File Upload', 'URL'))
userSelection = st.empty()
submitButton = st.empty()
summarizedTextArea = st.empty()

if input_Selection=="Text Input": #if text is copy pasted, then open a text_area widget for the user to input text
    userSelection=st.text_area("Enter your text here",height=500)
    inputText = userSelection
elif input_Selection=="File Upload":#if the user wants to upload the file, then we have to read the text from the file.
    userSelection=st.file_uploader("Select your pdf",type=['pdf'])
    if (userSelection):
        pdf_reader = PdfReader(userSelection)
        inputText = ''.join(page.extract_text() for page in pdf_reader.pages)
    else:
        st.write("Please select a file...")
elif input_Selection=="URL": #When the user enters an URL, extract the text from that URL
    userSelection=st.text_input("Enter URL")
    urlInput = userSelection
    try:
        inputText = urllib.request.urlopen(urlInput).read().decode()
    except:
        st.write ("Input wrong. Failed to open the link. Please select a proper URL")
    else:
        st.write ("Select Input")

submitButton = st.button("Summarise")
summarizedText =""

print(inputText)
if (submitButton):
    if (inputText!=""): #If the text has some content, then send it openNyai Summarizer
        with st.spinner('Wait for it...'):
            summarizedText = openNyaiSummarise (inputText)
            if (summarizedText != None):
                summarizedTextArea = st.text_area("Summarized Text",summarizedText,height=300)
            else:
                st.error("Summary failed!!")
            st.success('Done!')

st.markdown(""" """)