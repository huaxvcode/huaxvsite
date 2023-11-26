# java.json


```json
{
	// Place your snippets for java here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	"Print to console": {
		"prefix": "code",
		"body": [
			"import java.util.*;",
			"import java.io.*;",
			"import java.math.*;",
			"",
			"public class $TM_FILENAME_BASE {",
			"",
			"    final int N = 500000; // 1e6 已经快超时了",
			"",
			"    ${0}",
			"",
			"    public void solve() throws Exception {",
			"",
			"    }",
			"",
			"    public static void main(String[] args) throws Exception {",
			"        $TM_FILENAME_BASE cmd = new $TM_FILENAME_BASE();",
			"        cmd.solve(); cout.flush();",
			"    }",
			"",
			"    public static String space = \"\\\\\\s+\"; ",
			"",
			"    public static BufferedReader cin = new BufferedReader(new InputStreamReader(System.in));",
			"    public static PrintWriter cout = new PrintWriter(new OutputStreamWriter(System.out));",
			"",
			"    public static String[] gss() throws Exception {",
			"        return cin.readLine().split(space);",
			"    }",
			"",
			"    public static int gii(String s) {",
			"        return Integer.parseInt(s);",
			"    }",
			"",
			"    public static long gll(String s) {",
			"        return Long.parseLong(s);",
			"    }",
			"",
			"    public static double gff(String s) {",
			"        return Double.parseDouble(s);",
			"    }",
			"}",
			
		],
		"description": "Log output to console"
	}
}
```
