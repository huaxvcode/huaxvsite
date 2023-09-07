# [A. Vika and Her Friends](https://codeforces.com/problemset/problem/1848/A)

## 题目大意：

有一幅 $n * m$ 的网格图，图上有 $k$ 个巡逻员和 $1$ 个逃课的学生，对于每一分钟逃课的学生和巡逻员都必须移动到相邻的格子上，他们都知道对方在哪一个格子，并据此选择移动路线；

如果该逃课的学生与巡逻员位于同一个格子就被抓住了

问该学生是否一定会被抓住？

## 思路：

假设经过非常多分钟后，巡逻员一定会非常的接近该名学生，但是，如果巡逻员都分布在学生的相邻格子上，则一定不会被抓住，否则就一定可以被抓住；

因此可以求出每一个巡逻员与该名学生相遇时的最终状态到底是否相邻还是可以合并在同一个格子上，如果相邻则一定不会被这名巡逻员抓住

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

long n, m, k;
long x, y;
long res = 0;
long calc_d(long x1, long y1, long x2, long y2) {
    return std::abs(x1 - x2) + std::abs(y1 - y2);
}

void solve() {
    res = 0;
    std::cin >> n >> m >> k >> x >> y;
    for (long i = 1; i <= k; i ++) {
        long tx, ty; std::cin >> tx >> ty;
        long ds = calc_d(x, y, tx, ty) - 1;
        if (ds & 1) {
            res = 1;
        }
    }
    if (res) std::cout << "NO\n";
    else std::cout << "YES\n";
    
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