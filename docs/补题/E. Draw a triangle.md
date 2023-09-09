# [E. Draw a triangle](https://codeforces.com/gym/104008/problem/E)

如果三角形的 $3$ 个点都是整数坐标，那么围成的三角形面积 $s$ 的两倍一定是正整数，即 $2s$ 一定是正整数！

**叉积：**

假设向量 $A = (x1, y1), B = (x2, y2)$，则 $A \times B = x1 * y2 - y1 * x2$

平行四边形向量面积：$A \times B$

---

如果已知道两点的坐标为： $(x1, y1)$ 和 $(x2, y2)$ 且都是整数，请你求出一个整数坐标 $(x, y)$ 使得这三个点围成的三角形面积最小，面积必须为正数；

---

向量叉积：

> $(x - x1, y - y1) \times (x2 - x1, y2 - y1)$
>
> $(x2 - x1)x - x1(x2 - x1) - y(y2 - y1) + y1(y2 - y1)$
>
> $(x2 - x1)x + y(y1 - y2) - x1(x2 - x1) - y1(y1 - y2)$
>
> 即：$ax + by - x1*a - y1 * b$
>
> $t * gcd$
>
> 面积为正且最小，则 $t = 1$

```cpp
#include <bits/stdc++.h>
#define long long long
#define blong __int128

namespace code {
    
long x_, y_;
long x1, y1, x2, y2;

blong exgcd(blong a, blong b, blong& x, blong& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    blong d = exgcd(b, a % b, y, x);
    y -= a / b * x;
    return d;
}

void show(blong x, blong y) {
    std::cout << (long)(x1 + x) << ' ' << (long)(y1 + y) << '\n';
}

void solve() {
    std::cin >> x1 >> y1 >> x2 >> y2;
    x_ = x2 - x1; y_ = y2 - y1;
    // std::cout << x_ << ' ' << y_ << '\n';
    if (x_ == 0) {
        show(1, 0); return;
    }
    if (y_ == 0) {
        show(0, 1); return;
    }
    blong d, x, y;
    d = exgcd(y_ < 0 ? -y_ : y_, x_ < 0 ? -x_ : x_, x, y);
    y *= -1;
    if (y_ < 0) x *= -1;
    if (x_ < 0) y *= -1;
    show(x, y);
}
    
};

int main() {
	std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    long t; std::cin >> t; while (t --)
    code::solve();
    return 0;
}
```