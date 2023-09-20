# [I. Power and Zero](https://codeforces.com/gym/103447/problem/I)

## 题目描述：

给定 $n$ 个正整数 $a_1, a_2, \cdots, a_n$

对于每一次操作，你可以选择多个整数，假设选择了：

> $a_{b_1}, a_{b_2}, \cdots, a_{b_m}$

你需要对每一个数 $a_{b_i}$ 减去 $2^{i - 1}$

问将所有整数都变为 $0$ 的最小操作数

## 思路：

统计每一位的 $1$ 的个数，然后减去连续二进制位的 $1111 \cdots 1$

```cpp
#include <bits/stdc++.h>
typedef long long ll;
typedef __int128 hh;

namespace {

const ll N = 2e5;
ll n, a[N];
ll one[200];
ll res;

void add(ll n) {
    ll i = -1;
    while (n) {
        i ++;
        if (n & 1) one[i] ++;
        n >>= 1;
    }
}

ll have_one(ll l, ll r) {
    l --;
    while (++ l <= r) if (one[l]) return l;
    return 0;
}

void show() {
    for (ll i = 0; i <= 60; i ++) std::cout << one[i] << ' ';
    std::cout << '\n';
}

bool do_one() {
    for (ll i = 0; i <= 60; i ++) if (one[i]) goto lab;
    return false;
    lab:;
    for (ll i = 0; i <= 60; i ++) {
        if (one[i]) one[i] --;
        else {
            auto t = have_one(i, 60);
            if (t == 0) break;
            one[t] --;
            for (ll j = i; j < t; j ++) one[j] ++;
        }
    }
    // show(); exit(0);
    return true;
}


void solve() {
    std::cin >> n;
    for (ll i = 1; i <= n; i ++) std::cin >> a[i];
    for (ll i = 1; i <= n; i ++) add(a[i]);
    res = 0; 
    // show();
    while (do_one()) {
        res ++;
    }
    std::cout << res << '\n';
}

}

// g++ -std=c++20 Main.cpp -o Main && ./Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    return 0;
}
```
