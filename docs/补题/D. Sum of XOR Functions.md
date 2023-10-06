# [D. Sum of XOR Functions](https://codeforces.com/problemset/problem/1879/D)

按位拆分，然后统计含有奇数个 $1$ 的子串的总长度

```cpp
#include <bits/stdc++.h>
typedef long long var;
typedef __int128 hh;

namespace {

const var N = 3e6 + 10;
const var mod = 998244353;
const var inf = 1ll << 33;
var n;
var a[N];
std::string s;
var dp[3][N];
var dps[3][N];
var res, ans;

var calc() {
    res = 0;
    std::memset(dp, 0, sizeof dp);
    std::memset(dps, 0, sizeof dps);
    for (var i = 1; i <= n; i ++) {
        if (s[i] - '0') {
            if (i == 1) {
                dp[1][i] = 1;
                dps[1][i] = 1;
                continue;
            }
            dp[1][i] = (dp[2][i - 1] + 1 + dp[0][i - 1]) % mod;
            dp[2][i] = dp[1][i - 1] % mod;
            dps[1][i] = (dps[2][i - 1] + dp[2][i - 1] + 1 + dp[0][i - 1] * (dp[0][i - 1] + 1) / 2 + dp[0][i - 1]) % mod;
            dps[2][i] = (dps[1][i - 1] + dp[1][i - 1]) % mod;
        }
        else {
            dp[1][i] = dp[1][i - 1];
            dp[2][i] = dp[2][i - 1];
            dp[0][i] = dp[0][i - 1] + 1;
            dps[1][i] = (dps[1][i - 1] + dp[1][i]) % mod;
            dps[2][i] = (dps[2][i - 1] + dp[2][i]) % mod;
        }
    }
    for (var i = 1; i <= n; i ++) res += dps[1][i], res %= mod;
    return res;
}

// 求含有奇数个 1 的子串的总长度
void solve() {
    std::cin >> n;
    for (var i = 1; i <= n; i ++) std::cin >> a[i];
    for (var i = 1; i <= inf; i <<= 1) {
        s = ' ';
        for (var _ = 1; _ <= n; _ ++) {
            s += char('0' + ((a[_] & i) ? 1 : 0));
        }
        auto t = calc();
        ans = (ans + t * i % mod) % mod;
    }
    std::cout << ans << '\n';
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
