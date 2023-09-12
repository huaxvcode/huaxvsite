# [D, Power Tower](http://oj.daimayuan.top/course/28/problem/536)

给定有个序列：$a_1, a_2, a_3, \cdots, a_n$，请求出 $a_1^{a_2^{a_3 ^ {\cdots}}} \bmod m$ 的值

---

如果底数是 $1$ 则方程式的值固定为 $1$；

`huaxv` 需要判断指数与 $phi(m)$ 的大小，如果指数的某段为 $1$，那么只需要计算之前的就行，并且连续不为 $1$ 的段的长度超过了 $32$ 则方程式的值一定会超出 $long$ 范围内。

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

namespace {

const long N = 2e5 + 10;
long n, m, q;
long a[N];
long pm[N], cnt;

long phi(long n) {
    long ans = n;
    for (long i = 2; i * i <= n; i ++) {
        if (n % i == 0) {
            ans = ans / i * (i - 1);
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) ans = ans / n * (n - 1);
    return ans;
}

long qpow(long a, long b, long mod) {
    long ans = 1; a %= mod;
    while (b) {
        if (b & 1) ans = ans * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return ans % mod;
}

long ck_qpow(long a, long b, long c) {
    if (a == 1) return 1;
    long ans = 1;
    while (b) {
        if (a > c) return 0;
        if (b & 1) {
            ans = ans * a;
            if (ans > c) return 0;
        }
        a = a * a;
        b >>= 1;
    }
    return ans;
}

// 有问题！！
// long check(long l, long r, long c) {
//     long ans = 1;
//     for (long i = r; i >= l; i --) {
//         ans = ck_qpow(a[i], ans, c);
//         if (ans) continue;
//         return 0;
//     }
//     return ans;
// }

long check(long l, long r, long c) {
    
    long ans = 1;
    for (long i = l, j = 1; i <= r && j <= 32; i ++, j ++) {
        if (a[i] == 1) {
            r = i; break;
        }
    }
    if (r - l + 1 >= 32) return 0;
    for (long i = r; i >= l; i --) {
        ans = ck_qpow(a[i], ans, c);
        if (ans) continue;
        return 0;
    }
    return ans > c ? 0 : ans;
}

long calc(long l, long r, long step) {
    if (pm[step] == 1) return 0;
    if (a[l] == 1) return 1;
    if (l == r) return a[l] % pm[step];
    long t = check(l + 1, r, pm[step + 1]);
    if (t) return qpow(a[l], t, pm[step]);
    return qpow(a[l], calc(l + 1, r, step + 1) + pm[step + 1], pm[step]);
}

long read() {
    int t; std::cin >> t; return t;
}

void solve() {
    n = read(); m = read();
    for (long i = 1; i <= n; i ++) a[i] = read();
    pm[++ cnt] = m;
    while (m > 1) {
        m = pm[++ cnt] = phi(m);
    }
    q = read();
    while (q --) {
        long l, r; l = read(); r = read();
        // for (long i = l; i <= r; i ++) std::cout << (int)a[i] << ' ';
        // std::cout << '\n';
        std::cout << (int)calc(l, r, 1) << '\n';
    }
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