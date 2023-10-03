# [E. Kolya and Movie Theatre](https://codeforces.com/problemset/problem/1862/E)

```cpp
#include <bits/stdc++.h>
typedef long long var;
typedef __int128 hh;

namespace {

const var N = 2e6;
std::priority_queue<var, std::vector<var>, std::greater<var>> qu;
var sum;
var n, m, d;
var a[N];
var res;
void solve() {
    sum = res = 0;
    while (qu.size()) qu.pop();
    std::cin >> n >> m >> d;
    for (var i = 1; i <= n; i ++) std::cin >> a[i];
    for (var i = 1; i <= n; i ++) {
        res = std::max(res, sum + a[i] - d * i);
        if (a[i] > 0) {
            qu.push(a[i]); sum += a[i];
        }
        if (qu.size() == m) {
            sum -= qu.top();
            qu.pop();
        }
    } 
    std::cout << res << '\n';
}

}

// g++ -std=c++20 Main.cpp -o Main && Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    int t; std::cin >> t; while (t --)
    solve();
    return 0;
}
```
