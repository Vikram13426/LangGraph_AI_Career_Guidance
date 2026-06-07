from langchain_core.prompts import (
    PromptTemplate
)

from graph.state import CareerState

from utils.llm import llm

from utils.prompts import (
    PROFILE_ANALYSIS_PROMPT
)


prompt = PromptTemplate(

    input_variables=[

    "skills",

    "interests",

    "experience",

    "goals",

    "memory_context",

    "resume_analysis",

    "retrieved_context"

],

    template=PROFILE_ANALYSIS_PROMPT

)


def profile_node(
    state: CareerState
):

    formatted_prompt = prompt.format(

    skills=
        state["skills"],

    interests=
        state["interests"],

    experience=
        state["experience"],

    goals=
        state["goals"],

    memory_context=
        state["memory_context"],

    resume_analysis=
        state["resume_analysis"],

    retrieved_context=
        state["retrieved_context"]

)

    response = llm.invoke(
        formatted_prompt
    )

    return {

        "profile_analysis":
            response.content

    }
print("Profile Node Executed")    