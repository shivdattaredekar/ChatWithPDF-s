import os
import streamlit as st # To creat a streamlit app
from langchain.text_splitter import CharacterTextSplitter # Split the document into chunks
from langchain_community.embeddings import OpenAIEmbeddings # To create vectors from the chunks
from langchain_community.vectorstores import FAISS # To store the vectore and calculate the similarity 
from langchain_community.document_loaders import OnlinePDFLoader # To read the data from pdf documents 
from langchain_community.llms import OpenAI # To call OpenAI models
from langchain.chains.question_answering import load_qa_chain 
from dotenv import load_dotenv  # To load our api keys
load_dotenv()


# This function will help us to get all the text from the uploaded links  
def get_pdf_text(urls):
    all_text = ''
    for url in urls: # Loop to get the data from all the links
        loader = OnlinePDFLoader(url)
        data = loader.load()
        text = '\n'.join(str(document.page_content) for document in data)
        all_text += text
    return all_text

# This function will help us to split the text into chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separator='\n',
        length_function=len,
        )
    text_chunks = text_splitter.split_text(text)
    return text_chunks

# This function will help us to store the chunks in a vector store
def get_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)
    vector_store.save_local('FAISS_index') # Save the index in local environment
    return vector_store

# This function will help us to get the conversational chain
def get_conversational_chain():
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    return chain

# This function will help us to answer the user question
def user_input(user_question):
    embeddings = OpenAIEmbeddings()
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization= True) # calling our stored indexes
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain.run(input_documents=docs, question = user_question)
    print(response)
    st.write("Reply: ", response)

# This is the main function which will be called when we run this script
def main():
    # Streamlit framework
    st.set_page_config(page_title='ChatPDF', page_icon=':books:')
    st.title("Chat with PDF's")
    st.sidebar.subheader('Your documents')
    
    # Text input for pasting URLs
    url_inputs = []
    index = 0  
    while True:
        index += 1  
        url_input = st.sidebar.text_input(f"Paste PDF URL {index} here", key=f"url_input_{index}")
        if url_input == "":
            break
        url_inputs.append(url_input)

    # Button to trigger processing
    side_button = st.sidebar.button("Process URL's")

    # Answering the questions
    user_question = st.text_input("Ask a Question from the uploaded documents")
    if user_question:
        user_input(user_question)

    # Processing the URL's with side button
    if side_button:
        with st.spinner('Processing'):
            # Get the PDF text
            raw_text = get_pdf_text(url_inputs)  
            
            # Create the Text Chunks
            text_chunks = get_text_chunks(raw_text)
                
            # Create a vectore store
            vector_store = get_vector_store(text_chunks)

            # Key summary information
            st.write("Benefits of the scheme: ")
            st.write(user_input('what is the Scheme Benefits'))
            st.write("Application procedure: ")
            st.write(user_input('what is the Scheme Application Process'))
            st.write("Eligibility: ")
            st.write(user_input('what is the Eligibility for the Scheme'))
            st.write("Documents Required: ")
            st.write(user_input('what documents are required for Scheme'))

if __name__ == '__main__':
    main()




           







