import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
#Load the csv file
df = pd.read_csv("Iris.csv")

print(df.head())

#select independent and dependent variable
x = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
y = df["Species"]


#split the dataset into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50)

#Feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test= sc.transform(x_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(x_train, y_train)

# Make pickle file of our model
pickle.dump(classifier, open("model.pkl", "wb"))