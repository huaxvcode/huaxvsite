# [B. Come Together](https://codeforces.com/problemset/problem/1845/B)

```cpp
#include <bits/stdc++.h>
#define long long long
#define bint __int128

long xa, ya;
long xb, yb;
long xc, yc;

long dbx, dby;
long dcx, dcy;

long res;

void solve() {
    res = 1;
    
    std::cin >> xa >> ya 
            >> xb >> yb 
            >> xc >> yc;
    dbx = xb - xa;
    dby = yb - ya;
    
    dcx = xc - xa;
    dcy = yc - ya;
    
    if (dbx >= 0 && dcx >= 0) res += std::min(dbx, dcx);
    if (dbx <= 0 && dcx <= 0) res += std::min(-dbx, -dcx);
    if (dby >= 0 && dcy >= 0) res += std::min(dby, dcy);
    if (dby <= 0 && dcy <= 0) res += std::min(-dby, -dcy);
    
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