import pdfplumber


def extract_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text



def analyze_resume(file):

    text = extract_text(file)

    text_lower = text.lower()


    skills_list = [
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
        "Artificial Intelligence",
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


    found_skills = []


    for skill in skills_list:

        if skill.lower() in text_lower:

            found_skills.append(skill)



    # Resume score calculation

    score = min(
        len(found_skills) * 5 + 50,
        100
    )


    suggestions = []


    if len(found_skills) < 5:

        suggestions.append(
            "Add more technical skills"
        )


    if "project" not in text_lower:

        suggestions.append(
            "Add more projects with descriptions"
        )


    if "github" not in text_lower:

        suggestions.append(
            "Add GitHub profile and coding projects"
        )


    if len(found_skills) >= 5:

        suggestions.append(
            "Great technical skill coverage"
        )


    return {

        "skills": found_skills,

        "score": score,

        "suggestions": suggestions

    }