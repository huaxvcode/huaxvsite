# [J. Local Minimum](https://codeforces.com/gym/103447/problem/J)

```cpp
#include <bits/stdc++.h>
typedef long long ll;
typedef __int128 hh;

namespace {

ll n, m;
ll a[1010][1010];
ll x[1010];
ll y[1010];
ll res;

void solve() {
    std::cin >> n >> m;
    for (ll i = 1; i <= n; i ++) x[i] = 1e9;
    for (ll i = 1; i <= m; i ++) y[i] = 1e9;
    for (ll i = 1; i <= n; i ++) {
        for (ll j = 1; j <= m; j ++) std::cin >> a[i][j];
    }
    for (ll i = 1; i <= n; i ++) {
        for (ll j = 1; j <= m; j ++) {
            x[i] = std::min(x[i], a[i][j]);
        }
    }
    for (ll i = 1; i <= m; i ++) {
        for (ll j = 1; j <= n; j ++) {
            y[i] = std::min(y[i], a[j][i]);
        }
    }
    for (ll i = 1; i <= n; i ++) {
        for (ll j = 1; j <= m; j ++) {
            if (std::min(x[i], y[j]) == a[i][j]) {
                res ++;
            }
        }
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
