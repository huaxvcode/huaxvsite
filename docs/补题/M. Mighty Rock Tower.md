# [M. Mighty Rock Tower](https://codeforces.com/problemset/problem/1866/M)

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

const long N = 2e5;
long n;
long a[N];
long sum;

void solve() {
    std::cin >> n;
    sum = 0;
    for (long i = 1; i <= n; i ++) {
        std::cin >> a[i]; sum += a[i];
    }
    if (n == 1) {
        std::cout << "NO\n"; return;
    }
    std::sort(a + 1, a + 1 + n, [&](long x, long y) {
        if (x != y) return x > y;
        return false;
    });
    for (long i = 1; i <= n; i ++) {
        if (a[i] != 1) {
            sum --;
        }
        else sum -= 2;
    }
    if (sum < 0) std::cout << "NO\n";
    else std::cout << "YES\n";
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```