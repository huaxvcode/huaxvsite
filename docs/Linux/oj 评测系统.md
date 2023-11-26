# oj 评测系统

> 作者：林日清
> 
> 联系方式：1325595056@qq.com
>zi
> 转载请注明出处

## 基本命令

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

## 测试

```bash
#/bin/bash

# oj -cr Main.cpp
# oj -cr Main.py
# oj -cr Main.java

# oj -ocr Main.cpp
# oj -ocr Main.py
# oj -ocr Main.java

# oj -c Main.cpp Main.py Main.java
# oj -oc Main.cpp Main.py Main.java

# oj -cr Main.cpp Main.py Main.java

# oj -r Main.cpp Main.py Main.java
# oj -r Main.cpp
# oj -r Main.py
# oj -r Main.java

# oj -or Main.cpp Main.py Main.java

# oj -cr Random.cpp
# oj -cr Answer.cpp

# oj -cr Random.py
# oj -cr Answer.java

# oj -j 12 py java cpp
# oj -j 100 cpp cpp cpp
# oj -j 100 

# oj -s py java
# oj -s cpp cpp
# oj -s

# oj -n 12
# oj -a 12
# oj -n
# oj -a

# oj -n 23 py java
# oj -a 23 cpp
```

## 代码

### oj_tools.py

