# [B. Sort with Step](https://codeforces.com/problemset/problem/1823/B)

如果只能交换距离为 $k$ 的两个元素，问是否可以将数组排成有序状态？

如果能排成有序状态，则 $i$ 和 $a[i]$ 必定为同一组，即：$i \bmod k == a[i] \bmod k$ 否则一定不行！

如果只有两个元素 $a[i]$ 不在 $i$ 组，$a[j]$ 不在第 $j$ 组，那么 $a[j]$ 必定在第 $i$ 组，$a[i]$ 必定在第 $j$ 组！交换一次就可以继续排成有序

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

const long N = 3e5;
long n, k;
long a[N];
long error;

bool check() {
    for (long i = 1; i <= n; i ++) {
        if (i % k != a[i] % k) error ++;
    }
    return !error;
}

void solve() {
    std::cin >> n >> k;
    error = 0;
    for (long i = 1; i <= n; i ++) std::cin >> a[i];
    if (check()) {
        std::cout << 0 << '\n'; return;
    }
    else if (error == 2) {
        std::cout << 1 << '\n'; return;
    }
    else {
        std::cout << -1 << '\n'; return;
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