# static_assert

使用 `assert` 会在程序运行中捕获错误

```cpp
#include <bits/stdc++.h>

template <typename T, typename U> 
void bit_copy(T a, U b) {
    if (sizeof(a) != sizeof(b)) {
        printf("bit_copy must have the same size!");
        assert(sizeof(a) == sizeof(b));
    }
    std::memcpy(&a, &b, sizeof(b));
}

int main() {
    int a = 4; double b = 3.14;
    printf("bit_copy start...");
    bit_copy(a, b);
    printf("bit_copy end...");
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
    printf("bit_copy start...");
    bit_copy(a, b);
    printf("bit_copy end...");
    return 0;
}
```
