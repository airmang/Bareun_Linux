import sys
import google.protobuf.text_format as tf
from bareunpy import Tagger
from bareunpy import Tokenizer
from collections import defaultdict

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



    #안긴문장 안은문장 메소드
    def embrace(cls):
        #전성 어미 (ETN=명사형, ETM=관형형)
        print(cls.morph_list)
        print(len(cls.morph_list))

        SS_pivot = []
        pivot =[]
        flag = []
        driver = 0
        ter_switch = 0
        embrace_dict = defaultdict(list)
        embrace_result = []
        
        for i in range(len(cls.morph_list)):
            #관형절을 안은 문장
            if cls.morph_list[i][1] == 'ETM':
                ter_switch = 1
                print(cls.morph_list[i], i)
                flag.append(i)
                pivot.append(i)                
        
                while(True):
                    if cls.morph_list[flag[driver]][1] in ['JKB', 'JX'] :
                        for i in range(flag[driver]+1, pivot[driver]+1):
                            print(cls.morph_list[i])
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                    if cls.morph_list[flag[driver]][1] == 'JKS' :
                        for i in range(flag[driver]-1, pivot[driver]+1):
                            print(cls.morph_list[i])
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                    if flag[driver] == 0:
                        flag[driver] = 1
                        for i in range(flag[driver]-1, pivot[driver]+1):
                            print(cls.morph_list[i])
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                    flag[driver] = flag[driver] - 1
                
                driver = driver + 1
            #명사절을 안은 문장
            if cls.morph_list[i][1] == 'ETN':
                ter_switch = 1
                print(cls.morph_list[i], i)
                flag.append(i)
                pivot.append(i)
        
                while(True):
                    if cls.morph_list[flag[driver]][1] in ['JKB', 'JX'] :
                        for i in range(flag[driver]+1, pivot[driver]+1):
                            print(cls.morph_list[i])
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                    if cls.morph_list[flag[driver]][1] == 'JKS':                        
                        for j in range(flag[driver]-1, 0, -1):
                            if cls.morph_list[j][1] == 'JX' or cls.morph_list[j][1] == 'JKS':
                                break
                            
                        for i in range(j+1, pivot[driver]+1):
                            print(cls.morph_list[i])
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                    if flag[driver] == 0:
                        flag[driver] = 1
                        for i in range(flag[driver]-1, pivot[driver]+1):
                            print(cls.morph_list[i])
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                    flag[driver] = flag[driver] - 1
                
                driver = driver + 1

            #부사절을 안은 문장
            
            #인용절을 안은 문장
            #('라고', 'JKQ')를 포함하거나 ('고'로 끝나는 'EC''자고','다고','냐고','라고') 연결어미를 포함할 경우
            if (cls.morph_list[i][1] =='JKQ') or ((cls.morph_list[i][1] == 'EC') and (cls.morph_list[i][0] in ['라고','자고', '다고', '냐고','느냐고', 'ㄴ다고'])):
                ter_switch = 1
                print(cls.morph_list[i], i)
                flag.append(i)
                pivot.append(i)

                while(True):
                    if cls.morph_list[flag[driver]][1] in ['JKB', 'JX'] :
                        for i in range(flag[driver]+1, pivot[driver]+1):
                            print(cls.morph_list[i],1)
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                    if cls.morph_list[flag[driver]][1] == 'JKS' :
                        JKS_FLAG = flag[driver] - 1
                        while(True):
                            if cls.morph_list[JKS_FLAG][1] =='JKS' :
                                for i in range(flag[driver]-1, pivot[driver]+1):
                                    print(cls.morph_list[i],2)
                                    #embrace_result.append(cls.morph_list[i])
                                    embrace_dict[driver].append(cls.morph_list[i][0])
                                break
                            elif JKS_FLAG == 0:
                                flag[driver] = 1
                                for i in range(flag[driver]+1, pivot[driver]+1):
                                    print(cls.morph_list[i],3)
                                    #embrace_result.append(cls.morph_list[i])
                                    embrace_dict[driver].append(cls.morph_list[i][0])
                                break
                            JKS_FLAG = JKS_FLAG - 1
                        break
                    
                    elif flag[driver] == 0:
                        flag[driver] = 1
                        for i in range(flag[driver]-1, pivot[driver]+1):
                            print(cls.morph_list[i],4)
                            #embrace_result.append(cls.morph_list[i])
                            embrace_dict[driver].append(cls.morph_list[i][0])
                        break
                        
                    flag[driver] = flag[driver] - 1
                
                driver = driver + 1

        #서술절을 안은 문장(주어1+(주어2+서술어))
        #(은/는 다음으로 이/가 또는 이/가 다음으로 은/는)(보격조사('JKC')를 포함하면 안된다.)
        #case1: JKS + JKS + NOT(JKC)
        #case2: JKS + JX + NOT(JKC)
        #case3: JX + JKS + NOT(JKC)
        if ter_switch == 0:
            V_check = 0
            JKC_check = 0

            for i in range(len(cls.morph_list)):
                if cls.morph_list[i][1] == 'JKS' or cls.morph_list[i][1] == 'JX' :
                    if cls.morph_list[i][1] == 'JKS':
                        SS_pivot.append(i)
                        for j in range(i+1, len(cls.morph_list)):
                            if cls.morph_list[j][1] in {'VV', 'VA', 'VX', 'VCP', 'VCN'}:
                                V_check = 1
                            if V_check == 0 and cls.morph_list[j][1] in ['JKS', 'JX']:
                                # case 1, case 2 만족                                
                                for k in range(j, len(cls.morph_list)):
                                    if cls.morph_list[k][1] == 'JKC':
                                        JKC_check = 1
                                        break
                                if JKC_check == 0:
                                    print('case 1 or case 2')                                   
                                    for i in range(SS_pivot[driver]+1, len(cls.morph_list)):
                                        print(cls.morph_list[i],4)
                                        #embrace_result.append(cls.morph_list[i])
                                        embrace_dict[driver].append(cls.morph_list[i][0])
                                    driver = driver + 1                                                                
                        break
                    
                    if cls.morph_list[i][1] == 'JX':
                        SS_pivot.append(i)
                        for j in range(i+1, len(cls.morph_list)):
                            if cls.morph_list[j][1] in {'VV', 'VA', 'VX', 'VCP', 'VCN'}:
                                V_check = 1
                            if V_check == 0 and cls.morph_list[j][1] == 'JKS':
                                # case 3 만족
                                for k in range(j, len(cls.morph_list)):
                                    if cls.morph_list[k][1] == 'JKC':
                                        JKC_check = 1
                                        break
                                if JKC_check == 0:
                                    print('case 3')
                                    for i in range(SS_pivot[driver]+1, len(cls.morph_list)):
                                        print(cls.morph_list[i],4)
                                        #embrace_result.append(cls.morph_list[i])
                                        embrace_dict[driver].append(cls.morph_list[i][0])
                                    driver = driver + 1                          
                        break
        #print(list(embrace_dict.values()))            
        return list(embrace_dict.values())


    def message(cls):
        res = tagger.tags([cls.sentence])
        json_res = res.as_json()
        print(json_res)
        for sentence in json_res['sentences']:
            for token in sentence['tokens']:
                for morpheme in token['morphemes']:
                    tag = morpheme['tag']
                    if tag in cls.pos_dict:
                        morpheme['tag'] = cls.pos_dict[tag]
        return json_res

    #어절 단위로 나누는 메소드
    def list(cls):
        res = tagger.tags([cls.sentence])
        m = res.msg()
        #print(m.sentences)
        seg_list = []
        for sent in m.sentences:
            for token in sent.tokens:    
                seg_list.append(token.text.content)
        print(seg_list)
        return seg_list

    def offset(cls):
        res = tagger.tags([cls.sentence])
        m = res.msg()
        print(m.sentences[0].tokens[2].text.begin_offset)

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
    

