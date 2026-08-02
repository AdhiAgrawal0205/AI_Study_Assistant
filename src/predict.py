import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data=pd.read_csv("student_performance.csv",sep=";")

features=["studytime","failures","absences","G1","G2"]
X=data[features]
y=data["G3"]

model=RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X,y)

studytime=float(input("study time(1-4):"))
failures=float(input("number of failures:"))
absences=float(input("number of absences:"))
G1=float(input("first period grade(G1):"))
G2=float(input("second period grade(G2):"))

student=pd.DataFrame([[
    studytime,
    failures,
    absences,
    G1,
    G2
]],columns=features)
prediction=model.predict(student)[0]

print("\n------------------------")
print("AI Study Assistant")
print(f"Predicted Final Grade:{prediction:.2f}")