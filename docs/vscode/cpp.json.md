# cpp.json

```json
{
    // Place your snippets for cpp here. Each snippet is defined under a snippet name and has a prefix, body and 
    // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
    // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
    // same ids are connected.
    // Example:
    "code": {
        "prefix": "code",
        "body": [
            "#include <bits/stdc++.h>",
            "typedef long long var;",
            "typedef __int128 vhh;",
            "",
            "namespace {",
            "",
            "${0}",
            "",
            "void solve() {",
            "    ",
            "}",
            "",
            "}",
            "",
            "// g++ -std=c++17 $TM_FILENAME_BASE.cpp -o $TM_FILENAME_BASE",
            "int main() {",
            "    std::ios::sync_with_stdio(0);",
            "    std::cin.tie(0); std::cout.tie(0);",
            "    std::random_device rd;",
            "    std::mt19937 mt(rd());",
            "    srand(mt());",
            "    int t = 1; ",
            "    // std::cin >> t;",
            "    for (int i = 1; i <= t; i ++) {",
            "        // std::cout << \"Case #1: \";",
            "        solve();",
            "    }",
            "    return 0;",
            "}",
            
        ],
        "description": "Log output to console"
    }
}

```
