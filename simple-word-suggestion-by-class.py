import numpy as np

class Tf_Idf:
    def __init__(self):
        self._clean_lines = []
        self._word = ""
    
    def get_clean_lines(self, clean_lines):
        self._clean_lines = clean_lines

    def get_word(self, word):
        self._word = word

    def preprocess_lines (self):
        self._preprocessed_lines = []
        for self._line in self._clean_lines:
            self._preprocessed_line = self._line.replace(",", " ").replace("."," ").replace("(", " ").replace(")", " ").replace("-","")
            self._preprocessed_line  = self._preprocessed_line.lower().split()
            self._preprocessed_lines.append(self._preprocessed_line)
        return self._preprocessed_lines
    
    def count_words_in_lines (self):
        self._countered_lines = []
        for self.c_line in self._preprocessed_lines:
            self._countered_line = {}
            for self._word in self.c_line:
                if self._word in self._countered_line and self._word.isalpha():
                    self._countered_line[self._word] +=1
                else:
                    self._countered_line[self._word] = 1
            self._countered_lines.append(self._countered_line)
        return self._countered_lines

    def inverse_doc_freq (self):
        self.contained_word = 0
        for self._idf_line in self._preprocessed_lines:
            if self._word in self._idf_line:
                self.contained_word +=1
            else: pass
        if self.contained_word == 0: return None
        self.idf = np.log(len(self._preprocessed_lines)/self.contained_word)
        return self.idf
    
    def term_freq (self):
        self._tf_word = []
        for self._tf_line in self._countered_lines:
            self.__num_word = self._tf_line.get(self._word,0)
            self.__num_word_line = [i for _,i in self._tf_line.items()]
            self._tf_word_in_line = self.__num_word / sum(self.__num_word_line)
            self._tf_word.append(self._tf_word_in_line)
        return self._tf_word
    
    def tf_idf_calculate (self):
        self._tf_idf = np.array(self.term_freq()) * self.inverse_doc_freq()
        return self._tf_idf
    
    def __call__ (self):
        self.preprocess_lines()
        self.count_words_in_lines()
        self.inverse_doc_freq()
        self.term_freq()
        self.tf_idf_calculate()
class Suggested_Word (Tf_Idf):
    def __init__ (self):
        super.__init__(self)
    
    def get_clean_lines(self, clean_lines):
        super().get_clean_lines(clean_lines)
    
    def get_word(self, word):
        super().get_word(word)
    
    def 

    
test = Tf_Idf()
with open("./data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    test.get_clean_lines(lines)
    test.get_word("the")
    test()
    print(test.tf_idf_calculate())







