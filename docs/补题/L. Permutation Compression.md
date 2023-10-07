# [L. Permutation Compression](https://codeforces.com/gym/104172/problem/L)

搜索树、线段树、树状数组贪心地删除区间最大元素以保留最大值问题

如果一个区间 $[l, r]$ 的最大值一定要保留，那么要删除其他元素时，只能以最大值为分割点分成两个区间继续删，不能包含最大值；

如果一个区间的最大值可以删除，那么就删除该最大值，剩下元素合并。

```cpp
#include <bits/stdc++.h>
typedef int var;
typedef __int128 hh;

class FHQ
{
private:

    const var _size_;
    std::vector<var> val, key;
    std::vector<var> ls, rs;
    std::vector<var> size;
    std::vector<var> space;

    var ant;
    var root;

public:  

    FHQ(var N = 2e6) : _size_(N), 
    val(_size_, 0), key(_size_, 0), 
    ls(_size_, 0), rs(_size_, 0), 
    size(_size_, 0), 
    space(_size_, 0), 
    ant(0), root(0)
    {
        srand(time(0));

        for (var i = 1; i < _size_ - 10; i ++)
        {
            space[++ ant] = i;
        }
    }

private:

    var get()
    {
        return space[ant --];
    }

    void del(var pos)
    {
        val[pos] = 0; key[pos] = 0;
        ls[pos] = 0; rs[pos] = 0;
        size[pos] = 0;
        space[++ ant] = pos;
    }

    void push_up(var rt)
    {
        if (rt == 0) return;
        size[rt] = 1 + size[ls[rt]] + size[rs[rt]];
    }

    void split(var rt, var x, var& l, var& r)
    {
        if (rt == 0) { l = r = 0; return; }
        if (val[rt] < x)
        {
            l = rt;
            split(rs[rt], x, rs[rt], r);
        }
        else
        {
            r = rt;
            split(ls[rt], x, l, ls[rt]);
        }
        push_up(l);
        push_up(r);
    }

    void meld(var& rt, var l, var r)
    {
        if (l == 0 || r == 0)
        {
            rt = l + r;
            push_up(rt);
            return;
        }

        if (key[l] >= key[r])
        {
            rt = l;
            meld(rs[rt], rs[rt], r);
        }
        else 
        {
            rt = r;
            meld(ls[rt], l, ls[rt]);
        }

        push_up(rt);
    }

    // 查找第 k 大
    var kth(var root, var k)
    {
        var t = size[ls[root]] + 1;
        if (k == t) return val[root];
        else if (k > t) return kth(rs[root], k - t);
        else return kth(ls[root], k);
    }

    void clear(var root)
    {
        if (root == 0) return;
        clear(ls[root]);
        clear(rs[root]);
        del(root);
    }

public:

    // 插入元素 x
    void insert(var x)
    {
        var l, r;
        split(root, x, l, r);
        var p = get();
        val[p] = x;
        key[p] = rand();
        size[p] = 1;
        meld(root, l, p);
        meld(root, root, r);
    }

    // 删除一个元素 x
    void erase(var x)
    {
        var l, r;
        split(root, x, l, r);
        var p, q;
        split(r, x + 1, p, q);
        if (p)
        {
            var l = ls[p], r = rs[p];
            del(p);
            meld(p, l, r);
        }
        meld(root, l, p);
        meld(root, root, q);
    }

    // 元素个数
    var length()
    {
        return size[root];
    }

    // 比 x 小的元素个数
    var nleft(var x)
    {
        var l, r;
        split(root, x, l, r);
        var res = size[l];
        meld(root, l, r);
        return res;
    }

    // 比 x 小或等的元素个数
    var nleq(var x)
    {
        return nleft(x + 1);
    }

    // 比 x 大的元素个数
    var nright(var x)
    {
        return length() - nleq(x);
    }

    // 比 x 大或等的元素个数
    var nreq(var x)
    {
        return length() - nleft(x);
    }

    // 查找第 k 大
    var knum(var k)
    {
        if (k > length()) exit(1);
        return kth(root, k);
    }

    // 删除第 k 大
    void dknum(var k)
    {
        if (k > length()) exit(1);
        erase(knum(k));
    }

    void clear()
    {
        clear(root);
        root = 0;
    }

    // 查找左边第一个比 x 小的数
    var pre(var x)
    {
        if (nleft(x) == 0) exit(1);
        return knum(nleft(x));
    }

    // 查找右边第一个比 x 大的数
    var nxt(var x)
    {
        if (nleq(x) == length()) exit(1);
        return knum(nleq(x) + 1);
    }

    // 统计 l <= x <= r 的元素个数
    var count(var l, var r)
    {
        var x, y, z;
        split(root, l, x, y);
        split(y, r + 1, y, z);
        var t = size[y];
        meld(root, x, y);
        meld(root, root, z);
        return t;
    }

    // 删除 l <= x <= r 的区间
    void del(var l, var r)
    {
        var x, y, z;
        split(root, l, x, y);
        split(y, r + 1, y, z);
        clear(y);
        meld(root, x, z);
    }

    // 删除 <= x 的一段
    void del_pre(var x)
    {
        var l, r;
        split(root, x + 1, l, r);
        clear(l);
        l = 0;
        meld(root, l, r);
    }

    // 删除 >= x 的一段
    void del_post(var x)
    {
        var l, r;
        split(root, x, l, r);
        clear(r);
        r = 0;
        meld(root, l, r);
    }
};


namespace {
const var ninf = 1 << 31;
const var inf = ~(1 << 31);
const var N = 2e5 + 10;
var debug;
var n, m, k;
var a[N], b[N], c[N];
var on[N];
FHQ set;

var cs[N];
var lowbit(var x) { return x & -x; }
void update(var p, var x) {
    while (p <= n) {
        cs[p] += x;
        p += lowbit(p);
    }

}
var sum(var p) {
    var ans = 0;
    while (p) {
        ans += cs[p];
        p -= lowbit(p);
    }
    return ans;
}
var sum(var l, var r) {
    auto ans = sum(r) - sum(l - 1);
    return ans;
}

#define x_ first
#define y_ second
std::pair<var, var> tr[N << 2];
std::pair<var, var> None = { -1, -1 };
inline var ls(var p) { return p << 1; }
inline var rs(var p) { return p << 1 | 1; }
void push_up(var p, var l, var r) {
    if (l == r) return;
    if (tr[ls(p)].x_ > tr[rs(p)].x_) tr[p] = tr[ls(p)];
    else tr[p] = tr[rs(p)];
}
void build(var p, var l, var r) {
    if (l == r) { tr[p].x_ = a[l]; tr[p].y_ = l; return; }
    var mid = (l + r) >> 1;
    build(ls(p), l, mid);
    build(rs(p), mid + 1, r);
    push_up(p, l, r);
}
auto query(var p, var l, var r, var ll, var rr) {
    if (ll <= l && r <= rr) return tr[p];
    var mid = (l + r) >> 1;
    auto ans = None;
    if (ll <= mid) ans = query(ls(p), l, mid, ll, rr);
    if (rr > mid) {
        auto t = query(rs(p), mid + 1, r, ll, rr);
        if (t.x_ > ans.x_) ans = t;
    }
    return ans;
}
void modify(var p, var l, var r, var pos, auto val) {
    if (l == r) { tr[p] = val; return; }
    var mid = (l + r) >> 1;
    if (pos <= mid) modify(ls(p), l, mid, pos, val);
    else modify(rs(p), mid + 1, r, pos, val);
    push_up(p, l, r);
}

var read()
{
    register var x = 0, f = 1;
    register char c = getchar();
    while (!(c >= '0' && c <= '9'))
    {
        if (c == '-') f = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9')
    {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x * f;
}


void solve() {
    
    n = read(); m = read(); k = read();
    {
        for (var i = 1; i <= n; i ++) on[i] = 0;
        for (var i = 1; i <= n; i ++) cs[i] = 0;
        set.clear();
    }
    
    {
        auto f = [&](auto a, auto len) -> void {
            for (var i = 1; i <= len; i ++) a[i] = read();
        };
        f(a, n);
        f(b, m);
        f(c, k);
        var i = 1, j = 1;
        while (i <= m) {
            while (j <= n && b[i] != a[j]) j ++;
            if (j > n) { puts("NO"); return; }
            i ++;
        }
    }
    
    for (var i = 1; i <= k; i ++) set.insert(c[i]);
    
    auto kill = [&](var x) -> bool {
        if (set.nleft(x + 1) == 0) return false;
        auto t = set.pre(x + 1);
        set.erase(t);
        return true;
    };

    {
        build(1, 1, n);
        for (var i = 1; i <= m; i ++) on[b[i]] = 1;
        for (var i = 1; i <= n; i ++) update(i, 1);
    }
    
    std::queue<std::pair<var, var>> qu;
    qu.push({1, n});
    
    while (qu.size()) {
        auto [l, r] = qu.front(); qu.pop();
        auto t = query(1, 1, n, l, r);
        if (t.x_ == -1) continue;
        if (on[t.x_]) {
            auto m1 = t.y_ - 1, m2 = t.y_ + 1;
            if (m1 >= l) qu.push({l, m1});
            if (m2 <= r) qu.push({m2, r});
        }
        else {
            if (kill(sum(l, r))) {
                on[t.x_] = 1;
                modify(1, 1, n, t.y_, None);
                update(t.y_, -1);
                if (sum(l, r)) qu.push({l, r});
            }
            else {
                // std::cout << l << ' ' << r << '\n';
                // break;
            }
        }
    }
    // for (var i = 1; i <= n; i ++) std::cout << on[i] << ' '; std::cout << '\n';
    for (var i = 1; i <= n; i ++) if (on[i] == 0) 
        {puts("NO"); return;}
    puts("YES");
}

}

// g++ -std=c++20 Main.cpp -o Main && Main
int main() {
    // std::ios::sync_with_stdio(0);
    // std::cin.tie(0); std::cout.tie(0);
    int t; std::cin >> t; while (t --)
    solve();
    return 0;
}
```
