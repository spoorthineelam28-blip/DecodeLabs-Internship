import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


data = {
    'Attendance':[95,85,70,60,50,90,80,65,55,88],
    'Study_Hours':[8,7,5,4,3,9,6,4,2,7],
    'Marks':[90,80,65,55,40,92,78,58,35,85],
    'Result':['Pass','Pass','Average','Average',
              'Fail','Pass','Pass','Average',
              'Fail','Pass']
}

df = pd.DataFrame(data)

X = df[['Attendance','Study_Hours','Marks']]
y = df['Result']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred)*100)

print(classification_report(y_test,y_pred))

new_student = [[85,7,82]]

prediction = model.predict(new_student)

print("Predicted Result:",prediction[0])