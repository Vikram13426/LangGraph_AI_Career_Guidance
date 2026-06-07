import json
import os

from datetime import datetime

from graph.state import CareerState


MEMORY_FILE = (
    "memory/career_history.json"
)


def memory_saver_node(
    state: CareerState
):

    if os.path.exists(
        MEMORY_FILE
    ):

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

    else:

        history = []

    history.append({

        "goal":
            state["goals"],

        "career_paths":
            state["career_paths"],

        "date":
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M"
            )

    })

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            history,

            file,

            indent=4

        )

    return {}
print("Memory Saver Executed")