#관형절을 안은 문장    
S1_1 = morph('누나가 책을 읽은 도서관은 집 근처에 있다.')
S1_2 = morph('산에 이쁜 꽃이 피었다.')
S1_3 = morph('그는 어제 먹다 남은 과자를 버렸다.')
S1_4 = morph('친구는 내일 소풍 갈 장소를 검색했다.')
S1_test1 = morph('우리가 여행 갈 곳을 찾아보자.')
S1_test2 = morph('규현이는 잡고 있던 손을 놓지 않았다.')
#명사절을 안은 문장
S2_1 = morph('나는 등교수업이 재기되기를 바란다.')
S2_2 = morph('우리는 그가 옳았음을 알았다.')
S2_3 = morph('나는 형의 시험이 끝나기를 기다렸다.')
S2_4 = morph('집에 불이 났음을 알았다.')
S2_test1 = morph('당시에 그곳이 공사중이었음을 모르는 사람이 없다.')
#부사절을 안은 문장
S3_1 = morph('영희가 눈물을 철수가 떠나자 흘렸다.')
S3_2 = morph('누군가 소리도 없이 그녀에게 다가왔다.')
S3_3 = morph('진달래가 ')
#서술절을 안은 문장
S4_1 = morph('영희가 키가 크다.')
S4_2 = morph('철수는 키가 작다.')
S4_3 = morph('민수가 키는 작다.')
S4_4 = morph('철수가 대학생이 되었다.')
S4_5 = morph('영희는 범인이 아니다.')
S4_test1 = morph('거북이가 걸음이 느리다.')
S4_test2 = morph('토끼는 거북이가 아니다.')
S4_test3 = morph('용왕님은 옷이 화려하다.')
#인용절을 안은 문장
S5_1 = morph('찰수가 얼른 가라고 했어.')
S5_2 = morph('철수가 영희가 좋다고 말했다.')
S5_3 = morph('민수는 내게 친구들의 이름을 다 아느냐고 물었다.')
S5_4 = morph('철수는 영희가 온다는 사실을 알았다.')
S5_test1 = morph('얼른 진도를 나가자고 제안했다.')

S_test1 = morph('플래시는 정말 빠르다.')
S_test2 = morph('가오갤에서 제일 좋아하는 캐릭터는 그루트다.')

#S_test1.message()
#S_test1.offset()

S1_1.embrace()
S1_2.embrace()
S1_3.embrace()
S1_4.embrace()
S1_test1.embrace()
S1_test2.embrace()

S2_1.embrace()
S2_2.embrace()
S2_3.embrace()
S2_4.embrace()
S2_test1.embrace()

S3_1.embrace()
S3_2.embrace()

S4_1.embrace()
S4_2.embrace()
S4_3.embrace()
S4_4.embrace()
S4_5.embrace()
S4_test1.embrace()
S4_test2.embrace()
S4_test3.embrace()

S5_1.embrace()
S5_2.embrace()
S5_3.embrace()
S5_4.embrace()
S5_test1.embrace()

#S_test1.embrace()
#S_test2.message()
#S_test2.embrace()

#P1 = morph('안녕 나의 사랑')
#P1.list()

#P1 = tokenize('철수는 영희가 온다는 사실을 알았다.')