```py
from os import popen
from os import system
import os 
import sys
from time import time, sleep
import threading

lock = threading.Lock()
timeout = 5


def exit_error(a):
    a >>= 8
    if a:
        if a == 131:
            print("print so much !!!")
        elif a == 124:
            print("time limit exceed !!!")
        else:
            print("other error, maybe compiler error.")
        exit(a)

ote=0

## 编译单个文件
def cp(lang, name):
    global ote
    start = time()
    a=0
    if lang == 'py':
        pass
    elif lang == 'cpp':
        a=system(f"g++ -w -std=c++17 -O2 {name}.cpp -o {name} -pthread")
    elif lang == 'java':
        a=system(f"javac {name}.java")
    elif lang == 'c':
        a=system(f"gcc -w -std=c99 -O2 {name}.c -o {name}")
    end = time()
    lock.acquire()
    print('cp %s.%s use %.3f s' % (name, lang, (end - start)))
    ote=(ote if ote > (a>>8) else (a>>8))
    lock.release()


## 多线程运行
def runs(ls):
    global ote
    pools = []
    for i, j in ls:
        pools.append(threading.Thread(target=i, args=j))
    for i in pools:
        i.start()
    for i in pools:
        i.join()
    exit_error(ote << 8)

## 多线程编译多个文件    
def cps(lns):
    funs = []
    for i, j in lns:
        funs.append([cp, (i, j)])
    runs(funs)

def get_words(s):
    ans = []
    ts = ""
    emtpy = {
        ' ', '\t', '\n', '\f', '\b', '\r'
    }
    for i in s:
        if i in emtpy:
            if ts:
                ans.append(ts)
                ts = ""
        else: 
            ts += i
    if ts:
        ans.append(ts)
    return ans

# 逻辑比较两个字符串是否相同
def check(s1, s2):
    s1 = s1.split('\n')
    s2 = s2.split('\n')

    emtpy = {
        ' ', '\t', '\n', '\f', '\b', '\r'
    }
    def pop_emtpy_end(s1):
        while len(s1):
            on = 0
            for i in s1[-1]:
                if i not in emtpy:
                    on = 1
                    break
            if on:
                break

            s1.pop()

    pop_emtpy_end(s1)
    pop_emtpy_end(s2)

    if len(s1) != len(s2):
        return False

    for i, j in zip(s1, s2):
        if get_words(i) != get_words(j):
            return False
    return True

def get_content(path):
    s = ""
    with open(path, encoding='utf-8', mode='r') as f:
        s = f.read()
    return s

def equal(p1="./run.txt", p2="./out.txt"):
    if check(get_content(p1), get_content(p2)):
        return True
    return False

def get_status(a):
    return a >> 8


## 运行单个文件
def rn(lang, name):
    print(f'start rn {name}.{lang}')
    start = time()
    a=0
    if lang == 'cpp' or lang == 'c':
        a=system(f'(control_safe.sh "./{name}" "in.txt" "memory_safe") >run.txt')
    elif lang == 'py':
        a=system(f'(control_safe.sh "python3" "{name}.py" "in.txt" "memory_safe") >run.txt')
    elif lang == 'java':
        a=system(f'(control_safe.sh "java" "{name}" "in.txt" "memory_safe") >run.txt')
    end = time()
    print('rn %s.%s use %.3f s' % (name, lang, end - start))
    exit_error(a)
    if equal():
        print("· Accept")
    else:
        print('· Error')


## 正常运行单个文件
def rno(lang, name):
    print(f'start rn {name}.{lang}')
    start = time()
    if lang == 'cpp' or lang == 'c':
        system(f'./{name}')
    elif lang == 'py':
        system(f'python3 {name}.py')
    elif lang == 'java':
        system(f'java {name}')
    end = time()
    print('rn %s.%s use %.3f s' % (name, lang, end - start))


def random(lang):
    print(f'start rn Random.{lang}')
    start = time()
    a=0
    if lang == 'cpp' or lang == 'c':
        a=system(f'(control_safe.sh "./Random" "memory_safe") >in.txt')
    elif lang == 'py':
        a=system(f'(control_safe.sh "python3" "Random.py" "memory_safe" "0" "1") >in.txt')
    elif lang == 'java':
        a=system(f'(control_safe.sh "java" "Random" "memory_safe" "0" "1") >in.txt')
    end = time()
    print('rn %s.%s use %.3f s' % ('Random', lang, end - start))
    exit_error(a)


def answer(lang):
    print(f'start rn Answer.{lang}')
    start = time()
    a=0
    if lang == 'cpp' or lang == 'c':
        a=system('(control_safe.sh "./Answer" "in.txt" "memory_safe") >out.txt')
    elif lang == 'py':
        a=system('(control_safe.sh "python3" "Answer.py" "in.txt" "memory_safe") >out.txt')
    elif lang == 'java':
        a=system('(control_safe.sh "java" "Answer" "in.txt" "memory_safe") >out.txt')
    end = time()
    print('rn %s.%s use %.3f s' % ('Answer', lang, end - start))
    exit_error(a)


## 编译并运行单个文件
def oj_single(lang, name):
    cp(lang, name)
    if name == 'Random':
        random(lang)
        return
    elif name == 'Answer':
        answer(lang)
        return
    rn(lang, name)
    # if equal():
    #     print("· Accept")
    # else:
    #     print('· Error')


## 对拍一次
def oj(lang_r='cpp', lang_a='cpp', lang_m='cpp'):
    # runs([
    #     [cp, (lang_r, 'Random')],
    #     [cp, (lang_a, 'Answer')],
    #     [cp, (lang_m, 'Main')]
    # ])
    random(lang_r)
    answer(lang_a)
    rn(lang_m, 'Main')
    if equal():
        # print("· Accept")
        return True
    else:
        # print('· Error')
        return False


def oj_one(lang_r='cpp', lang_a='cpp'):
    runs([
        [cp, (lang_r, 'Random')],
        [cp, (lang_a, 'Answer')]
    ])
    random(lang_r)
    answer(lang_a)


oj_get_nums = 10


def oj_get(lang_r='cpp', lang_a='cpp', nums=oj_get_nums):
    nums = oj_get_nums
    cmd = '''
        if [ -d datas ]; then
            rm -r datas;
        fi;
        mkdir datas;
    '''
    system(cmd)
    runs([
        [cp, (lang_r, 'Random')],
        [cp, (lang_a, 'Answer')]
    ])
    for i in range(1, nums+1):
        cmd = f'''
            touch datas/in_{i}.in;
            touch datas/out_{i}.out;
        '''
        print(f'new data_{i}')
        system(cmd)
        a=0
        if lang_r == 'cpp' or lang_r == 'c':
            a=system(f'(control_safe.sh "./Random" "memory_safe") >datas/in_{i}.in')
        elif lang_r == 'py':
            a=system(f'(control_safe.sh "python3" "Random.py" "memory_safe" "0" "1") >datas/in_{i}.in')
        elif lang_r == 'java':
            a=system(f'(control_safe.sh "java" "Random" "memory_safe" "0" "1") >datas/in_{i}.in')
        exit_error(a)
        if lang_a == 'cpp' or lang_a == 'c':
            a=system(f'(control_safe.sh "./Answer" "datas/in_{i}.in" "memory_safe") >datas/out_{i}.out')
        elif lang_a == 'py':
            a=system(f'(control_safe.sh "python3" "Answer.py" "datas/in_{i}.in" "memory_safe") >datas/out_{i}.out')
        elif lang_a == 'java':
            a=system(f'(control_safe.sh "java" "Answer" "datas/in_{i}.in" "memory_safe") >datas/out_{i}.out')
        exit_error(a)

def oj_get_run(lang='cpp', nums=oj_get_nums):
    nums = oj_get_nums
    cp(lang, 'Main')
    cmd = f'''
        if [ -d runs ]; then
            rm -r runs;
        fi;
        mkdir runs;
    '''
    system(cmd)
    for i in range(1, nums+1):
        cmd = f'''
            touch runs/run_{i}.txt
        '''
        print(f'test data_{i}')
        a=0
        if lang == 'cpp' or lang == 'c':
            a=system(f'(control_safe.sh "./Main" "datas/in_{i}.in" "memory_safe") >runs/run_{i}.txt')
        elif lang == 'py':
            a=system(f'(control_safe.sh "python3" "Main.py" "datas/in_{i}.in" "memory_safe") >runs/run_{i}.txt')
        elif lang == 'java':
            a=system(f'(control_safe.sh "java" "Main" "datas/in_{i}.in" "memory_safe") >runs/run_{i}.txt')
        exit_error(a)
        if check(get_content(f'datas/out_{i}.out'), get_content(f'runs/run_{i}.txt')):
            print(f'data_{i} Accept')
        else:
            print(f'data_{i} Error')

def deal_file(name):
    for i in range(len(name) - 1, 0, -1):
        if name[i] == '.':
            if name[i+1:] not in ['py', 'cpp', 'c', 'java']:
                break
            return [name[i+1:], name[:i]]
    print("you may have some errors in you put")
    exit()

def is_right(type_f):
    if type_f in { 'cpp', 'py', 'c', 'java' }:
        return type_f
    print("you may have some errors in you put")
    exit(0)

def main():
    global oj_get_nums
    system('echo -n "" > run.txt')
    arg = sys.argv[1:]
    if len(arg) == 0:
        return
    mo = set(arg[0][1:].lower())
    if ('o' in mo) and len(mo) <= 3:
        if len(arg) == 1:
            return
        if 'c' in mo:
            cps(list(map(deal_file, arg[1:])))
        if 'r' in mo:
            for i, j in map(deal_file, arg[1:]):
                rno(i, j)
    elif ('j' in mo) and len(mo) == 1:
        if len(arg) == 2:
            n = int(arg[1])
            runs([
                [cp, ('cpp', 'Random')],
                [cp, ('cpp', 'Answer')],
                [cp, ('cpp', 'Main')],
            ])
            for i in range(n):
                if oj():
                    continue
                return
        else:
            n = int(arg[1])
            runs([
                [cp, (is_right(arg[2]), 'Random')],
                [cp, (is_right(arg[3]), 'Answer')],
                [cp, (is_right(arg[4]), 'Main')],
            ])
            for i in range(n):
                if oj(*map(is_right, arg[2:])):
                    continue
                return
    elif ('s' in mo) and len(mo) == 1:
        if len(arg) == 1:
            oj_one()
        else:
            oj_one(*map(is_right, arg[1:]))
    elif ('n' in mo) and len(mo) == 1:
        if len(arg) == 1:
            oj_get()
            return
        n = int(arg[1])
        oj_get_nums = n
        oj_get(*map(is_right, arg[2:]))
    elif ('a' in mo) and len(mo) == 1:
        if len(arg) == 1:
            oj_get_run()
            return
        oj_get_nums = int(arg[1])
        oj_get_run(*map(is_right, arg[2:]))
    else:
        if 'c' in mo and 'r' in mo:
            for i, j in map(deal_file, arg[1:]):
                oj_single(i, j)
        else:
            if 'c' in mo:
                cps(list(map(deal_file, arg[1:])))
            if 'r' in mo:
                for i, j in map(deal_file, arg[1:]):
                    print(i, j)
                    rn(i, j)

# python3 oj_tools.py
if __name__ == '__main__':
    # print(set("hello"))
    main()

```

