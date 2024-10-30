import collections
import pandas as pd
import sys

def write_filtered_file(target_file_name: str, corpus: pd.DataFrame, counter: collections.Counter):
    with open(target_file_name, 'w') as f:
            f.write("id,sentence,target\n")
            for i, row in corpus.iterrows():
                sentence_id = row['id']
                words = row['sentence'].split()
                new_words = f'"{" ".join([word for word in words if counter[word] > 1])}"'
                label = row['target']
                s = f"{sentence_id},{new_words},{label}\n"
                f.write(s)
    
    f.close()


def remove_one_count_words(file_name: str):

    data = pd.read_csv(file_name)
    word_counts = collections.Counter()
    for index, row in data.iterrows():
        words = row['sentence']
        for word in words.split():
            word_counts[word] += 1

    write_filtered_file(f"filtered.{file_name}", data, word_counts)

if __name__ == "__main__":
    remove_one_count_words(sys.argv[1])
 