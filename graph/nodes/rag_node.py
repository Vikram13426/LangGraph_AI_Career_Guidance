from langchain_chroma import (
    Chroma
)

from graph.state import CareerState

from utils.embeddings import (
    embedding_model
)


VECTOR_DB_PATH = (
    "vector_store"
)


def rag_node(
    state: CareerState
):

    query = f"""

Career Goal:
{state["goals"]}

Skills:
{state["skills"]}

Interests:
{state["interests"]}

"""

    try:

        vector_db = Chroma(

            persist_directory=
                VECTOR_DB_PATH,

            embedding_function=
                embedding_model

        )

        results = vector_db.similarity_search(

            query,

            k=3

        )

        retrieved_context = ""

        retrieved_sources = ""

        for idx, doc in enumerate(results, start=1):

            retrieved_context += (

                doc.page_content

                + "\n\n"

            )

            source = doc.metadata.get(
                "source",
                "Unknown Document"
            )

            retrieved_sources += f"""

### Source {idx}

{source}

---

"""

        return {

            "retrieved_context":
                retrieved_context,

            "retrieved_sources":
                retrieved_sources

        }

    except Exception as e:

        print(
            "RAG Error:",
            e
        )

        return {

            "retrieved_context":
                "",

            "retrieved_sources":
                ""

        }