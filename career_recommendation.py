def recommend_career(skills, interest):

    skills = skills.lower()
    interest = interest.lower()

    career = ""
    score = 0
    reason = ""
    missing = []


    if "python" in skills and ("sql" in skills or "excel" in skills):

        career = "Data Analyst"
        score = 80
        reason = "Your Python, SQL and Excel skills match analytics roles."

        if "power bi" not in skills:
            missing.append("Power BI")

        if "statistics" not in skills:
            missing.append("Statistics")


    elif "python" in skills and ("machine learning" in skills or "ai" in interest):

        career = "AI/ML Engineer"
        score = 75
        reason = "Your Python skills are suitable for Artificial Intelligence roles."

        if "tensorflow" not in skills:
            missing.append("TensorFlow")

        if "deep learning" not in skills:
            missing.append("Deep Learning")


    elif "html" in skills and "css" in skills:

        career = "Web Developer"
        score = 85
        reason = "Your frontend skills match web development."

        if "javascript" not in skills:
            missing.append("JavaScript")


    else:

        career = "Software Developer"
        score = 60
        reason = "Your skills match general software roles."

        missing.append("Advanced Programming Skills")


    return career, score, reason, missing