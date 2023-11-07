# oj 评测系统

```bash
#!/bin/bash

## 运行并评测 Main.language 文件
## in.txt 作为输入，run.txt 作为输出，out.txt 作为答案
oj -cr Main.language

## 正常编译并运行 Main.language 文件
oj -ocr Main.language

## 多线程编译文件
oj -c file1.language file2.language file3.language ...

## 运行，in.txt 作为输入, run.txt 作为输出
oj -r Main.language

## 正常运行
oj -or Main.language

## 特殊的，无输入文件，只重定向输出到 in.txt
oj -cr Random.language

## 特殊的，以 in.txt 作为输入，输出到 run.txt 文件中
oj -cr Answer.language

## 对拍 100 次
## 将 Random.language1, Answer.language2, Main.language3 互相对拍 100 次
## 其中，默认状态下，language1、language2、language3 都是 cpp
oj -j 100 language1 language2 language3

## 硬性要求
language 后缀只能是：
    
    cpp 、java、py
    
## 获取一次样例
## 使用 Random.language1、Answer.language2 来获取一次样例
oj -s language1 language2

## 获取 10 个样例
## 样例需要放入 data 文件夹中
## 第 i 个样例组应该以：in_i.in、out_i.out 的格式命名
oj -n 10
```

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

# 以样例组作为输入运行，并对拍
# Main.lang
oj -a lang
# Main.cpp
oj -a
```
