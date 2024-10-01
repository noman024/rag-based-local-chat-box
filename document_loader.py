from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
)
import os
import pandas as pd
from typing import List
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import glob

TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)


def load_documents_into_database(model_name: str, documents_path: str) -> Chroma:
    """
    Loads documents from the specified directory into the Chroma database
    after splitting the text into chunks.

    Returns:
        Chroma: The Chroma database with loaded documents.
    """

    print("Loading documents")
    raw_documents = load_documents(documents_path)
    documents = TEXT_SPLITTER.split_documents(raw_documents)

    print("Creating embeddings and loading documents into Chroma...")
    db = Chroma.from_documents(
        documents,
        OllamaEmbeddings(model=model_name),
    )
    print("Successfully loaded documents into Chroma.")
    return db

def load_documents(path: str) -> List[Document]:
    """
    Loads documents from the specified directory path.

    This function supports loading of PDF, Markdown, XLSX, CSV, and JSON documents.
    It checks if the provided path exists and raises a FileNotFoundError if it does not.

    Args:
        path (str): The path to the directory containing documents to load.

    Returns:
        List[Document]: A list of loaded documents.

    Raises:
        FileNotFoundError: If the specified path does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The specified path does not exist: {path}")

    loaders = {
        ".pdf": DirectoryLoader(
            path,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
            show_progress=True,
            use_multithreading=True,
        ),
        ".md": DirectoryLoader(
            path,
            glob="**/*.md",
            loader_cls=TextLoader,
            show_progress=True,
        ),
        ".xlsx": load_xlsx_files,
        ".csv": load_csv_files,
        ".json": load_json_files,
    }

    docs = []
    for file_type, loader in loaders.items():
        print(f"Loading {file_type} files")
        if callable(loader):
            docs.extend(loader(path))
        else:
            docs.extend(loader.load())
    return docs

def load_xlsx_files(path: str) -> List[Document]:
    """
    Loads and processes XLSX files into a list of Document objects.

    Args:
        path (str): The directory path to XLSX files.

    Returns:
        List[Document]: A list of Document objects created from the XLSX files.
    """
    docs = []
    for file in glob.glob(os.path.join(path, "**/*.xlsx"), recursive=True):
        df = pd.read_excel(file)
        content = df.to_string()
        doc = Document(page_content=content, metadata={"source": file, "page": 1})
        docs.append(doc)
    return docs


def load_csv_files(path: str) -> List[Document]:
    """
    Loads and processes CSV files into a list of Document objects.

    Args:
        path (str): The directory path to CSV files.

    Returns:
        List[Document]: A list of Document objects created from the CSV files.
    """
    docs = []
    for file in glob.glob(os.path.join(path, "**/*.csv"), recursive=True):
        df = pd.read_csv(file)
        content = df.to_string()
        doc = Document(page_content=content, metadata={"source": file, "page": 1})
        docs.append(doc)
    return docs


def load_json_files(path: str) -> List[Document]:
    """
    Loads and processes JSON files into a list of Document objects.

    Args:
        path (str): The directory path to JSON files.

    Returns:
        List[Document]: A list of Document objects created from the JSON files.
    """
    docs = []
    for file in glob.glob(os.path.join(path, "**/*.json"), recursive=True):
        with open(file, "r") as f:
            data = f.read()
        doc = Document(page_content=data, metadata={"source": file, "page": 1})
        docs.append(doc)
    return docs
