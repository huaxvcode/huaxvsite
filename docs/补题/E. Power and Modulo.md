# [E. Power and Modulo](https://codeforces.com/gym/103447/problem/E)

下面几种情况可以特判：

- 如果全部都是 $0$，那么只能取模 $1$ 才能成立；
- 如果第一位不是 $1$，无法通过取模得到；
- 如果只有第一位是 $1$，且只有 $1$ 个元素时，可以对 $m > 1$ 的任意一个数取模得到；
- 如果只有第一位是 $1$，且后面都是 $0$，只能对 $2$ 取模得到；

---

一般情况下，$a[i + 1] = 2 * a[i]$

如果到了某一位后，使得：$a[i + 1] \neq 2 * a[i]$ 说明 $2 * a[i]$ 取模 $m$ 生效了，且 $a[i] < m$, $m \leq 2 * a[i] < 2 * m$，所以 $m = 2 * a[i] - a[i + 1]$

```cpp
#include <bits/stdc++.h>
typedef long long ll;
typedef __int128 hh;

namespace {

const ll N = 2e6;
ll n;
ll a[N];
ll sum;
ll res;

void solve() {
    sum = res = 0;
    std::cin >> n;
    for (ll i = 1; i <= n; i ++) std::cin >> a[i], sum += a[i];
    if (a[1] == 0 && sum == 0) { std::cout << 1 << '\n'; return; }
    if (a[1] != 1) { std::cout << -1 << '\n'; return; }
    if (sum == 1 && n > 1) { std::cout << 2 << '\n'; return; }
    if (sum == 1) { std::cout << -1 << '\n'; return; }
    for (ll i = 1; i < n; i ++) {
        if (a[i] * 2 != a[i + 1]) {
            res = a[i] * 2 - a[i + 1];
            if (res <= 0) { std::cout << -1 << '\n'; return; }
            break;
        }
    }
    if (res == 0) { std::cout << -1 << '\n'; return; }
    for (ll i = 1, p = 1; i <= n; i ++, p = p * 2 % res) {
        if (a[i] != p) { std::cout << -1 << '\n'; return; }
    }
    std::cout << res << '\n';
}

}

// g++ -std=c++20 Main.cpp -o Main && ./Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    int t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```
