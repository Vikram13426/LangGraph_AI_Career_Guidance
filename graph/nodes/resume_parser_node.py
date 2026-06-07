from pypdf import PdfReader

from graph.state import CareerState

text1=""
def resume_parser_node(
    state: CareerState
):

    resume_path = state.get(
        "resume_path",
        ""
    )

    if not resume_path:

        return {

            "resume_text":
                ""

        }

    try:

        reader = PdfReader(
            resume_path
        )

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text

                text += "\n"
        text1=text        

        return {

            "resume_text":
                text

        }

    except Exception as e:

        print(
            "Resume Parsing Error:",
            e
        )

        return {

            "resume_text":
                ""

        }
        print("\n========== RESUME TEXT ==========\n")
print(text1[:1000])
print("\n===============================\n")
print("Resume Parser Executed")