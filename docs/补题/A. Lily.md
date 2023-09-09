# [A. Lily](https://codeforces.com/gym/104008/problem/A)

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

namespace code {
    
    long n; std::string s;
    std::string res;
    void solve() {
        std::cin >> n >> s;
        for (long i = 1; i <= n; i ++) res += "C";
        for (long i = 0; i < n; i ++) {
            if (s[i] == 'L') {
                if (i - 1 >= 0 && res[i - 1] == 'C') res[i - 1] = '.';
                if (i + 1 < n && res[i + 1] == 'C') res[i + 1] = '.';
                res[i] = s[i];
            }
        }
        std::cout << res << '\n';
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