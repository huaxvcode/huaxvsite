# [Oops, It's Yesterday Twice More](https://codeforces.com/gym/103470/problem/A)

```cpp
#include <bits/stdc++.h>

int n, x, y; 

std::vector<std::string> v;
std::vector<std::pair<long long, long long>> pos;

std::string get(const std::string& s, int ts) {
    std::string res;
    while (ts -- > 0) res += s;
    return res;
}

std::string get(int x1, int y1, int x2, int y2) {
    std::string res;
    if (x1 <= x2) res += get("D", x2 - x1);
    else res += get("U", x1 - x2);
    if (y1 <= y2) res += get("R", y2 - y1);
    else res += get("L", y1 - y2);
    return res;
}

void solve() {
    std::cin >> n >> x >> y;
    std::string res;
    pos = {
        {1, 1}, {1, n}, {n, 1}, {n, n}
    };
    for (auto [x1, y1] : pos) {
        for (auto [x2, y2] : pos) {
            if (x1 == x2 || y1 == y2) continue;
            res = get(x1, y1, x2, y2) + get(x2, y2, x, y);
            if (res.size() <= 3 * n - 3) {
                std::cout << res << '\n';
                return;
            }
        }
    }
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0); std::cout.tie(0);
    
    solve();
    return 0;
}

```