### oj.cpp

```cpp
#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
typedef long long var;
typedef __int128 hh;

std::string s = "python3 -u ~/huaxv/.lrq_tools/sources/oj_tools.py";

// g++ -std=c++20 oj.cpp -o oj && oj
int main(int n, char* ss[]) {
    {
        var on = 1;
        for (var i = 1; i < n; i ++) {
            if (on) s += ' ';
            on = 1; s += ss[i];
        }
        system((char*)s.data());
    }
    return 0;
}
```

### memory_safe.cpp

```bash
#include <bits/stdc++.h>
typedef long long var;
typedef __int128 vhh;

namespace {

const var N = 5e7;
var cnt;
char s[N + 100];
var status;

/*

cd ~/huaxv/.lrq_tools/sources && g++ -std=c++17 memory_safe.cpp -o memory_safe && mv memory_safe ..

*/

void solve() {
    char c;
    while ((c = std::cin.get()) != EOF) {
        if (cnt >= N) {
            // std::cout << "print so much !!!\n";
            // exit(131); 
            status = 131;
            // return;
            // break;
        }
        else {
            s[cnt ++] = c;
        }
        //std::cout << c;
    }
    if (!status) std::cout << s;
    exit(status);
}

}

// g++ -std=c++17 Random.cpp -o Random
int main() {
    //std::ios::sync_with_stdio(0);
    //std::cin.tie(0); std::cout.tie(0);
    std::random_device rd;
    std::mt19937 mt(rd());
    srand(mt());
    int t = 1; 
    // std::cin >> t;
    for (int i = 1; i <= t; i ++) {
        // std::cout << "Case #1: ";
        solve();
    }
    return 0;
}

```

