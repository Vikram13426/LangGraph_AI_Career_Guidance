import json
import os

from graph.state import CareerState


MEMORY_FILE = (
    "memory/career_history.json"
)


def memory_loader_node(     
    state: CareerState
):

    if not os.path.exists(
        MEMORY_FILE
    ):

        return {

            "memory_context":
                "No previous history."

        }

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            history = json.load(
                file
            )

    except:

        history = []

    if not history:

        return {

            "memory_context":
                "No previous history."

        }

    latest_entries = history[-3:]

    memory_context = ""

    for entry in latest_entries:

        memory_context += f"""

Goal:
{entry['goal']}

Career Paths:
{entry['career_paths']}

Date:
{entry['date']}

"""

    return {

        "memory_context":
            memory_context

    }
print("Memory Loader Executed")    