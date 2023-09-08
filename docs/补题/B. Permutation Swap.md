# [B. Permutation Swap](https://codeforces.com/problemset/problem/1828/B)

给定一个 $1 \sim n$ 的排列，你只能交换相隔距离为 $d$ 的两个元素，但是可以交换无数次

问你，若要将该排列排成 $1 \sim n$ 的顺序，最大的 $d$ 可以取多少？

---

直观上很像希尔排序：

对于每一轮的希尔排序，你都需要选定一个长度 $d$，然后按照距离为 $d$ 的两个元素记为相邻，可以分成 $d$ 组，对每一组元素进行排序；

如果选取的 $d$ 分组后排序能排成有序状态，能确定什么结论呢？

假设有这样的排列：$4, 2, 6, 7, 5, 3, 1$

若要将 $4$ 排到第 $4$ 个元素处，那么 $4$ 和 $7$ 必定在同一组；

若要将 $7$ 排到第 $7$ 个元素处，那么 $7$ 和 $1$ 必定在同一组；

若要将 $6$ 排到第 $6$ 个元素处，那么 $6$ 一定和 $3$ 一组；

大致可以分组成以下选择：

```txt
4, 7, 1
6, 3
2
5
```

取每一小组按照位置排序后的间隔差，记为：$d_1, d_2, d_3, \cdots, d_n$

则 $d | d_i$ 一定成立，即题目就是求最大公约数！

时间复杂度：$O(n\log(n))$

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

const long N = 3e5;
long n;
long a[N];
long on[N];
std::vector<long> vt;
std::vector<long> ds;
long res;

// 有点类似希尔排序，按照间隔为 d 分组排序
// 如果分组排序后，是从小到大排列，就说明排序成功

long gcd(long a, long b) {
    return b == 0 ? a : gcd(b, a % b);
}

void solve() {
    std::cin >> n;
    vt.clear(); ds.clear(); res = 0;
    for (long i = 1; i <= n; i ++) on[i] = 0;
    for (long i = 1; i <= n; i ++) std::cin >> a[i];
    for (long i = 1; i <= n; i ++) {
        if (on[i]) continue;
        vt.clear();
        long t = i;
        while (on[t] == 0) {
            vt.push_back(t);
            on[t] = 1;
            t = a[t];
        }
        if (vt.size() > 1) {
            std::sort(vt.begin(), vt.end());
            for (long i = 1; i < vt.size(); i ++) {
                ds.push_back(vt[i] - vt[i - 1]);
            }
        }
    } 
    if (ds.size() == 0) {
        std::cout << n << '\n'; return;
    }
    res = ds.front();
    for (long i : ds) {
        res = gcd(res, i);
    }
    std::cout << res << '\n';
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