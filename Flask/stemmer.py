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
        self.result = tagger.tags([sentence])           
        self.morph_list = self.result.pos()
    pos_dict = {'NNG': '일반 명사', 'NNP': '고유 명사', 'NNB': '의존 명사', 'NP': '대명사', 'NR': '수사', 'NF': '명사 추정 범주', 'NA': '분석불능범주', 'NV': '용언 추정 범주', 
                 'VV': '동사', 'VA': '형용사', 'VX': '보조 용언', 'VCP': '긍정 지정사', 'VCN': '부정 지정사', 
                 'MMA': '성상 관형사', 'MMD': '지시 관형사', 'MMN': '수 관형사', 'MAG': '일반 부사', 'MAJ': '접속 부사', 
                 'IC': '감탄사', 'JKS': '주격 조사', 'JKC': '보격 조사', 'JKG': '관형격 조사', 'JKO': '목적격 조사', 'JKB': '부사격 조사', 'JKV': '호격 조사', 'JKQ': '인용격 조사', 'JX': '보조사', 'JC': '접속 조사', 
                 'EP': '선어말 어미', 'EF': '종결 어미', 'EC': '연결 어미', 'ETN': '명사형 전성 어미', 'ETM': '관형형 전성 어미', 
                 'XPN': '체언 접두사', 'XSN': '명사 파생 접미사', 'XSV': '동사 파생 접미사', 'XSA': '형용사 파생 접미사', 'XR': '어근', 
                 'SF': '마침표,물음표,느낌표', 'SP': '쉼표,가운뎃점,콜론,빗금', 'SS': '따옴표,괄호표,줄표', 'SE': '줄임표', 'SO': '붙임표(물결,숨김,빠짐)', 'SW': '기타기호 (논리수학기호,화폐기호)', 'SL': '외국어', 'SH': '한자', 'SN': '숫자'}


    def message(cls):
        res = tagger.tags([cls.sentence])
        return res.as_json()

    #어절 단위로 나누는 메소드
    def list(cls):
        res = tagger.tags([cls.sentence])
        m = res.msg()
        #print(m.sentences)
        seg_list = []
        for sent in m.sentences:
            for token in sent.tokens:    
                seg_list.append(token.text.content)
        return seg_list

    #체언 추출
    def substantives(cls):
        substantives_keys = {'NNG', 'NNP', 'NNB', 'NP', 'NR'}
        filtered = [t for t in cls.morph_list if t[1] in substantives_keys]
        new_list = [(x[0], cls.pos_dict[x[1]]) if x[1] in cls.pos_dict else x for x in filtered]
        print(cls.morph_list)
        print(new_list)
        return new_list

    #용언 추출
    def predicates(cls):
        termination_keys = {'VV', 'VA', 'VX', 'VCP', 'VCN'}
        filtered = [t for t in cls.morph_list if t[1] in termination_keys]
        new_list = [(x[0], cls.pos_dict[x[1]]) if x[1] in cls.pos_dict else x for x in filtered]
        print(cls.morph_list)
        print(new_list)
        return new_list

    #관계언 추출
    def relative(cls):
        termination_keys = {'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC'}
        filtered = [t for t in cls.morph_list if t[1] in termination_keys]
        new_list = [(x[0], cls.pos_dict[x[1]]) if x[1] in cls.pos_dict else x for x in filtered]
        print(cls.morph_list)
        print(new_list)
        return new_list

    #수식언 추출
    def modifier(cls):
        termination_keys = {'MMA', 'MMD', 'MMN', 'MAG', 'MAJ'}
        filtered = [t for t in cls.morph_list if t[1] in termination_keys]
        new_list = [(x[0], cls.pos_dict[x[1]]) if x[1] in cls.pos_dict else x for x in filtered]
        print(new_list)
        return new_list

    #어미 추출
    def termination(cls):
        termination_keys = {'EP', 'EF', 'EC', 'ETN', 'ETM'}
        filtered = [t for t in cls.morph_list if t[1] in termination_keys]
        new_list = [(x[0], cls.pos_dict[x[1]]) if x[1] in cls.pos_dict else x for x in filtered]
        print(cls.morph_list)
        print(new_list)
        return new_list

class tokenize:
    def __init__(self, sentence):
        self.sentence = sentence        

    #형태소 단위로 나누는 메소드    
    def list(cls):
        tokenized = tokenizer.tokenize_list([cls.sentence])
        ss = tokenized.segments()
        print(ss)
        return ss
    
    
S1 = morph('철수는 영희가 온다는 사실을 알았다.')
S1.substantives()
P1 = tokenize('철수는 영희가 온다는 사실을 알았다.')


