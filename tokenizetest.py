import sys
import google.protobuf.text_format as tf
from bareunpy import Tokenizer

API_KEY="koba-YEVHS7Q-VDSUWIY-XCIS3OQ-LWD7WHA"
# If you have your own localhost bareun.
tokenizer = Tokenizer(API_KEY, 'localhost')


# print results. 
tokenized = tokenizer.tokenize_list(["철수는 영희가 온다는 사실을 알았다.", "영희는 철수가 온다는 사실을 몰랐다."])

# get protobuf message.
m = tokenized.msg()
tf.PrintMessage(m, out=sys.stdout, as_utf8=True)
print(tf.MessageToString(m, as_utf8=True))
print(f'length of sentences is {len(m.sentences)}')
## output : 2
print(f'length of tokens in sentences[0] is {len(m.sentences[0].tokens)}')
print(f'length of segments of first token in sentences[0] is {len(m.sentences[0].tokens[0].segments)}')
print(f'tagged of first token in sentences[0] is {m.sentences[0].tokens[0].tagged}')
print(f'first segment of first token in sentences[0] is {m.sentences[0].tokens[0].segments[0]}')
print(f'hint of first morph of first token in sentences[0] is {m.sentences[0].tokens[0].segments[0].hint}')

## Advanced usage.
for sent in m.sentences:
    for token in sent.tokens:
        for m in token.segments:
            print(f'{m.text.content}/{m.hint}')

# get json object
jo = tokenized.as_json()
print(jo)

# get tuple of segments
ss = tokenized.segments()
print(ss)
ns = tokenized.nouns()
print(ns)
vs = tokenized.verbs()
print(vs)
# postpositions: 조사
ps = tokenized.postpositions()
print(ps)
# Adverbs, 부사
ass = tokenized.adverbs()
print(ass)
ss = tokenized.symbols()
print(ss)
