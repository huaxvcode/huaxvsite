# [B. Battling with Numbers](https://codeforces.com/problemset/problem/1866/B)

```cpp
#include <bits/stdc++.h>
typedef long long var;
typedef __int128 hh;

namespace {

const var N = 2e6;
const var mod = 998244353;
var n, m;
var a[N], pa[N];
var b[N], pb[N];
var cur;

var qpow(var a, var b, var mod) {
    var ans = 1;
    a %= mod;
    while (b) {
        if (b & 1) ans = ans * a % mod;
        b >>= 1; a = a * a % mod;
    }
    return ans;
}

void solve() {
    cur = 0;
    std::cin >> n;
    for (var i = 1; i <= n; i ++) std::cin >> a[i];
    for (var i = 1; i <= n; i ++) std::cin >> pa[i];
    std::cin >> m;
    for (var i = 1; i <= m; i ++) std::cin >> b[i];
    for (var i = 1; i <= m; i ++) std::cin >> pb[i];
    if (n < m) { std::cout << 0 << '\n'; return; }
    {
        var i = 1, j = 1;
        while (j <= m && i <= n) {
            while (i <= n && a[i] != b[j]) i ++;
            if (i > n) { std::cout << 0 << '\n'; return; }
            if (pa[i] < pb[j]) { std::cout << 0 << '\n'; return; }
            if (pa[i] == pb[j]) ++ cur;
            j ++;
        }
        cur = n - cur;
    }
    std::cout << qpow(2, cur, mod) << '\n';
}

}

// g++ -std=c++20 Main.cpp -o Main && Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    //int t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```
