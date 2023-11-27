# __func__

预定义标识符：`__func__`

```cpp
#include <bits/stdc++.h>

const char* print() { return __func__; }
int main() {
    std::cout << print() << '\n';
    // 输出函数的名称：print
}
```

这段代码输出函数名 `print`
