import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_chroma import (
    Chroma
)

from utils.embeddings import (
    embedding_model
)

KNOWLEDGE_FOLDER = (
    "knowledge_base"
)

VECTOR_DB_PATH = (
    "vector_store"
)


def load_documents():

    documents = []

    for file in os.listdir(
        KNOWLEDGE_FOLDER
    ):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(

                KNOWLEDGE_FOLDER,

                file

            )

            loader = PyPDFLoader(
                pdf_path
            )

            docs = loader.load()

            documents.extend(
                docs
            )

    return documents


def split_documents(
    documents
):

    splitter = (
        RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=200

        )
    )

    return splitter.split_documents(
        documents
    )


def create_vector_store():

    print(
        "\nLoading PDFs..."
    )

    documents = load_documents()

    print(
        f"Loaded {len(documents)} pages"
    )

    chunks = split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks"
    )

    vector_db = Chroma.from_documents(

        documents=chunks,

        embedding=
            embedding_model,

        persist_directory=
            VECTOR_DB_PATH

    )

    print(
        "\nVector Database Created Successfully"
    )

    print(
        f"Saved To: {VECTOR_DB_PATH}"
    )


if __name__ == "__main__":

    create_vector_store()