# RAG-based Local Chat Box

Author: Md Mutasim Billah Abu Noman Akanda, Machine Learning Engineer  
Updated on: 1 October, 2024

## Project Description

RAG-based Local Chat Box is a Streamlit-based web application designed to integrate a Local Language Model (LLM) with Retrieval-Augmented Generation (RAG) capabilities. This project allows users to index documents, create embeddings, and interact with their data through an intuitive chat interface powered by state-of-the-art language models. Ideal for researchers and developers, `rag-based-local-chat-box` facilitates efficient data retrieval and conversational interactions within a local environment.

## Features

- **Model Selection:** Choose from a variety of local LLM models (`Mistral`, `llama`) to suit your needs.
- **Document Indexing:** Easily load and index documents from a specified directory.
- **Embedding Creation:** Utilize the `nomic-embed-text` model to create meaningful embeddings for your documents.
- **Interactive Chat Interface:** Engage with your indexed data through a seamless chat interface.
- **Session Management:** Maintains chat history and model selections across user sessions.
- **Real-time Responses:** Receive streaming responses from the LLM for a dynamic interaction experience.

## Project Structure

```
rag-based-local-chat-box/
├── ui.py                              # Main Streamlit application script
├── document_loader.py                 # Handles loading and indexing of documents
├── models.py                          # Retrieves and manages the list of available LLM models
├── llm.py                             # Manages interactions with the Language Model, including streaming responses
├── requirements.txt                   # Python package dependencies
├── README.md                          # Project documentation
└── Research/                          # Default directory for storing and indexing documents
```

## Prerequisites

Before setting up the project, ensure you have the following prerequisites installed:

- **Python:** Version 3.8 or higher
- **Streamlit:** For running the web application
- **Ollama:** A local LLM framework
- **Git:** For cloning the repository
- **Pip:** Python package installer

## Setup Instructions

### 1. Clone the Repository

Begin by cloning the `rag-based-local-chat-box` repository to your local machine:

```bash
git clone https://github.com/noman024/rag-based-local-chat-box.git
cd rag-based-local-chat-box
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
sudo chmod 777 setup_env.sh
./setup_env.sh
```

### 3. Prepare Your Documents

Place the documents you wish to index in the `Research/` directory or specify a different folder path via the application's sidebar.

## Usage

### Running the Application

Start the Streamlit application by navigating to the project directory and executing:

```bash
streamlit run ui.py
```

This command will launch the RAG-based Local Chat Box web interface in your default web browser.

### Using RAG-based Local Chat Box

#### 1. Select a Model:

- Navigate to the sidebar.
- Use the dropdown menu to select your desired local LLM model from the available options.

#### 2. Specify Folder Path:

- Enter the path to the folder containing the documents you wish to index.
- he default path is set to `Research`, but you can modify this as needed.

#### 3. Index Documents:

- Click the `Index Documents` button.
- The application will validate the directory and begin creating embeddings.
- Once indexing is complete, a confirmation message will appear.

#### 4. Interact via Chat:

- Use the chat input at the bottom of the interface to ask questions.
- The assistant will provide answers based on the indexed documents.
- Chat history is maintained throughout your session for continuity.

## Dependencies

RAG-based Local Chat Box relies on several Python packages and external tools:

- **Streamlit:** For building the web interface.
- **LangChain Community:** Provides utilities for working with language models.
- **Ollama:** Facilitates interactions with local LLMs.
- **nomic-embed-text:** Embedding model for creating document embeddings.

For the full list, see the `requirements.txt` file.

## Contact

If you have any questions or issues, please open an issue on the GitHub repository.
