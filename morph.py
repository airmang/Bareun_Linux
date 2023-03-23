import sys
import google.protobuf.text_format as tf
from bareunpy import Tagger

#initiate bareun
API_KEY="koba-YEVHS7Q-VDSUWIY-XCIS3OQ-LWD7WHA"
tagger = Tagger(API_KEY, 'localhost')

class morph:
    def __init__(self, sentence):
        self.sentence = sentence

    def termination(cls):
        termination_keys = {'EP', 'EF', 'EC', 'ETN', 'ETM'}
        result = tagger.tags([cls.sentence])
        morph_list = result.pos()
        filtered = [t for t in morph_list if t[1] in termination_keys]
        #print(filtered)
        return filtered

#S1 = morph('봄이오면 벚꽃을 보러가요.')
#S1.termination()


