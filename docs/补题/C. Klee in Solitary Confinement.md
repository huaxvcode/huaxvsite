# [C. Klee in Solitary Confinement](https://codeforces.com/gym/103470/problem/C)


```cpp
#include <bits/stdc++.h>

const int N = 4e6 + 100;
const int M = 2e6 + 10;
int n, k, res;
int a[N];
std::vector<int> mp[N];

int find(const std::vector<int>& vt, int x) {
    if (vt.size() == 0) return -1;
    int l = 0, r = vt.size() - 1, mid;
    while (l < r) {
        mid = (l + r) >> 1;
        if (vt[mid] < x) l = mid + 1;
        else r = mid;
    }
    if (vt[r] == x) return r;
    return -1;
}

int get(int x) {
    if (mp[x - k + M].size() == 0) return mp[x + M].size();
    std::vector<int> vt = mp[x + M];
    vt.insert(vt.end(), mp[x - k + M].begin(), mp[x - k + M].end());
    std::sort(vt.begin(), vt.end());
    std::vector<int> st(vt.size());
    for (int i = 0; i < st.size(); i ++) {
        if (find(mp[x + M], vt[i]) > -1) st[i] = -1;
        else st[i] = 1;
    }
    int mx = 0, t = 0, l = 0, r = 0;
    while (r < st.size()) {
        if (t + st[r] >= 0) {
            t += st[r];
            mx = std::max(mx, t);
        }
        else {
            t = 0;
            l = r + 1;
        }
        r ++;
    }
    return mx + mp[x + M].size();
}

std::set<int> set;

void solve() {
    std::cin >> n >> k;
    for (int i = 1; i <= n; i ++) std::cin >> a[i];
    for (int i = 1; i <= n; i ++) mp[a[i] + M].push_back(i);
    for (int i = 1; i <= n; i ++) set.insert(a[i]);
    for (auto x : set) {
        res = std::max(res, get(x));
    }
    std::cout << res << '\n';
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);

    solve();
    return 0;
}
```