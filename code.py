import langchain
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain
import requests
import io
import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debug: Check if environment variables are loaded
clipdrop_key = os.getenv('CLIPDROP_API_KEY')
cohere_key = os.getenv('COHERE_API_KEY')

if not clipdrop_key or not cohere_key:
    st.error("API keys not found in environment variables. Please check your .env file.")
    st.stop()

st.header("AI story image generator")
llm = Cohere(cohere_api_key=cohere_key)


def generate_image(prompt, save_path=None):
    try:
        r = requests.post('https://clipdrop-api.co/text-to-image/v1',
            files={
                'prompt': (None, prompt, 'text/plain')
            },
            headers={'x-api-key': clipdrop_key}
        )
        
        if r.ok:
            images = Image.open(io.BytesIO(r.content))
            if save_path:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                images.save(save_path)
            return images
        else:
            st.error(f"API Error: {r.status_code} - {r.text}")
            raise ValueError(f"Failed to generate image: {r.text}")
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        raise


def hello():
    template = """You are an AI assistant that writes in the style of an artist. always write in 5 paragraphs after each paragraph leave a line. Answer in 300 words or less
Your prompt is: {question}
"""
    question = st.text_input('Tell me your story')
    prompt1 = PromptTemplate(template=template, input_variables=["question"] )

    llm_chain = LLMChain(prompt=prompt1, llm=llm)
    if(question!='Tell me your story'):
        response = llm_chain.run(question)
        st.text_area("Story",response,height=200)
        # print(response)
        get_titles(response)
    
def get_titles(response):
    template1 = """give only 4 titles based on the story, return each title in quotes and in a new line : {response}"""
    prompt2 = PromptTemplate(template=template1, input_variables=["response"] )
    llm_chain = LLMChain(prompt=prompt2, llm=llm)
    response1 = llm_chain.run(response)
    st.text_area("image titles",response1)
    print(response1)
    get_array(response,response1)
    
def get_array(response,response1):
    array = response1.split("\n")
    array_para = response.split('-i787k-')
    index = max([len(array), len(array_para)])
    images = []
    
    # Create examples directory if it doesn't exist
    os.makedirs('examples', exist_ok=True)
    
    for i in range(len(array)):
        # Generate image and save it
        image_path = f'examples/image_{i+1}.jpg'
        images.append(generate_image(array[i], save_path=image_path))
    
    for i in range(index):
        if i < len(array) and i < 6:
            st.text(array[i])
        if i < len(array_para):
            st.text_area('', array_para[i])
        if i < len(array) and i < 6:
            st.image(images[i])
    print(array)
# def main():
st.button("response", on_click=hello())
