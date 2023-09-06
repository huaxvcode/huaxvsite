# [E. Identical Parity](https://codeforces.com/gym/104076/problem/E)

## 暴力打表发现的规律

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

long n, k;
// #define yes std::cout << "1 "
// #define no std::cout << "0 "
#define yes std::cout << "Yes\n"
#define no std::cout << "No\n"

void solve() {
    std::cin >> n >> k;
    if (k % 2 == 0) {yes;return;}
    if (n == 1) {yes;return;}
    if (n == k) {yes;return;}
    if (k == 1) {no;return;}
    n -= k - 1;
    long x = n / (k + 1);
    long y = n % (k + 1);
    long sp = k - x * 2;
    if (sp <= 0) {no;return;}
    if (y == 0) {no;return;}
    if (y <= sp) {yes;return;}
    else {no;return;}
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    // for (long i = 1; i <= 300; i ++) {
    //     for (long j = 1; j <= i; j ++) {
    //         n = i, k = j;
    //         solve();
    //     }
    //     std::cout << '\n';
    // }
    return 0;
}

```

## exgcd 每吞入一个，都要吐出一个，这两者奇偶性相同

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

#define yes {std::cout << "Yes\n"; return;}
#define no {std::cout << "No\n"; return;}
long n, k;

long exgcd(long a, long b, long& x, long& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long d = exgcd(b, a % b, y, x);
    y -= a / b * x;
    return d;
}

void solve() {
    std::cin >> n >> k;
    if (n == k) yes
    if (k % 2 == 0) yes
    if (k == 1) no
    long a = n / k + 1, b = n / k, c = (n + 1) >> 1;
    long d, x, y;
    d = exgcd(a, b, x, y);
    if (c % d) no
    a /= d; b /= d; c /= d;
    x *= c; y *= c;
    long xx = (x % b + b) % b;
    long t = (xx - x) / b;
    long yy = y - a * t;
    if (xx > n % k) no
    if (yy < 0) no
    long a1 = b * (yy - k + n % k), a2 = b * yy, a3 = a * (n % k - xx);
    if (a1 > a2) no
    if (a3 < 0) no
    if (!(a1 > a3 || a2 < 0)) {
        long aa = std::max(a1, 0ll);
        long bb = std::min(a2, a3);
        long t = bb / a / b * a * b;
        if (t >= aa && t <= bb) yes
        else no
    }
    else no
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();

    return 0;
}

```