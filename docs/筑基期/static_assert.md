# static_assert

使用 `assert` 会在程序运行时捕获错误

```cpp
#include <bits/stdc++.h>

template <typename T, typename U> 
void bit_copy(T a, U b) {
    if (sizeof(a) != sizeof(b)) {
        std::cout << "bit_copy must have the same size!\n";
        assert(sizeof(a) == sizeof(b));
    }
    std::memcpy(&a, &b, sizeof(b));
}

int main() {
    int a = 4; double b = 3.14;
    bit_copy(a, b);
    return 0;
}
```

---

使用 `static_assert` 编译时就会捕获错误，并输出提示信息

```cpp
#include <bits/stdc++.h>

template <typename T, typename U> 
void bit_copy(T a, U b) {
    static_assert(sizeof(a) == sizeof(b), "bit_copy must have the same size!");
    std::memcpy(&a, &b, sizeof(b));
}

int main() {
    int a = 4; double b = 3.14;
    bit_copy(a, b);
    return 0;
}
```

还可以在全局区块中使用来判断预处理是否有不符合预期的地方：

```cpp
#include <bits/stdc++.h>

static_assert(0 < 1, "what happened");

int main() {
    return 0;
}
```

『注意』：`static_assert` 只能用于常量的比较，如果出现了变量就会报错！！！
