import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

## 1. Import data
data = pd.read_csv('covid19-symptoms-dataset.csv')
#2. Split data into the input features and output class
X = data.drop('Infected', axis=1)
y = data['Infected']
# 3. Split data into test and training data
# split into test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
## 4. Train and test model
# create model"
clf = RandomForestClassifier()
# train model",
clf.fit(X_train, y_train)
# score model"
clf.score(X_test, y_test)
# confirm what the feature labels are
X.columns
# test making a prediction
clf.predict([[1,0,1,0]])
## 5. Export model
joblib.dump(clf, 'covid_predictor.pkl')
