
# Retrieval Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is an AI framework that improves the output of large language models (LLMs) by combining them with traditional information retrieval systems

## References

[RAG Documentation](https://python.langchain.com/docs/tutorials/rag/)

[Pinecone](https://www.pinecone.io/)

[Huggingface](https://huggingface.co/)

[Google Gemini API](https://ai.google.dev/)






## Installation

Install my-project with npm

```bash
  pipenv shell
```

Installing Langchain, Langchain Core, Langchain Google GenAI etc
    
```bash
  pipenv install langchain_google_genai langchain langchain_core langchain_huggingface langchain_pinecone langchain_community langchain_text_splitters
```

Installing dotenv package for storing API keys, and other important credentials

```bash
  pip install python-dotenv
```

After installing this package create .env file and add below GOOGLE API KEY from https://ai.google.dev/

```bash
  GOOGLE_API_KEY=AIzaSyDfJIcDSXgRZvW3GdFzCIo1iPBXHXULh8Q
```

Visit Pinecone website to create new index &
get your pinecone api key and add that inside the .env file

```bash
  PINECONE_API_KEY=AIzaSyDfJIcDSXgRZvW3GdFzCIo1iPBXHXULh8Q
```

Replace your pincone key with above dummy key.


## Project Info

This project is divided into 2 parts

    1. Ingestion
    2. Retrieve


