# oj

## 功能

### oj get

使用 `Random` 和 `Answer` 随机生成一个数据点，将 `Random` 文件的输出重定向到 `in.in` ，将 `Answer` 的输出重定向到 `out.out`

### oj new

使用 `Random` 和 `Answer` 随机生成 10 个数据点，将 `Random` 文件的输出重定向到 `.in` 后缀，将 `Answer` 的输出重定向到 `.out` 后缀，应该以 `in_1.in`、`out_1.out` 一直到 `in_10.in`、`out_10.out` 来命名.

### oj 1000

对拍 1000 次

### oj language code

按照 language 来识别是哪种文件，并编译和运行

以 `in.in` 作为输入，输出到 `run.run` 文件中，并与 `out.out` 文件做对比

### oj cp language code

编译语言为 language 的代码

### oj rn language code

运行一次语言为 language 的代码，以 `in.in` 作为输入，`run.run` 作为输出，并于 `out.out` 文件做对比

### oj lang1 lang2 lang3 1000

支持对文件 `Random.lang1`、`Answer.lang2`、`Main.lang3` 对拍 1000 次

### oj save language code

以覆盖式备份一个文件名为 `code.language` 的内容

### oj get language code

将之前的备份取出来放到 `code.language` 文件中

### 特殊说明

如果文件为 `Random` 开头的，重定向输出到 `in.in` 文件；

如果文件为 `Answer` 重定向输出到 `out.out` 文件；

强制要求，文件名不能以 `cpp`、`java`、`py`、`oj`、`cp`、`rn` 作为开头

### 具体实现

```cpp
# 负责文件的编译
void compiler(language, filename);

# 运行指定文件
void run(language, filename, str="");

# 创建一个线程池函数
void threads(auto...args);
```
