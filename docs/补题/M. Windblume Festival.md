# [M. Windblume Festival](https://codeforces.com/gym/103470/problem/M)

```cpp
#include <bits/stdc++.h>

const long long N = 2e6;
long long n;
long long a[N];
long long mi, mx, res, sum;
const long long inf = ~(1ll << 63);

void solve() {
    std::cin >> n;
    mi = inf; mx = -inf; res = -inf; sum = 0;
    for (long long i = 1; i <= n; i ++) std::cin >> a[i];
    for (long long i = 1; i <= n; i ++) {
        mi = std::min(mi, a[i]);
        mx = std::max(mx, a[i]);
        sum += a[i];
    }
    if (n == 1) {
        std::cout << a[1] << '\n'; return;
    }
    if (mi > 0) {
        for (long long i = 1; i <= n; i ++) {
            long long j = i - 1; if (j == 0) j = n;
            if (a[j] <= a[i]) res = std::max(res, sum - 2 * a[j]);
        }
        std::cout << res << '\n';
    }
    else if (mx < 0) {
        for (long long i = 1; i <= n; i ++) {
            long long j = i - 1; if (j == 0) j = n;
            if (a[j] >= a[i]) res = std::max(res, sum * (-1) + 2 * a[j]);
        }
        std::cout << res << '\n';
    }
    else {
        res = 0;
        for (long long i = 1; i <= n; i ++) res += std::abs(a[i]);
        std::cout << res << '\n';
    }
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long long t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```