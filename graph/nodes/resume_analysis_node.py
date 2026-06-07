from langchain_core.prompts import (
    PromptTemplate
)

from graph.state import CareerState

from utils.llm import llm

from utils.prompts import (
    RESUME_ANALYSIS_PROMPT
)


prompt = PromptTemplate(

    input_variables=[
        "resume_text"
    ],

    template=
        RESUME_ANALYSIS_PROMPT

)


def resume_analysis_node(
    state: CareerState
):

    resume_text = state.get(
        "resume_text",
        ""
    )

    if not resume_text.strip():

        return {

            "resume_analysis":
                "No resume uploaded."

        }

    formatted_prompt = prompt.format(

        resume_text=
            resume_text[:12000]

    )

    response = llm.invoke(
        formatted_prompt
    )

    return {

        "resume_analysis":
            response.content

    }