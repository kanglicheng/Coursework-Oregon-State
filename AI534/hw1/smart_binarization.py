from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

data = pd.read_csv('hw1-data/income.train.5k.csv', header=0)
data['age'] = data['age'] / 100

num_processor = 'passthrough' # i.e., no transformation
cat_processor = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

num_features = ['age', 'hours']
cat_features = ['country', 'sector', 'edu', 'marriage', 'occupation', 'race', 'sex',]
preprocessor = ColumnTransformer([('num', num_processor, num_features),
                                  ('cat', cat_processor, cat_features)
                                 ])

preprocessor.fit(data)
print(len(preprocessor.get_feature_names_out()))
processed_data = preprocessor.transform(data)

# max_acc = 0
# best_k = 0  
# for i in range(1, 101, 2):
#     if i == 1:
#         continue
#     knn = KNeighborsClassifier(n_neighbors=i)
#     knn.fit(processed_data, data['target'])
#     prediction = knn.predict(processed_data)
#     print(i, accuracy_score(data['target'], prediction))
#     if max_acc < accuracy_score(data['target'], prediction):
#         max_acc = accuracy_score(data['target'], prediction)
#         best_k = i
#     max_acc = max(max_acc, accuracy_score(data['target'], prediction))

# print(best_k)

knn = KNeighborsClassifier(n_neighbors=3)   
knn.fit(processed_data, data['target'])
data2 = pd.read_csv('hw1-data/income.test.blind.csv', header=0)

# num_processor = 'passthrough' # i.e., no transformation
# cat_processor = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# num_features = ['age', 'hours']
# cat_features = ['country', 'sector', 'edu', 'marriage', 'occupation', 'race', 'sex',]
# preprocessor = ColumnTransformer([('num', num_processor, num_features),
#                                   ('cat', cat_processor, cat_features)
#                                  ])

processed_data = preprocessor.transform(data2)
print(len(preprocessor.get_feature_names_out()))
# processed_data = preprocessor.transform(data2)

prediction = knn.predict(processed_data)


data2['target'] = prediction
data2.to_csv('output.csv', index=False)
