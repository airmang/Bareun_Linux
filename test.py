import sys
import google.protobuf.text_format as tf
from bareunpy import Tagger

#
# you can API-KEY from https://bareun.ai/
#
API_KEY="koba-YEVHS7Q-VDSUWIY-XCIS3OQ-LWD7WHA"

# If you have your own localhost bareun.
tagger = Tagger(API_KEY, 'localhost')
# or if you have your own bareun which is running on 10.8.3.211:15656.


# print results. 
res = tagger.tags(["철수는 영희가 온다는 사실을 알았다."])

# get protobuf message.
m = res.msg()
tf.PrintMessage(m, out=sys.stdout, as_utf8=True)
print(tf.MessageToString(m, as_utf8=True))
print(f'length of sentences is {len(m.sentences)}')
## output : 2
print(f'length of tokens in sentences[0] is {len(m.sentences[0].tokens)}')
print(f'length of morphemes of first token in sentences[0] is {len(m.sentences[0].tokens[0].morphemes)}')
print(f'lemma of first token in sentences[0] is {m.sentences[0].tokens[0].lemma}')
print(f'first morph of first token in sentences[0] is {m.sentences[0].tokens[0].morphemes[0]}')
print(f'tag of first morph of first token in sentences[0] is {m.sentences[0].tokens[0].morphemes[0].tag}')

## Advanced usage.
for sent in m.sentences:
    for token in sent.tokens:
        for m in token.morphemes:
            print(f'{m.text.content}/{m.tag}:{m.probability}:{m.out_of_vocab}')

# get json object
jo = res.as_json()
print(jo)

# get tuple of pos tagging.
pa = res.pos()
print(pa)
# another methods
ma = res.morphs()
print(ma)
na = res.nouns()
print(na)
va = res.verbs()
print(va)

