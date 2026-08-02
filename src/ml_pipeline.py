import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from rag import get_relevant_notes
import ollama

data=pd.read_csv("student_performance.csv",sep=";")
features=["studytime","failures","absences","G1","G2"]
X=data[features]
y=data["G3"]

model=RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X,y)

print("\n====Student Information===")
studytime=float(input("Study time(1-4):"))
failures=float(input("number of failures:"))
absences=float(input("number of absences:"))
G1=float(input("first period of grade(G1):"))
G2=float(input("second period of grade(G2):"))
student=pd.DataFrame(
    [[studytime,failures,absences,G1,G2]],
    columns=features
)

predicted_grade=model.predict(student)[0]
print("\nPredicted final grade:",round(predicted_grade,2))

print("\n=====Weak Topics=====")
weak_topics_input=input(
    "which topics do you find difficult?"
    "(seperate topics with commas):"
)
weak_topic_names=[
    topic.strip()
    for topic in weak_topics_input.split(",")
    if topic.strip()
]
notes=get_relevant_notes(weak_topic_names)

prompt = f"""
You are an AI Study Assistant.

Student's predicted final grade:
{predicted_grade:.2f}

Student's weak topics:
{", ".join(weak_topic_names)}

Relevant study notes:

{notes}

Based on the student's weak topics and the provided study notes:

1. Explain the weak topics in simple language.
2. Tell the student which topic should be studied first.
3. Create a simple 7-day study plan.
4. Give practical study tips.

Use the provided notes as the main study material.
"""

response=ollama.chat(
    model="llama3",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)
print("\n====================")
print("AI Study Assistant")
print("\n====================")
print(response["message"]["content"])
