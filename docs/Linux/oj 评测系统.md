# oj 评测系统

```bash
# 编译并运行 <in.txt >run.txt
oj -cr name.lang

# 编译并运行 无重定向要求
oj -ocr name.lang

# 编译
oj -c name.lang
oj -oc name.lang

# 运行 <in.txt >run.txt
oj -r name.lang

# 运行 无重定向要求
oj -or name.lang

# 特殊定义，有特殊重定向要求
# Random >in.txt
# Answer <in.txt >out.txt
oj -cr Random.lang
oj -cr Answer.lang

# 对拍 n 次
# Random.lang1 Answer.lang2 Main.lang3
oj -j n lang1 lang2 lang3
# Random.cpp Answer.cpp Main.cpp
oj -j n

# 获取一次样例组
# Random.lang1 Answer.lang2
oj -s lang1 lang2
# Random.cpp Answer.cpp
oj -s

# 获取 n 个样例组
# Random.lang1 Answer.lang2
oj -n n lang1 lang2
# Random.cpp Answer.cpp
oj -n n
# 默认 10 个
oj -n 

# 以样例组中的前 n 个样例作为输入运行，并对拍
# Main.lang
oj -a n lang
# Main.cpp
oj -a n
# 默认前 10 个样例组Main.cpp
oj -a
```
