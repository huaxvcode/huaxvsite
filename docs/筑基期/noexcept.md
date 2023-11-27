---
title: noexcept
header-includes:
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
output:
  pdf_document:
    latex_engine: xelatex
    toc: true
    template: C:/Huaxv/Huaxv-Tool/markdown-preview=enhanced/template.tex
    highlight: tango
    path: C:/Users/huaxv/Desktop/noexcept.pdf
---

# noexcept

阻止异常的继续抛出，直接中断程序

```cpp
#include <bits/stdc++.h>

void func1() { throw(1); }
void func2() { func1(); }
void func3() noexcept { func2(); }

int main() {
    try {
        func1();
    }
    catch(...) {
        std::cout << "func1 error\n";
    }
    try {
        func2();
    }
    catch(...) {
        std::cout << "func2 error\n";
    }
    try {
        func3();
    }
    catch(...) {
        std::cerr << "func3 error\n";
    }
    return 0;
}
```

由于 `func1` 函数抛出了一个异常，所以 `func2` 函数继续向上抛出异常，直到被 `catch` 捕获为止

为了停止异常继续向上传播，`func3` 用 `noexcept` 修饰，直接强制中断程序并报错！

