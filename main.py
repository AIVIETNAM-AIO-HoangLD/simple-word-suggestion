import numpy as np
def preprocess_text(file_path) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        clean_lines = []
        for line in lines:
            preprocessed_line = line.replace(",", " ").replace("."," ").replace("(", " ").replace(")", " ")
            preprocessed_line = preprocessed_line.lower().split()
            clean_lines.append(preprocessed_line)
    return clean_lines

def count_word(lines: list) -> list:
    counter_lines = []
    for line in lines:
        counter_line = {}
        for word in line:
            if word in counter_line and word.isalpha():
                counter_line[word] +=1
            else:
                counter_line[word] = 1
        counter_lines.append(counter_line)
    return counter_lines

def inverse_doc_frequency (word: str, preprocessed_lines: list) -> float:
    '''IDF = log(Total number of documents / Number of documents containing the term)'''
    contained_word = 0
    for line in preprocessed_lines:
        if word in line:
            contained_word = contained_word + 1
        else: pass
    if contained_word == 0: return None
    result = np.log(len(preprocessed_lines) / contained_word)
    return result

def term_frequency (word: str, words: list) -> float:
    '''TF = (Number of times the term appears in the document) / (Total number of terms in the document)'''
    counter_words = count_word(words)
    num_word = count_word.get(word,0)
    tf_word = num_word/len(counter_words)
    return tf_word

def tf_idf (word: str, data: list) -> dict:
    tf_idf_word = {}
    idf = inverse_doc_frequency(word, data)
    for words in data:
        tf_idf_word[word] = term_frequency(word, words) * idf
    return tf_idf


#===================MAIN======================================
file_path = r".\word_suggestion\data.txt"
clean_lines = preprocess_text(file_path)
print(inverse_doc_frequency("this",clean_lines))
    #print(inverse_doc_frequency(r"the",clean_text))
