# [M. Best Carry Player](https://codeforces.com/gym/104076/problem/M)

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

const long N = 2e5;
long n;
long res;

std::vector<long> add(const std::vector<long>& a, const std::vector<long>& b) {
    long mod = 10;
    std::vector<long> res;
    long n = a.size(), m = b.size();
    for (long i = 0, t = 0; i < n || i < m || t; i ++) {
        if (i < n) t += a[i];
        if (i < m) t += b[i];
        res.push_back(t % mod);
        t /= mod;
        if (t) ::res ++;
    }
    return res;
}

std::vector<long> get(long x) {
    std::vector<long> res;
    if (x == 0) return {0};
    while (x) {
        res.push_back(x % 10); x /= 10;
    }
    return res;
}

void solve() {
    std::cin >> n; 
    res = 0;
    std::vector<long> sum(0);
    for (long i = 1; i <= n; i ++) {
        long t; std::cin >> t;
        sum = add(sum, get(t));
    }
    std::cout << res << '\n';
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```