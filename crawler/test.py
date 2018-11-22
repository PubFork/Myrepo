import jieba
from redis import Redis
import simplejson



redis = Redis('192.168.0.18')
stopwords = set()
with open(r'C:\Users\Administrator\Desktop\selfpro\chineseStopWords.txt','r',encoding='gbk') as f:
    for line in f:
        word = line.rstrip('\r\n')
        stopwords.add(word)

print(len(stopwords))
items = redis.lrange('doubanbook:items',0,-1)

words = {}
for item in items:
    val = simplejson.loads(item)["comment"]
    for word in jieba.cut(val):
        words[word] = words.get(word,0)+1
print(len(words))
print(sorted(words.items(),key=lambda x:x[1],reverse=True))

words = {}
for item in items:
    val = simplejson.loads(item)["comment"]
    for word in jieba.cut(val):
        if word not in stopwords:
            words[word] = words.get(word,0)+1

print(len(words))
print(sorted(words.items(),key=lambda x:x[1],reverse=True))


total = len(words)
frenq = {k:v/total for k,v in words.items()}
print(frenq)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(font_path='simhei.ttf',background_color='white',max_font_size=80)

plt.figure(2)
wordcloud.fit_words(frenq)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()