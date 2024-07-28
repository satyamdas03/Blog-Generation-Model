import streamlit as st
from ctransformers import AutoModelForCausalLM  # Importing from ctransformers
from langchain.prompts import PromptTemplate

## Function To get response from the Llama2 model
def getLLamaresponse(input_text, no_words, blog_style):
    ## Loading the model
    llm = AutoModelForCausalLM.from_pretrained(
        "D:\\Blog_generation_model\\model\\llama-2-7b-chat.ggmlv3.q8_0.bin",  # Adjust this path as needed
        model_type="llama"
    )

    ## Prompt template
    template = """
    write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'], template=template)

    ## Generating the response from the model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response

st.set_page_config(
    page_title="Generate Blogs",
    page_icon=' ',
    layout='centered',
    initial_sidebar_state='collapsed'
)
st.header('Generate Blogs')
input_text = st.text_input("Enter the Blog Topic")

# Creating additional fields for the number of words and blog style
col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input('Number of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)
submit = st.button("Generate")

# Final Response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
