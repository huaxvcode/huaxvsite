# [H. Mad City](https://codeforces.com/problemset/problem/1873/H)

如果只有一个环，只需要 `dfs` 两次就可以获取该环的环路

```cpp
#include <bits/stdc++.h>
typedef long long var;
typedef __int128 hh;

namespace {

const var N = 2e6;
var n, a, b;
std::vector<var> g[N];
var on[N];
var lu, lv;
std::set<var> set;

void add(var x, var y) {
	g[x].push_back(y);
}

void dfs1(var u, var fa) {
	if (on[u]) { lu = u; lv = fa; return; }
	on[u] = 1;
	for (auto v : g[u]) {
		if (v == fa) continue;
		dfs1(v, u);
	}
}

void dfs2(var u, var fa) {
	set.insert(u);
	if (u == lv) return;
	var st = 0;
	for (auto v : g[u]) {
		if (v == fa) continue;
		if (v == lv) {
			st = 1; continue;
		}
		dfs2(v, u);
	}
	if (st) dfs2(lv, u);
	set.erase(u);
}

void solve() {
	std::cin >> n >> a >> b;
	set.clear();
	for (var i = 0; i <= n; i ++) g[i].clear(), on[i] = 0;
	for (var i = 1; i <= n; i ++) {
		var x, y; std::cin >> x >> y;
		add(x, y); add(y, x);
	}
	dfs1(b, 0); dfs2(lu, 0);
	std::queue<std::pair<var, var>> qu;
	qu.push({b, 0});
	std::memset(on, 0, sizeof(var) * (n + 1));
	var p_, d_;
	
	while (qu.size()) {
		auto [x, y] = qu.front(); qu.pop();
		if (on[x]) continue;
		on[x] = 1;
		if (set.count(x)) {
			p_ = x; d_ = y;
			break;
		}
		for (auto v : g[x]) {
			qu.push({v, y + 1});
		}
	}
	while (qu.size()) qu.pop();
	var dd_;
	qu.push({a, 0});
	std::memset(on, 0, sizeof(var) * (n + 1));
	while (qu.size()) {
		auto [x, y] = qu.front(); qu.pop();
		if (on[x]) continue;
		on[x] = 1;
		if (x == p_) {
			dd_ = y; break;
		}
		for (auto v : g[x]) {
			qu.push({v, y + 1});
		}
	}
	if (dd_ <= d_) std::cout << "NO\n";
	else std::cout << "YES\n";
}

}

// g++ -w -std=c++20 -O2 Main.cpp -o Main -pthread && ./Main
int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0); std::cout.tie(0);
	srand(time(0));
	int t; std::cin >> t; while (t --)
	solve();
	return 0;
}

```
