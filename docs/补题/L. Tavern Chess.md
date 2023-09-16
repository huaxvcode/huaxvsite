# [L. Tavern Chess](https://codeforces.com/gym/104160/problem/L)

```cpp
#include <bits/stdc++.h>
#define ll long long
#define vll std::vector<ll>

namespace {

	ll n, m;
	vll a, ca, ha, b, cb, hb;
	double wa, wb, tie;

	void init(vll& a, vll& ca, vll& ha, ll& n) {
		ll i = 0, j = 1;
		while (j <= n) {
			if (a[j] <= 0) j ++;
			else {
				++ i;
				a[i] = a[j];
				ca[i] = ca[j];
				ha[i] = ha[j];
				j ++;
			}
		}
		n = i;
	}

	ll get(const vll& a, const vll& ca, ll n) {
		ll p = 0, mi = 1e9;
		for (ll i = 1; i <= n; i ++) {
			if (ca[i] < mi) {
				mi = ca[i];
				p = i;
			}
		}
		return p;
	}

	void dfs(vll a, vll ca, vll ha, ll n, double& wa, vll b, vll cb, vll hb, ll m, double& wb, double f) {
		init(a, ca, ha, n); 
		init(b, cb, hb, m);
		if (n == 0 && m == 0) {
			tie += f;
			return;
		}
		if (n == 0) {
			wb += f; return;
		}
		if (m == 0) {
			wa += f; return;
		}
		f /= m;
		ll p = get(a, ca, n);
		for (ll i = 1; i <= m; i ++) {
			a[p] -= hb[i];
			b[i] -= ha[p];
			ca[p] ++;
			// cb[i] ++;
			dfs(b, cb, hb, m, wb, a, ca, ha, n, wa, f);
			a[p] += hb[i];
			b[i] += ha[p];
			ca[p] --;
			// cb[i] --;
		}
	}

	void solve() {
		scanf ("%lld%lld", &n, &m);
		a.push_back(0);
		ca.push_back(0);
		ha.push_back(0);
		b.push_back(0);
		cb.push_back(0);
		hb.push_back(0);
		for (ll i = 1; i <= n; i ++) {
			ll t; scanf ("%lld", &t);
			a.push_back(t);
			ca.push_back(0);
			ha.push_back(t);
		}
		for (ll i = 1; i <= m; i ++) {
			ll t; scanf ("%lld", &t);
			b.push_back(t);
			cb.push_back(0);
			hb.push_back(t);
		}
		if (n > m) dfs(a, ca, ha, n, wa, b, cb, hb, m, wb, 1);
		else if (n < m) dfs(b, cb, hb, m, wb, a, ca, ha, n, wa, 1);
		else {
			dfs(a, ca, ha, n, wa, b, cb, hb, m, wb, 0.5);
			dfs(b, cb, hb, m, wb, a, ca, ha, n, wa, 0.5);
		}
		// dfs(b, cb, hb, m, wb, a, ca, ha, n, wa, 0.5);
		printf ("%.13f\n%.13f\n%.13f\n", wa, wb, tie);
	}
}

int main() {
	// std::ios::sync_with_stdio(0);
	// std::cin.tie(0);
	// std::cout.tie(0);

	solve();
	return 0;
}
```
