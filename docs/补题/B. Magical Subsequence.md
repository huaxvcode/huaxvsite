# [B. Magical Subsequence](https://codeforces.com/gym/103447/problem/B)

## 题目描述：

给定长度为 $n$ 的序列 $a[n]$，请找出这样的子序列：

> $a[b_1], a[b_2], a[b_3], \cdots, a[b_m]$

满足：

> $a[b_1] + a[b_2] = a[b_3] + a[b_4] = \cdots = a[b_{m - 1}] + a[b_m]$ 
>
> $1 \leq b_1 < b_2 < \cdots < b_m \leq n$

求 $m$ 的最大值；

## 思路：

因为 $1 \leq a[i] \leq 100$，所以对于任意一对 $2 \leq a[i] + a[j] \leq 200$

暴力枚举相加的值，寻找最长的子序列

时间复杂度：$200n$

```cpp
#include <bits/stdc++.h>
typedef long long ll;
namespace {

	const ll N = 2e5;
	ll pos[300];
	ll n;
	ll a[N];
	ll res;

	void solve() {
		std::cin >> n;
		for (ll i = 1; i <= n; i ++) std::cin >> a[i];
		for (ll i = 2; i <= 200; i ++) {
			ll m = 0;
            std::memset(pos, 0, sizeof pos);
            ll cur = 0;
			for (ll j = 1; j <= n; j ++) {
				if (i - a[j] < 0) {
                    pos[a[j]] = j;
                }
                else if (pos[i - a[j]] > cur) {
                    m ++; cur = j;
                }
                else pos[a[j]] = j;
			}
			res = std::max(res, m * 2);
		}
		std::cout << res << '\n';
	}
}

int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	solve();
	return 0;
}
```
