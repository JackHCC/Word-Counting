# 中文小说词频统计及正则匹配

### 首先导入中文分词库jieba，Counter库和re库
```
import jieba
import re
from collections import Counter
```

###导入打开要处理的文本傲慢与偏见中文版小说并利用jieba分词
```
txt = open("傲慢与偏见.txt", "r", encoding="gb18030").read()
words = jieba.lcut(txt)
```

