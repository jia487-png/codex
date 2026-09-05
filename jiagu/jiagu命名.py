import jiagu
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
text = '全国绿化委员会'
words = jiagu.cut(text)  # 分词
print('‘全国绿化委员会’的分词结果：'+ '/'.join(words))
ner = jiagu.ner(words)  # 命名实体识别
print('‘全国绿化委员会’的实体名称识别：'+ '/'.join(ner))