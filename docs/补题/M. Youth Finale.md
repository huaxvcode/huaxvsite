# [M. Youth Finale](https://codeforces.com/gym/104008/problem/M)

如果长度为 $n$ 的数组 $a$ 的逆序对数量求出来了，翻转数组 $a$ 后的逆序对数量是多少呢？

> $n * (n - 1) / 2 - 逆序对数量(a)$

如果长度为 $n$ 的数组 $a$ 的逆序对数量求出来了，对数组左移一位，逆序对的数量又是多少呢？

左移时，只有第一个元素需要移动到末尾处，其他保持原顺序不变，那么删掉第一个元素时，会少多少个逆序对的数量呢？在末尾添加首元素后，又会增加多少逆序对的数量呢？

这些都是 `huaxv` 要解决的疑问！

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

namespace code {
    
    const long N = 5e5;
    long n, m;
    std::string s;
    long a[N], a_[N];
    std::deque<long> qu;
    long mo;
    long now;
    
    long msort(long l, long r) {
        if (l >= r) return 0;
        long mid = (l + r) >> 1;
        long res = 0;
        res += msort(l, mid);
        res += msort(mid + 1, r);
        long i = l, j = mid + 1, k = 0;
        while (i <= mid && j <= r) {
            if (a[i] > a[j]) res += mid - i + 1, a_[++ k] = a[j ++];
            else a_[++ k] = a[i ++];
        }
        while (i <= mid) a_[++ k] = a[i ++];
        while (j <= r) a_[++ k] = a[j ++];
        i = l, j = 1;
        for (; j <= k; j ++, i ++) a[i] = a_[j];
        return res;
    }
    
    long lf(long x) {
        long l = 1, r = n, mid;
        while (l < r) {
            mid = (l + r) >> 1;
            if (a[mid] < x) l = mid + 1;
            else r = mid;
        }
        if (a[r] >= x) return r;
        else return -1;
    }
    
    long rf(long x) {
        long l = 1, r = n, mid;
        while (l < r) {
            mid = (l + r + 1) >> 1;
            if (a[mid] <= x) l = mid;
            else r = mid - 1; 
        }
        if (a[l] <= x) return l;
        else return -1;
    }
     
    void solve() {
        std::cin >> n >> m;
        for (long i = 1; i <= n; i ++) std::cin >> a[i];
        for (long i = 1; i <= n; i ++) qu.push_back(a[i]);
        std::cin >> s;
        now = msort(1, n);
        std::cout << now << '\n';
        for (auto c : s) {
            if (c == 'R') {
                mo ++;
                now = n * (n - 1) / 2 - now;
                std::cout << now % 10;
            }
            else {
                if (mo % 2 == 0) {
                    long mi = rf(qu.front() - 1); 
                    mi = (mi == -1 ? 0 : mi);
                    long mx = lf(qu.front() + 1);
                    mx = (mx == -1 ? 0 : n - mx + 1);
                    now = now + mx - mi;
                    std::cout << now % 10;
                    qu.push_back(qu.front());
                    qu.pop_front();
                }
                else {
                    long mi = rf(qu.back() - 1); 
                    mi = (mi == -1 ? 0 : mi);
                    long mx = lf(qu.back() + 1);
                    mx = (mx == -1 ? 0 : n - mx + 1);
                    now = now + mx - mi;
                    std::cout << now % 10;
                    qu.push_front(qu.back());
                    qu.pop_back();
                }
            }
        }
        std::cout << '\n';
    }
    
}

void solve() {
    
}

// g++ -std=c++20 Main.cpp -o Main && ./Main
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    //long t; std::cin >> t; while (t --)
    code::solve();
    return 0;
}

```