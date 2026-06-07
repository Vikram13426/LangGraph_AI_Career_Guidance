document.addEventListener(
    "DOMContentLoaded",
    () => {

        const tabButtons =
            document.querySelectorAll(".tab-btn");

        const tabContents =
            document.querySelectorAll(".tab-content");

        tabButtons.forEach(button => {

            button.addEventListener(
                "click",
                () => {

                    const targetTab =
                        button.dataset.tab;

                    tabButtons.forEach(btn =>
                        btn.classList.remove(
                            "active"
                        )
                    );

                    tabContents.forEach(content =>
                        content.classList.remove(
                            "active-tab"
                        )
                    );

                    button.classList.add(
                        "active"
                    );

                    document
                        .getElementById(
                            targetTab
                        )
                        .classList.add(
                            "active-tab"
                        );

                }
            );

        });

        loadHistory();

    }
);


async function generateCareerGuidance() {

    const skills =
        document.getElementById(
            "skills"
        ).value.trim();

    const interests =
        document.getElementById(
            "interests"
        ).value.trim();

    const experience =
        document.getElementById(
            "experience"
        ).value;

    const goals =
        document.getElementById(
            "goals"
        ).value.trim();

    const resumeFile =
        document.getElementById(
            "resume"
        ).files[0];

    if (

        !skills ||

        !interests ||

        !experience ||

        !goals

    ) {

        showValidationError();

        return;
    }

    showLoadingState();

    try {

        const formData =
            new FormData();

        formData.append(
            "skills",
            skills
        );

        formData.append(
            "interests",
            interests
        );

        formData.append(
            "experience",
            experience
        );

        formData.append(
            "goals",
            goals
        );

        if (resumeFile) {

            formData.append(
                "resume",
                resumeFile
            );

        }

        const response =
            await fetch(
                "/generate",
                {

                    method: "POST",

                    body: formData

                }
            );

        const data =
            await response.json();

        populateTabs(data);

        loadHistory();

    }

    catch (error) {

        console.error(error);

        showErrorState();

    }

}


function populateTabs(data) {

    document
        .getElementById(
            "overview"
        )
        .innerHTML =
        marked.parse(
            data.overview || ""
        );

    document
        .getElementById(
            "career_paths"
        )
        .innerHTML =
        marked.parse(
            data.career_paths || ""
        );

    document
        .getElementById(
            "roadmap"
        )
        .innerHTML =
        marked.parse(
            data.roadmap || ""
        );

    document
        .getElementById(
            "projects"
        )
        .innerHTML =
        marked.parse(
            data.projects || ""
        );

    document
        .getElementById(
            "interview_prep"
        )
        .innerHTML =
        marked.parse(
            data.interview_prep || ""
        );

    document
        .getElementById(
            "learning_resources"
        )
        .innerHTML =
        marked.parse(
            data.learning_resources || ""
        );

    const resumeTab =
        document.getElementById(
            "resume_analysis"
        );

    if (resumeTab) {

        resumeTab.innerHTML =
            marked.parse(
                data.resume_analysis ||
                "No resume uploaded."
            );

    }
    const knowledgeTab =
        document.getElementById(
            "knowledge_sources"
        );

    if (knowledgeTab) {

        knowledgeTab.innerHTML =
            marked.parse(

                data.knowledge_sources ||

                "No knowledge sources retrieved."

            );

    }

}


async function loadHistory() {

    try {

        const response =
            await fetch(
                "/history"
            );

        const history =
            await response.json();

        const historyTab =
            document.getElementById(
                "history"
            );

        if (!historyTab) {

            return;

        }

        if (!history.length) {

            historyTab.innerHTML = `

                <h2>
                    No Previous Sessions
                </h2>

                <p>
                    Generate your first roadmap
                    to start building history.
                </p>

            `;

            return;
        }

        let html = `

            <h2>
                Career History
            </h2>

        `;

        history.forEach(item => {

            html += `

                <div class="history-card">

                    <h3>
                        ${item.goal}
                    </h3>

                    <p>

                        <strong>Date:</strong>

                        ${item.date}

                    </p>

                    <hr>

                    <div>

                        ${marked.parse(
                item.career_paths
            )}

                    </div>

                </div>

            `;

        });

        historyTab.innerHTML =
            html;

    }

    catch (error) {

        console.error(error);

    }

}


function showLoadingState() {

    const loadingHTML = `

        <div class="loading-container">

            <div class="loader"></div>

            <h3>
                CareerForge AI is analyzing your profile...
            </h3>

            <p>
                Building your personalized roadmap.
            </p>

        </div>

    `;

    document
        .querySelectorAll(
            ".tab-content"
        )
        .forEach(tab => {

            tab.innerHTML =
                loadingHTML;

        });

}


function showValidationError() {

    document
        .getElementById(
            "overview"
        )
        .innerHTML = `

            <div class="error-box">

                <h3>
                    Missing Information
                </h3>

                <p>
                    Please fill all required fields.
                </p>

            </div>

        `;

}


function showErrorState() {

    document
        .querySelectorAll(
            ".tab-content"
        )
        .forEach(tab => {

            tab.innerHTML = `

                <div class="error-box">

                    <h3>
                        Something Went Wrong
                    </h3>

                    <p>
                        Please try again.
                    </p>

                </div>

            `;

        });

}