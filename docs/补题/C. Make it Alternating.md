# [C. Make it Alternating](https://codeforces.com/problemset/problem/1879/C)

统计连续相同的区块的个数（大于 1 的才统计进去）得到数组：

> $x_1, x_2, \cdots, x_n$

答案：

> $(x_1 + x_2 + \cdots + x_n - n)! * x_1 * x_2 * \cdot * x_n$

```cpp
#include <bits/stdc++.h>
typedef long long var;
typedef __int128 hh;

namespace {

const var mod = 998244353;
const var N = 2e6;
var pr[N];
std::string s;
var a[N], cur;
var n;

void solve() {
    std::cin >> s; n = s.size();
    var res = 0, sum = 0;
    var i = 0, j = 0;
    cur = 0;
    while (i < n) {
        while (j < n && s[i] == s[j]) j ++;
        sum += j - i - 1;
        if (j - i - 1) a[++ cur] = j - i;
        i = j;
    }
    res = pr[sum];
    for (var i = 1; i <= cur; i ++) res = res * a[i] % mod;
    std::cout << sum << ' ' << res << '\n';
}

}

// g++ -std=c++20 Main.cpp -o Main && Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    pr[0] = 1;
    for (var i = 1; i < N; i ++) pr[i] = pr[i - 1] * i % mod;
    int t; std::cin >> t; while (t --)
    solve();
    return 0;
}
```
