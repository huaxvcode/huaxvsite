# [D. Balanced Round](https://codeforces.com/problemset/problem/1850/D)

从小到大排序，先求出连续成立的最大长度

在对剩下的元素从最小的开始求出最大长度，不断重复此过程

答案就是这些长度的最大值

---

为什么成立呢？如果第一步求出来后，需要从剩下的部分求出最大长度，那么这部分无论哪一个元素都不能放入第一部分，因为差值大于 $k$，就相当于是独立出来了。

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

const long N = 3e5;
long n, k;
long a[N];
long res;

long rf(long x) {
    long l = 1, r = n, mid;
    while (l < r) {
        mid = (l + r + 1) >> 1;
        if (a[mid] <= x) l = mid;
        else r = mid - 1;
    }
    if (a[l] <= x) return l;
    return 0;
}

void solve() {
    res = 0;
    std::cin >> n >> k;
    for (long i = 1; i <= n; i ++) std::cin >> a[i];
    std::sort(a + 1, a + 1 + n);
    for (long i = 1; i <= n; i ++) {
        long l = i;
        long p = i;
        while (l <= n) {
            long r = rf(a[l] + k);
            res = std::max(res, r - p + 1);
            if (r != l) l = r;
            else break;
        }
        i = l;
    }
    std::cout << n - res << '\n';
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    long t; std::cin >> t; while (t --)
    solve();
    return 0;
}

```