### control_safe.sh

```bash
#!/bin/bash



max_ti=10

if [[ $# -eq 2 ]]; then
    (timeout $max_ti $1) | $2
    rs=(${PIPESTATUS[*]})
elif [[ $# -eq 3 ]]; then
    (timeout $max_ti $1<$2) | $3
    rs=(${PIPESTATUS[*]})
elif [[ $# -eq 4 ]]; then
    (timeout $max_ti $1 $2<$3) | $4
    rs=(${PIPESTATUS[*]})
elif [[ $# -eq 5 ]]; then
    (timeout $max_ti $1 $2) | $3
    rs=(${PIPESTATUS[*]})
else
    exit 1
fi;

st=0
if [[ ${rs[1]} -ne 0 ]]; then 
    # echo "print so much !!!";
    st=131
elif [[ ${rs[0]} -ne 0 ]]; then
    # echo "time limit exceed !!!"
    st=124
fi;

exit $st



# #!/bin/bash



# max_ti=10

# if [ $# -eq 2 ]; then
#     (timeout $max_ti $1) | $2
#     rs=(${PIPESTATUS[*]})
# elif [ $# -eq 3 ]; then
#     (timeout $max_ti $1<$2) | $3
#     rs=(${PIPESTATUS[*]})
# else
#     exit 1
# fi;

# st=0
# if [[ ${rs[1]} -ne 0 ]]; then 
#     # echo "print so much !!!";
#     st=131
# elif [[ ${rs[0]} -ne 0 ]]; then
#     # echo "time limit exceed !!!"
#     st=124
# fi;

# exit $st

```
