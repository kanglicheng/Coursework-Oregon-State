from __future__ import division
from collections import defaultdict
import sys
import time
import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MaxAbsScaler
from sklearn.metrics import accuracy_score

# Assuming svector is a custom class or function you have that works like a sparse vector
from svector import svector


def read_data(textfile):
    data = []
    for line in open(textfile):
        label, words = line.strip().split("\t")
        data.append((1 if label == "+" else -1, words.split()))
    return data


def count_words(data):
    word_counts = defaultdict(int)
    for _, words in data:
        for word in words:
            word_counts[word] += 1
    return word_counts


def make_vector(words, word_counts, bias=True):
    v = svector()
    for word in words:
        if word in word_counts:
            v[word] += 1
    if bias:
        v['<bias>'] = 1
    return v


def prune_features(word_counts, min_count=2):
    return {word: count for word, count in word_counts.items() if count >= min_count}


def vector_to_nparray(vectors, vocabulary):
    X = np.zeros((len(vectors), len(vocabulary)))
    for i, vector in enumerate(vectors):
        for word, value in vector.items():
            if word in vocabulary:
                X[i, vocabulary[word]] = value
    return X


def logistic_regression(train_data, dev_data, word_counts):
    pruned_word_counts = prune_features(word_counts)
    vocabulary = {word: idx for idx, word in enumerate(pruned_word_counts.keys())}

    X_train = vector_to_nparray([make_vector(words, pruned_word_counts) for _, words in train_data], vocabulary)
    y_train = np.array([label for label, _ in train_data])
    X_dev = vector_to_nparray([make_vector(words, pruned_word_counts) for _, words in dev_data], vocabulary)
    y_dev = np.array([label for label, _ in dev_data])

    scaler = MaxAbsScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_dev_scaled = scaler.transform(X_dev)

    model = LogisticRegression(max_iter=200)
    start_time = time.time()
    model.fit(X_train_scaled, y_train)

    y_dev_pred = model.predict(X_dev_scaled)
    accuracy = accuracy_score(y_dev, y_dev_pred) * 100
    print(100 - accuracy)
    print("Training time",time.time() - start_time)

    return vocabulary, model, scaler


def get_predicted(test_file, vocabulary, model, scaler, output_file):
    test_data = read_data(test_file)
    X_test = vector_to_nparray([make_vector(words, vocabulary) for _, words in test_data], vocabulary)
    X_test_scaled = scaler.transform(X_test)

    predictions = model.predict(X_test_scaled)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        for (label, words), pred in zip(test_data, predictions):
            writer.writerow(['+' if pred == 1 else '-', ' '.join(words)])

            
            

if __name__ == "__main__":
    train_file = 'train.txt'
    dev_file = 'dev.txt'
    test_file = 'test.txt'
    output_file = 'test.txt.predicted'

    train_data = read_data(train_file)
    dev_data = read_data(dev_file)
    word_counts = count_words(train_data)

    vocabulary, model, scaler = logistic_regression(train_data, dev_data, word_counts)
    get_predicted(test_file, vocabulary, model, scaler, output_file)