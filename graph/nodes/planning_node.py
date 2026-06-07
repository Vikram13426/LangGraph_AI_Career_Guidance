from langchain_core.prompts import PromptTemplate

from graph.state import CareerState

from utils.llm import llm

from utils.prompts import (
    CAREER_PLANNING_PROMPT
)


prompt = PromptTemplate(

    input_variables=[
        "profile_analysis"
    ],

    template=CAREER_PLANNING_PROMPT

)


def extract_section(text, start, end=None):

    start_idx = text.find(start)

    if start_idx == -1:
        return ""

    start_idx += len(start)

    if end:

        end_idx = text.find(end)

        return text[start_idx:end_idx].strip()

    return text[start_idx:].strip()


def planning_node(
    state: CareerState
):

    formatted_prompt = prompt.format(

        profile_analysis=
            state["profile_analysis"]

    )

    response = llm.invoke(
        formatted_prompt
    )

    content = response.content


    career_paths = extract_section(
        content,
        "CAREER_PATHS:",
        "ROADMAP:"
    )

    roadmap = extract_section(
        content,
        "ROADMAP:",
        "PROJECTS:"
    )

    projects = extract_section(
        content,
        "PROJECTS:",
        "INTERVIEW_PREP:"
    )

    interview_prep = extract_section(
        content,
        "INTERVIEW_PREP:",
        "LEARNING_RESOURCES:"
    )

    learning_resources = extract_section(
        content,
        "LEARNING_RESOURCES:"
    )

    return {

        "career_paths":
            career_paths,

        "roadmap":
            roadmap,

        "projects":
            projects,

        "interview_prep":
            interview_prep,

        "learning_resources":
            learning_resources

    }
print("Planning Node Executed")    