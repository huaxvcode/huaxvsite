# [B. Longest Divisors Interval](https://codeforces.com/problemset/problem/1855/B)

先假定他的区间长度为 $len$，则 $n$ 一定会是 $1$ 的倍数、$2$ 的倍数、···、$len-1$ 的倍数、$len$ 的倍数

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

long n;

void solve() {
    std::cin >> n;
    if (n & 1) { std::cout << 1 << '\n'; return; }
    long ml;
    for (long i = 1; ; i ++) {
        if (n % i) break;
        ml = i;
    }
    std::cout << ml << '\n';
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```