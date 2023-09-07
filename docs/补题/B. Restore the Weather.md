# [B. Restore the Weather](https://codeforces.com/problemset/problem/1833/B)

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

const long N = 3e5;
long n, m;
long b[N];
std::pair<long, long> a[N];
long c[N];

void solve() {
    std::cin >> n >> m;
    for (long i = 1; i <= n; i ++) std::cin >> a[i].first, a[i].second = i;
    for (long i = 1; i <= n; i ++) std::cin >> b[i];
    std::sort(b + 1, b + 1 + n);
    std::sort(a + 1, a + 1 + n, [&](auto x, auto y) {
        if (x.first != y.first) return x.first < y.first;
        if (x.second != y.second) return x.second < y.second;
        return false;
    });
    long error = 0;
    for (long i = 1; i <= n; i ++) {
        auto [x, y] = a[i];
        c[y] = b[i];
        if (std::abs(x - b[i]) > m) error = 1;
    }
    for (long i = 1; i <= n; i ++) std::cout << c[i] << ' ';
    std::cout << '\n';
    if (error) std::cout << "ERROR\n";
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