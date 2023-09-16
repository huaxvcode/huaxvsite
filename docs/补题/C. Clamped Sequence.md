# [C. Clamped Sequence](https://codeforces.com/gym/104160/problem/C)

```cpp
#include <bits/stdc++.h>
#define ll long long
#define hh __int128

namespace {

const ll N = 2e6;
ll n, m;
ll a[N], b[N];
ll res;

void solve() {
    std::cin >> n >> m;
    for (ll i = 1; i <= n; i ++) std::cin >> a[i];
    for (ll i = 1; i <= n; i ++) {
        ll l = a[i], r = a[i] + m;
        ll t = 0;
        for (ll j = 1; j <= n; j ++) {
            b[j] = std::max(a[j], l);
            b[j] = std::min(b[j], r);   
        }
        for (ll j = 1; j < n; j ++) {
            t += std::abs(b[j] - b[j + 1]);
        }
        res = std::max(res, t);
    }
    for (ll i = 1; i <= n; i ++) {
        ll r = a[i], l = a[i] - m;
        ll t = 0;
        for (ll j = 1; j <= n; j ++) {
            b[j] = std::max(a[j], l);
            b[j] = std::min(b[j], r);   
        }
        for (ll j = 1; j < n; j ++) {
            t += std::abs(b[j] - b[j + 1]);
        }
        res = std::max(res, t);
    }
    std::cout << res << '\n';
}

}

// g++ -std=c++20 Main.cpp -o Main && ./Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    //long t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```
