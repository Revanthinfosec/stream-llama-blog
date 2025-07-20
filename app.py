import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

MODEL_PATH = "/Users/revanthchowdary/Desktop/projects/Lama /llama-2-7b-chat.ggmlv3.q8_0.bin"

#catche THE LLM SO IT ONLY LOADS ONCE
@st.cache_resource
def load_llm():
    return CTransformers(
        model=MODEL_PATH,
        model_type="llama",
        config={
            "max_new_tokens": 256,
            "temperature": 0.01, 
            # multi threading enables
                 "threads":4},
    )

def generate_blog(topic: str, n_words: int, style: str, stream: bool = False):
    llm = load_llm()
    template = """
    Write a {style}-style blog post of about {n_words} words on the topic: "{text}"
    """
    prompt = PromptTemplate(
        input_variables=["style", "text", "n_words"],
        template=template
    )
    prompt_text = prompt.format(style=style, text=topic, n_words=n_words)

    if stream:
        #3b stream token as they arrive
        output =""
        for token in llm.invoke(prompt_text, streaming=True):
            output += token
            yield output
    else:
        #3a one-shot generation
        yield llm.invoke(prompt_text)


st.set_page_config(page_title="Generate Blogs", layout="centered")
st.title("Generate Your Own Blog Posts")

#input and validation
topic = st.text_input("Blog topic:")
words = st.text_input("Number of words:")
style = st.selectbox("Write the blog for:", ("Researchers", "Data Scientist", "Data Engineer", "General Audience"))

if st.button("Generate"):
    if not topic or not words.isdigit():
        st.error("Please specify a topic and a numeric word count.")
    else:
        n = int(words)
        with st.spinner("Generating…"):
            #toggle stream= True if you want incremental updates
            for partial in generate_blog(topic, n, style, stream=True):
                st.write(partial)
        st.success("Done!")
