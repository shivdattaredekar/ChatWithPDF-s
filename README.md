# ChatPDF

ChatPDF is a Streamlit application that allows users to interact with PDF documents by uploading URLs of the PDFs and asking questions based on the content of those documents. The application leverages LangChain, OpenAI embeddings, and FAISS for text processing and similarity search.

https://github.com/shivdattaredekar/ChatWithPDFsWithLLM/assets/46707992/714a931e-d47f-46cf-8551-abac212c1222

## Features

- Upload PDF URLs and extract their text content.
- Split the text content into manageable chunks.
- Store the text chunks as embeddings in a FAISS vector store.
- Perform similarity searches based on user questions.
- Generate responses using OpenAI's language models.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ChatPDF.git
   cd ChatPDF

2. **Create and activate a virtual environment (optional but recommended):**

  python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the required packages**
  pip install -r requirements.txt
   
4. **Set up environment variables**
  OPENAI_API_KEY=your_openai_api_key

## Usage
   
1. **Run the Streamlit app**
  streamlit run app.py

2. **Interact with the app**
  Upload PDFs: Paste the URLs of the PDFs you want to upload in the sidebar.
  Process URLs: Click the "Process URLs" button to extract and process the text from the PDFs.
  Ask Questions: Enter your question in the text input field to get answers based on the uploaded PDFs.


### Part 2:

## Code Overview

### main.py
Main script that sets up the Streamlit interface and handles user interactions.

### get_pdf_text(urls)
Extracts text content from the given PDF URLs.

### get_text_chunks(text)
Splits the extracted text into manageable chunks.

### get_vector_store(chunks)
Converts text chunks into embeddings and stores them in a FAISS vector store.

### get_conversational_chain()
Creates a question-answering chain using OpenAI models.

### user_input(user_question)
Handles user questions by performing similarity search and generating responses.

## Dependencies

- Python 3.7+
- Streamlit
- LangChain
- OpenAI
- FAISS
- dotenv

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/langchain/langchain)
- [OpenAI](https://openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

If you have any questions or feedback, feel free to reach out to me at
- [Gmail](shivdattaredekar@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/shivdatta-redekar-93ab1511a)


