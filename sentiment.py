from pythainlp.corpus import thai_words
from pythainlp import word_tokenize,Tokenizer
from sklearn.metrics import classification_report

positive_vocab = []
negative_vocab = []
swear_words = []
neutral_vocab = []

with open("neg.txt", 'r',encoding="utf8") as f:
    for line in f:
        negative_vocab.append(line.rstrip())

with open("pos.txt", 'r',encoding="utf8") as f:
    for line in f:
        positive_vocab.append(line.rstrip())
        
with open("swear-words.txt", 'r',encoding="utf8") as f:
    for line in f:
        swear_words.append(line.rstrip())

with open("neu.txt", 'r',encoding="utf8") as f:
    for line in f:
        neutral_vocab.append(line.rstrip())

sentences = input("insert thai text ")

pythainlp_words = thai_words()
custom_dict = ["ลุงตู่"]
dictionary = list(pythainlp_words) + custom_dict
tok = Tokenizer(dictionary)

tokens = []
tokens = tok.word_tokenize(sentences)
tokens = ' '.join(tokens)
tokens = [tokens]

for sentence in tokens:
    pos = 0
    neu = 0
    neg = 0
    pred = []
    print(sentence)
    words = sentence.split(' ')
    for word in words:
        if word in positive_vocab:
            pred.append("pos")
            pos = pos + 1
        elif word in negative_vocab or word in swear_words:
            pred.append("neg")
            neg = neg + 1
        elif word in neutral_vocab:
            pred.append("neu")
            neu = neu + 1
        else:
            pred.append("neu")
            neu = neu + 1

    if pos > neg and pos > neu:
        print('positive')
    elif neg > pos and neg > neu:
        print('negative')
    elif neu > pos and neu > neg:
        print('neutral')
    elif pos == neg or neg == neu or pos == neu:
        print ('neutral')

y_true = ["neu","neu","neg"]
print(pred)
print(classification_report(y_true = y_true,y_pred = pred))
