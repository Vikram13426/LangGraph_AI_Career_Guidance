import os
import json

from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from graph.career_graph import (
    career_graph
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = (
    UPLOAD_FOLDER
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/generate",
    methods=["POST"]
)
def generate():

    skills = request.form.get(
        "skills"
    )

    interests = request.form.get(
        "interests"
    )

    experience = request.form.get(
        "experience"
    )

    goals = request.form.get(
        "goals"
    )

    resume_file = request.files.get(
        "resume"
    )

    resume_path = ""

    if resume_file:

        resume_path = os.path.join(

            app.config[
                "UPLOAD_FOLDER"
            ],

            resume_file.filename

        )

        resume_file.save(
            resume_path
        )

    state = {

        "skills":
            skills,

        "interests":
            interests,

        "experience":
            experience,

        "goals":
            goals,

        "resume_path":
            resume_path,

        "resume_analysis":
            "",

        "memory_context":
            "",

        "profile_analysis":
            "",

        "career_paths":
            "",

        "roadmap":
            "",

        "projects":
            "",

        "interview_prep":
            "",

        "learning_resources":
            ""

    }

    result = career_graph.invoke(
        state
    )

    return jsonify({

        "overview":
            result.get(
                "profile_analysis",
                ""
            ),

        "career_paths":
            result.get(
                "career_paths",
                ""
            ),

        "roadmap":
            result.get(
                "roadmap",
                ""
            ),

        "projects":
            result.get(
                "projects",
                ""
            ),

        "interview_prep":
            result.get(
                "interview_prep",
                ""
            ),

        "learning_resources":
            result.get(
                "learning_resources",
                ""
            ),

        "resume_analysis":
            result.get(
                "resume_analysis",
                ""
            ),
        "knowledge_sources":
            result.get(
            "retrieved_sources",
            ""
        )    
            

    })


@app.route("/history")
def history():

    memory_file = (
        "memory/career_history.json"
    )

    if not os.path.exists(
        memory_file
    ):

        return jsonify([])

    try:

        with open(
            memory_file,
            "r",
            encoding="utf-8"
        ) as file:

            history = json.load(
                file
            )

    except:

        history = []

    return jsonify(
        history[::-1]
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )