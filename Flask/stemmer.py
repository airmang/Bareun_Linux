import sys
import google.protobuf.text_format as tf
from bareunpy import Tagger
from bareunpy import Tokenizer

#initiate bareun
API_KEY="koba-YEVHS7Q-VDSUWIY-XCIS3OQ-LWD7WHA"
tagger = Tagger(API_KEY, 'localhost',5656)
tokenizer = Tokenizer(API_KEY, 'localhost',5656)

class morph:
    def __init__(self, sentence):
        self.sentence = sentence

    def list(cls):
        res = tagger.tags([cls.sentence])
        m = res.msg()
        print(m.sentences)
        for sent in m.sentences:
            for token in sent.tokens:                
                print(token.text.content)
            #print(m.sentences[0].tokens[0].lemma)

    def termination(cls):
        termination_keys = {'EP', 'EF', 'EC', 'ETN', 'ETM'}
        result = tagger.tags([cls.sentence])           
        morph_list = result.pos()
        filtered = [t for t in morph_list if t[1] in termination_keys]
        
        print(filtered)
        return filtered

class tokenize:
    def __init__(self, sentence):
        self.sentence = sentence        
        
    def list(cls):
        tokenized = tokenizer.tokenize_list([cls.sentence])
        ss = tokenized.segments()

        print(tokenizer.seg(cls.sentence))
        print(ss)
        print(tokenized.print_as_json())
        return ss
    
S1 = morph('철수는 영희가 온다는 사실을 알았다.')
S1.list()
P1 = tokenize('철수는 영희가 온다는 사실을 알았다.')
#P1.list()



