# [Modulo Ruins the Legend](https://codeforces.com/gym/104090/problem/A)

```cpp
#include <bits/stdc++.h>

long long exgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long long d = exgcd(b, a % b, y, x);
    y -= a / b * x;
    return d;
}

long long n, m;
long long sum;

void solve() {
    std::cin >> n >> m;
    for (long long i = 1; i <= n; i ++) {
        long long t; std::cin >> t; sum += t; sum %= m;
    }
    long long a = n, b = n * (n + 1) >> 1;
    long long s, d, t1, t2;
    long long d1 = exgcd(a, b, s, d);
    long long d2 = exgcd(d1, m, t1, t2);
    s = s * t1 % m;
    d = d * t1 % m;
    long long t = sum / d2;
    if (((sum % d2 - d2) % m + m) % m < sum % d2) t ++;
    long long res = ((sum - t * d2) % m + m) % m;
    s = (s * -t % m + m) % m;
    d = (d * -t % m + m) % m;
    std::cout << res << '\n';
    std::cout << s << ' ' << d << '\n';
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    
    solve();
    return 0;
}

```