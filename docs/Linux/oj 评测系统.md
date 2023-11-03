# oj 评测系统

```bash
#!/bin/bash

## 运行并评测 Main.language 文件
## in.txt 作为输入，run.txt 作为输出，out.txt 作为答案
oj Main.language

## 编译 Main.language 文件
cp Main.language

## 运行，in.txt 作为输入, run.txt 作为输出
rn Main.language

## 特殊的，无输入文件，只重定向输出到 in.txt
oj Random.language

## 特殊的，以 in.txt 作为输入，输出到 run.txt 文件中
oj Answer.language

## 对拍 100 次
## 将 Random.language1, Answer.language2, Main.language3 互相对拍 100 次
## 其中，默认状态下，language1、language2、language3 都是 cpp
oj 100 language1 language2 language3

## 硬性要求
language 后缀只能是：
    
    cpp 、java、py
    
## 获取一次样例
## 使用 Random.language1、Answer.language2 来获取一次样例
oj one language1 language2

## 获取 10 个样例
## 样例需要放入 data 文件夹中
## 第 i 个样例组应该以：in_i.in、out_i.out 的格式命名


```
