from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

#column_names = ["id", "age", "sector", "edu", "marriage", "occupation", "race", "sex", "hours", "country", "target"]
train_data = pd.read_csv("../hw1-data/income.dev.csv", header=0)
dev_data = pd.read_csv("../hw1-data/income.dev.csv", header=0)
#train_data = pd.concat([train_data, dev_data], axis=0)
# train_data['age'] = pd.to_numeric(train_data['age'], errors='coerce')
# train_data['hours'] = pd.to_numeric(train_data['hours'], errors='coerce')
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
new_data = train_data.drop(['id', 'target'], axis=1, inplace=False)
encoder.fit(new_data)
new_data = encoder.transform(new_data)
print(len(encoder.get_feature_names_out()))

blind_data = pd.read_csv('../hw1-data/income.test.blind.csv', header=0)
test_data = encoder.transform(blind_data.drop(['id'], axis=1, inplace=False))
knn = KNeighborsClassifier(n_neighbors=69)
knn.fit(new_data, train_data['target'])
prediction = knn.predict(test_data)
blind_data['target'] = prediction
blind_data.to_csv('output_n.csv', index=False)


# dev_data['age'] =  pd.to_numeric(dev_data['age'], errors='coerce')
# dev_data['hours'] = pd.to_numeric(dev_data['hours'], errors='coerce')
num_processor = MinMaxScaler(feature_range=(0, 10))
cat_processor = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

num_columns = ['age', 'hours']
cat_columns = ['sector', 'edu', 'marriage', 'occupation', 'race', 'sex', 'country',]



preprocessor = ColumnTransformer([
           ('hours', MinMaxScaler(feature_range=(0, 10)), ['hours']),
           ('age', MinMaxScaler(feature_range=(0, 2)), ['age']),
           ('cat', cat_processor, cat_columns)
       ])

preprocessor.fit(train_data)
print(len(preprocessor.get_feature_names_out()))

train_num_cat_bin_data = preprocessor.transform(train_data)
dev_num_cat_bin_data = preprocessor.transform(dev_data)
feature_dimension_size = train_num_cat_bin_data.shape[1]


print("Feature dimension size:", len(preprocessor.get_feature_names_out()))

for i in range(1, 100, 2):


    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_num_cat_bin_data, train_data['target'])
    score = 1 - knn.score(train_num_cat_bin_data, train_data['target'])
    print(i, score)


# # print data stats
# print("Data Shapes --------------------------------------")
# print("X_train\t\tX_test\t\ty_train\t\ty_test")
# print("{}\t{}\t{}\t{}\n".format(X_train.shape, X_test.shape, y_train.shape, y_test.shape))

# print(len(X_train[0]))
# print(len(y_train[0]))
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(train_num_cat_bin_data, train_data['target'])

blind_data = pd.read_csv('../hw1-data/income.test.blind.csv')

processed_blind_data = preprocessor.transform(blind_data)

prediction = knn.predict(processed_blind_data)
blind_data['target'] = prediction
blind_data.to_csv('output_new.csv', index=False)

        # train_error = 1 - knn_classifier.score(X_train, y_train)
# preprocessor.get_feature_names_out()
# data.drop(['id', 'target'], axis=1, inplace=True)
# data2 = data[['age', 'sector']]


# encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
# encoder.fit(data2)
# binary_data = encoder.transform(data2)

#num_processor = MinMaxScaler(feature_range=(0, 10))
#num_processor = 'passthrough'
# cat_processor = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# preprocessor = ColumnTransformer([
#            ('num', num_processor, ['age', 'hours']),
#            ('cat', cat_processor, ['sector', 'edu', 'occupation', 'sex', 'country', 'race', 'marriage'])
#        ])
# preprocessor = ColumnTransformer([
#            ('num', num_processor, ['age']),
#            ('cat', cat_processor, ['sector',])
#        ])

# preprocessor.fit(data)
# print(len(preprocessor.get_feature_names_out()))
# processed_data = preprocessor.transform(data)




# knn = KNeighborsClassifier(n_neighbors=7)
# knn.fit(processed_data, data['target'])

# test_data = pd.read_csv('hw1-data/income.test.blind.csv', header=0)
# processed_test_data = preprocessor.transform(test_data)
# pred = knn.predict(processed_test_data)
# test_data['target'] = pred
# test_data.to_csv('output3.csv', index=False)
