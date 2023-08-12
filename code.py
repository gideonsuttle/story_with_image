from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain
import requests
import io
import streamlit as st
from PIL import Image
import streamlit as st
st.header("AI story image generator")
llm = Cohere(cohere_api_key="Q6ryuEOendZO0gOYBrToKNctroY7ehJOkkxeueV2")


def generate_image(prompt):
    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
        files={
            'prompt': (None, prompt, 'response')
        },
        headers={'x-api-key': '1051f780910c468e9b562f10427467ed86261f932d85a9d8b73062d7b30d27a86654934a75079f7890cf02712bf67337'}
    )

    if r.ok:
        images = Image.open(io.BytesIO(r.content))
        return images
    else:
        raise ValueError("Failed to generate image")




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
    index= max([len(array),len(array_para)])
    images=[]
    for i in range(len(array)):
        images.append(generate_image(array[i]))
    for i in range (index):
        if(i < len(array) and i<6):
            st.text(array[i])
        if(i < len(array_para) ):
            print('yay')
            st.text_area('',array_para[i])
        if(i < len(array) and i<6):
            st.image(images[i]) 
    print(array)
# def main():
st.button("response", on_click=hello())