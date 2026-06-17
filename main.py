import numpy as np

def preprocess_text(file_path) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        clean_lines = []
        for line in lines:
            preprocessed_line = line.replace(",", " ").replace("."," ").replace("(", " ").replace(")", " ").replace("-","")
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

def term_frequency (word: str, list_count_word: list) -> list:
    '''TF = (Number of times the term appears in the document) / (Total number of terms in the document)'''
    tf_word = []
    for line in list_count_word:
        num_word = line.get(word,0)
        num_word_line = [ i for _,i in line.items()]
        tf_line = num_word /sum(num_word_line)
        tf_word.append(tf_line)
    return tf_word

def tf_idf (word: str, clean_line: list, counted_line: list) -> list:
    tf = np.array(term_frequency(word, counted_line))
    idf = inverse_doc_frequency(word, clean_line)
    #print(f"TF: {tf}")
    #print(f"IDF: {idf}")
    tf_idf = tf * idf
    tf_idf_list = tf_idf.tolist()
    return tf_idf_list

def suggested_line (word: str, cleaned_list: list, counted_list: list, data: list) -> str:
    tf_idf_list = tf_idf(word, cleaned_list, counted_list)
    max = 0
    idx_max = -1
    for idx, value in enumerate(tf_idf_list):
        if value > max: 
            idx_max = idx
            max = value
    print(max)
    print(idx_max)
    print(data[idx_max])
    print(tf_idf_list)



#===================MAIN======================================
file_path = r".\word_suggestion\data.txt"
clean_lines = preprocess_text(file_path)
counted_list = count_word(clean_lines)
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    suggested_line('boiling',clean_lines,counted_list, lines)