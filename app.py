from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_community.llms import Ollama
import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

##tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
##creating bot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Please provide reaponse to the user queries"),
        ("user","Question:{question}")
    ]
)
#streamlit
st.title("Secretary")
input_text=st.text_input("search the topic you want")
#open ai llm call

llm = Ollama(model="llama2")
output_parser=StrOutputParser()
##chain
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text}))
