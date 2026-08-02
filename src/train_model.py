import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score
data = pd.read_csv("student_performance.csv",sep=";")
print("Dataset loaded successfully")
print(data.columns.tolist())

features=["studytime","failures","absences","G1","G2"]
X=data[features]
y=data["G3"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("\nTraining samples:",len(X_train))
print("testing samples:",len(X_test))

model=RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)
print("\nModel trained successfully")

predictions=model.predict(X_test)

mae=mean_absolute_error(y_test,predictions)
r2=r2_score(y_test,predictions)

print("\nModel performance:")
print("MAE:",round(mae,2))
print("R2_Score:",round(r2,2))