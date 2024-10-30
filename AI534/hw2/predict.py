from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
import time
import pandas as pd
from scipy.stats import uniform, randint
import xgboost as xgb

def read_from_yield(textfile):
    data = pd.read_csv(textfile)
    for idx, line in data.iterrows():
        id, words, label = line['id'], line['sentence'].split(), line['target']
        yield (1 if label=="+" else 0, words, id)

def read_from(textfile):
    data = pd.read_csv(textfile)
    sentences, signs = [], []
    for idx, line in data.iterrows():
        if not line['sentence'] or pd.isna(line['sentence']):
            continue
        id, words, label = line['id'], line['sentence'].split(), line['target']
        sentences.append(' '.join(words))
        signs.append(1 if label == "+" else 0)
    return sentences, signs

# def read_from(textfile):
#     word, sign = [], []
#     for line in open(textfile):
#         label, words = line.strip().split("\t")
#         sign.append(1 if label == "+" else -1)
#         word.append(' '.join(words.split()))
#     print(word, sign)
#     return word, sign

def train(trainfile, devfile):
    t = time.time()
    word_train, sign_train = read_from(trainfile)
    word_dev, sign_dev = read_from(devfile)

    #vectorizer = CountVectorizer(min_df=2, token_pattern=r"\b\w{2,}\b", ngram_range=(1, 2))
    vectorizer = TfidfVectorizer(min_df=2, token_pattern=r"\b\w{2,}\b", ngram_range=(1, 2))
    word_train = vectorizer.fit_transform(word_train)
    word_dev_Bi = vectorizer.transform(word_dev)
    
    # Increase the max_iter parameter
    # Hyperparameter tuning using Grid Search
    # param_dist = {
    #     'C': uniform(0.1, 50),
    #     'solver': [ 'liblinear' ],
    #     'penalty': [ 'l2', 'l1']
    # }
    #model = RandomizedSearchCV(LogisticRegression(max_iter=3000), param_distributions=param_dist, n_iter=50, cv=10, scoring='accuracy', n_jobs=-1, random_state=55)
    # param_dist = {
    #     'C': uniform(1, 30),
    #     'kernel': ['linear', 'sigmoid'],
    #     'gamma': ['scale', 'auto']
    # }
    # model = RandomizedSearchCV(SVC(), param_distributions=param_dist, n_iter=20, cv=5, scoring='accuracy', n_jobs=-1, random_state=55)
    param_dist = {
        'n_estimators': randint(50, 500),
        'max_depth': randint(3, 10),
        'learning_rate': uniform(0.01, 0.3),
        'subsample': uniform(0.7, 1.0),
        'colsample_bytree': uniform(0.7, 1.0)
    }
    model = RandomizedSearchCV(xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss'), param_distributions=param_dist, n_iter=50, cv=5, scoring='accuracy', n_jobs=-1, random_state=55)
    model.fit(word_train, sign_train)

    sign_pred = model.predict(word_dev_Bi)
    accuracy = accuracy_score(sign_dev, sign_pred) * 100
   # print(f"Accuracy on the development set: {accuracy:.2f}%")
    print(100 - accuracy)

    # Predict on test data
    test_data = pd.read_csv("test.csv")
    test_words = test_data['sentence'].fillna('')
    test_transformed = vectorizer.transform(test_words)
    test_predictions = model.predict(test_transformed)

    test_predictions = ["+" if pred == 1 else "-" for pred in test_predictions]

    # Add predictions to test_data and save to CSV
    test_data['target'] = test_predictions
    test_data.to_csv("test_predictions.csv", index=False)

    print("time: %.1f secs" % (time.time() - t))
    return model

train("filtered.train.csv", "filtered.dev.csv")
