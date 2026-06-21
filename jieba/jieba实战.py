# encoding=utf-8
import jieba
jieba.initialize()  # 手动初始化jieba资源，提高分词效率。
# 启动paddle模式。 0.40版之后开始支持，早期版本不支持,
#jieba.enable_paddle()
seg_list = jieba.cut("我来到北京南站北广场西路东口",use_paddle=True) # 使用paddle模式
print("Paddle模式: " + '/'.join(list(seg_list)))
seg_list = jieba.cut("我来到北京南站北广场西路东口", cut_all=True)
print("全模式: " + "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut("我来到北京南站北广场西路东口", cut_all=False)
print("精确模式: " + "/ ".join(seg_list))  # 精确模式
seg_list = jieba.cut("我来到北京南站北广场西路东口")  # 默认是精确模式
print("默认是精确模式："+"/ ".join(seg_list))
seg_list = jieba.cut_for_search("我来到北京南站北广场西路东口")  # 搜索引擎模式
print("搜索引擎模式, "+"/".join(seg_list))
