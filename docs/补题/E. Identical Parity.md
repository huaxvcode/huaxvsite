# [E. Identical Parity](https://codeforces.com/gym/104076/problem/E)

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

long n, k;
#define yes std::cout << "Yes\n"
#define no std::cout << "No\n"

void solve() {
    std::cin >> n >> k;
    if (k % 2 == 0) {yes;return;}
    if (n == 1) {yes;return;}
    if (k == 1) {no;return;}
    n -= k;
    long t1 = n / (k + 1);
    long t2 = n % (k + 1);
    long _ = k - t1 * 2;
    if (_ < 0) {no;return;}
    if (t2 < _) {yes;return;}
    else {no;return;}
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    // for (long i = 1; i <= 25; i ++) {
    //     for (long j = 1; j <= i; j ++) {
    //         n = i, k = j;
    //         solve();
    //     }
    //     std::cout << '\n';
    // }
    return 0;
}

```