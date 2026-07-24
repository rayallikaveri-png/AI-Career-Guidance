import streamlit as st
from ml_model import predict_career_ml
from resume_analyzer import analyze_resume


# Page settings
st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🌸",
    layout="wide"
)


# Cute Aesthetic CSS
st.markdown("""
<style>

.main {
    background-color: #fff7fb;
}

h1 {
    color: #d63384;
    text-align:center;
    font-family: "Comic Sans MS";
}

h2, h3 {
    color:#9c36b5;
}

p, label {
    font-size:16px;
}


/* Buttons */
.stButton button {

    background: linear-gradient(
        90deg,
        #ff8fab,
        #d63384
    );

    color:white;
    border-radius:25px;
    border:none;
    padding:12px;
    font-weight:bold;
}


/* Cards */
.card {

    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 5px 20px rgba(214,51,132,0.15);

}


/* Sidebar */

section[data-testid="stSidebar"] {

    background:#ffe5ec;

}

</style>
""", unsafe_allow_html=True)



# Header

st.markdown(
"""
<h1>🌸 AI Career Assistant 🎓</h1>

<center>
<p>
✨ Discover your perfect career path using Artificial Intelligence ✨
</p>
</center>

""",
unsafe_allow_html=True
)



# Sidebar

st.sidebar.title("🌷 Menu")

page = st.sidebar.radio(
    "Choose",
    [
        "Career Prediction",
        "Resume Analyzer"
    ]
)



# ================= CAREER PREDICTION =================


if page == "Career Prediction":


    st.header("💗 Create Your Career Profile")


    name = st.text_input(
        "🌸 Your Name"
    )


    education = st.text_input(
        "🎓 Education"
    )


    cgpa = st.number_input(
        "📊 CGPA",
        0.0,
        10.0,
        step=0.1
    )


    st.subheader("🛠 Select Your Skills")


    skills = st.multiselect(
        "Choose skills",
        [

            "Python",
            "Java",
            "C++",
            "SQL",
            "Excel",
            "Power BI",
            "Tableau",
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "Data Science",
            "Statistics",
            "AI",
            "NLP",
            "Computer Vision",
            "AWS",
            "Cloud Computing",
            "Linux",
            "Cyber Security",
            "Networking",
            "Git",
            "MongoDB",
            "Spring Boot",
            "IoT",
            "Robotics"

        ]
    )


    interests = st.multiselect(
        "💖 Select Your Interests",
        [

            "Data Analytics",
            "Data Science",
            "Artificial Intelligence",
            "Machine Learning",
            "Web Development",
            "Software Development",
            "Cyber Security",
            "Cloud Computing",
            "UI/UX Design",
            "IoT",
            "Robotics",
            "Automation",
            "Research",
            "Blockchain",
            "DevOps"

        ]
    )



    if st.button("✨ Analyze My Career"):


        if len(skills)==0 or len(interests)==0:

            st.warning(
                "Please select skills and interests 💗"
            )


        else:


            skill_text = ", ".join(skills)

            interest_text = ", ".join(interests)



            career, score = predict_career_ml(
                skill_text,
                interest_text
            )



            st.markdown(
                f"""
                <div class="card">

                <h2>🎯 Your Recommended Career</h2>

                <h1>{career}</h1>

                </div>
                """,
                unsafe_allow_html=True
            )



            st.subheader("📊 Career Match")

            st.progress(
                score/100
            )

            st.write(
                f"✨ {score}% Match"
            )



            st.subheader("🌱 Skills To Improve")


            improve = [

                "Deep Learning",
                "GitHub Projects",
                "Communication Skills",
                "Cloud Technologies",
                "Advanced Projects"

            ]


            for i in improve:

                st.write(
                    "🌸",
                    i
                )



# ================= RESUME ANALYZER =================



else:


    st.header("📄 Resume Analyzer ✨")


    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type="pdf"
    )


    if uploaded_file:


        result = analyze_resume(
            uploaded_file
        )


        st.markdown(
            f"""

            <div class="card">

            <h2>📊 Resume Score</h2>

            <h1>{result["score"]}%</h1>

            </div>

            """,
            unsafe_allow_html=True
        )



        st.subheader("💎 Skills Found")


        for skill in result["skills"]:

            st.write(
                "✅",
                skill
            )



        st.subheader("🌷 Suggestions")


        for s in result["suggestions"]:

            st.write(
                "💡",
                s
            )