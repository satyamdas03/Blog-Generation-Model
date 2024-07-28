1) to create the conda env --> create -p venv python==3.9 -y
2) next thing is to do is activate conda ==> conda activate D:\Blog_generation_model\venv
3) next thing is to do is to mention the dependencies inside the requirements.txt ==> pip install -r requirements.txt
4) coding up the app.py
    ==) import streamlit
    ==) import langchain.prompts
    ==) import langchain.llms
    ==) st.set_page_config --> setting the page title
                           --> setting page icon
                           --> layout
                           --> initial sidebar state
    ==) st.head
    ==) creating an input box --> input_text
    ==) creating 2 more fields below the input field, one field is about how many words we want for the blog, the other field or column is the blog style
        ---) the blog style will depict from whom we are writing the blog 
    ==) finally the submit button, which will submit all the information from above and generate the blog. 
    ==) in the final response, after the submit button is hit,
    it will call the function which will call the model and make the necessary operations
    we are going to use ctransformers, which will be used to call the llama2 model transformers

    ==) steps to create the function:
        --) arguments that will be taken as the input :
            ---) input_text,no_words,blog_style
        --) llm = using ctransformers add the model path
        --) model_type --> llama
        --) mentioning the config of the model
            ==> max_new_tokens = 256
            ==> temperature = 0.01 .. to expect different answers
        --) create a prompt template
        --) generating the response from the llama model
            ==> we have to format the prompt's format

5) to run the app : streamlit run app.py
