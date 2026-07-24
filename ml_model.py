import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier


data = {

    "Skills": [
        ["Python","SQL","Excel"],
        ["Python","Machine Learning","TensorFlow"],
        ["HTML","CSS","JavaScript"],
        ["Java","Spring Boot","MongoDB"],
        ["AWS","Cloud Computing","Linux"],
        ["Cyber Security","Networking","Linux"],
        ["Python","Data Science","Statistics"],
        ["React","JavaScript","HTML"],
        ["Python","NLP","AI"],
        ["IoT","Robotics","Python"]
    ],

    "Interest": [
        "Data Analytics",
        "Artificial Intelligence",
        "Web Development",
        "Software Development",
        "Cloud Computing",
        "Cyber Security",
        "Data Science",
        "Web Development",
        "Artificial Intelligence",
        "IoT"
    ],

    "Career": [
        "Data Analyst",
        "AI Engineer",
        "Frontend Developer",
        "Backend Developer",
        "Cloud Engineer",
        "Cyber Security Analyst",
        "Data Scientist",
        "Full Stack Developer",
        "NLP Engineer",
        "IoT Engineer"
    ]
}


df = pd.DataFrame(data)


mlb = MultiLabelBinarizer()

skills_encoded = mlb.fit_transform(
    df["Skills"]
)


skills_df = pd.DataFrame(skills_encoded)


interest_encoded = pd.get_dummies(
    df["Interest"]
)


X = pd.concat(
    [
        skills_df,
        interest_encoded
    ],
    axis=1
)


X.columns = X.columns.astype(str)


y = df["Career"]


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(
    X,
    y
)



def predict_career_ml(skills, interests):

    user_skills = [
        x.strip()
        for x in skills.split(",")
    ]


    user_interest = interests.split(",")[0].strip()


    skill_vector = mlb.transform(
        [user_skills]
    )


    user_skill_df = pd.DataFrame(
        skill_vector
    )


    user_interest_df = pd.get_dummies(
        pd.Series([user_interest])
    )


    user_interest_df = user_interest_df.reindex(
        columns=interest_encoded.columns,
        fill_value=0
    )


    user_input = pd.concat(
        [
            user_skill_df,
            user_interest_df
        ],
        axis=1
    )


    user_input.columns = user_input.columns.astype(str)


    user_input = user_input.reindex(
        columns=X.columns,
        fill_value=0
    )


    prediction = model.predict(
        user_input
    )[0]


    probability = model.predict_proba(
        user_input
    )


    score = int(
        max(probability[0]) * 100
    )


    return prediction, score