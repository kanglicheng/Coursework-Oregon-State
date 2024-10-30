from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

data = pd.read_csv('hw1-data/income.dev.csv', header=0)
train_labels = data['target']
data.drop(['id', 'target'], axis=1, inplace=True)
print(data.head())
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

encoder.fit(data)
train_binary_data = encoder.transform(data)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_binary_data, train_labels)

full_train = pd.read_csv('hw1-data/income.test.blind.csv', header=0)
full_train.drop(['id'], axis=1, inplace=True)
full_train_binary_data = encoder.transform(full_train)
prediction = knn.predict(full_train_binary_data)

full_train = pd.read_csv('hw1-data/income.test.blind.csv', header=0)
full_train['target'] = prediction
full_train.to_csv('output.csv', index=False)
