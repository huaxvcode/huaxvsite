# __func__

预定义标识符：`__func__`

## 输出函数名

```cpp
#include <bits/stdc++.h>

const char* print() { return __func__; }
int main() {
    std::cout << print() << '\n';
    // 输出函数的名称：print
}
```

这段代码输出函数名 `print`

等价于下面代码：

```cpp
#include <bits/stdc++.h>

const char* print() { 
    static const char* __func__ = "print";
    return __func__;  
}

int main() {
    std::cout << print() << '\n';
}
```

## 输出类名

```cpp
#include <bits/stdc++.h>

struct Node {
    const char* name;
    // 输出类名
    Node() : name(__func__) {}
};

int main() {
    Node t;
    std::cout << t.name << '\n';
}
```

输出结果：`Node`
