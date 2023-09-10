# [B. Indivisible](https://codeforces.com/problemset/problem/1818/B)

如果 $n = 1$，答案就是 $1$;

如果 $n$ 是奇数，则总和 $\frac{(n + 1) * n}{2}$ 是 $n$ 的倍数,因为 $n + 1$ 是偶数，所以这种情况一定无解；

如果 $n$ 是偶数，则总和 $\frac{(n + 1) * n}{2}$ 一定不会是 $n$ 的倍数，因为 $n + 1$ 是奇数，所以 $\gcd(n + 1, n) = 1$，且 $\frac{n}{2} < n$ 所以总和一定不是 $n$ 的倍数。

假设 $\frac{(n + 1) * n}{2}$ 是 $n$ 的倍数，则 $\frac{(n + 1) * n}{2} = kn$，所以 $n + 1 = 2 * k$，因为 $n + 1$ 是奇数，所以等式不成立。

在这里的启发就是，如果 $n$ 是偶数，保持原有顺序就一定可以保证不是倍数，如果是奇数，按原有顺序一定不是倍数，但是如果可以让原有顺序的最大值 +1，就可以破坏倍数的关系。

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

namespace {

const long N = 2e5;
long n;
long a[N];

void solve() {
    std::cin >> n;
    if (n == 1) {
        std::cout << 1 << '\n';
        return;
    }
    if (n % 2) {
        std::cout << -1 << '\n';
        return;
    }
    for (long i = 1; i <= n; i ++) a[i] = i;
    for (long i = 1; i + 1 <= n; i += 2) std::swap(a[i], a[i + 1]);
    for (long i = 1; i <= n; i ++) std::cout << a[i] << ' ';
    std::cout << '\n';
}

}

// g++ -std=c++20 Main.cpp -o Main && ./Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    return 0;
}
```