# neovim

## 安装 neovim

```bash
sudo apt-get-repository ppa:neovim-ppa/stable
sudo apt-get update
sudo apt-get install -y neovim
```

## 普通模式下

### 上下左右

```
h       左

j       下

k       上

l       右
```

### 多行跳跃、多格跳跃

```
4h      向左边跳 4 格

4j      向下跳 4 行

4k      向上跳 4 行

4l      向右跳 4 格
```

### 单词跳跃

```
b       上一个单词，last beginning

w       下一个单词，next word
```

### 回到文档的最上方

```
gg      回到文档的最上方
```

### 回到文档的末尾

```
G       到文档的末尾
```

### 翻页

```
ctrl + u    向上翻页

ctrl + d    向下翻页
```

### 到下一个字母处

```
fr      到下一个字符 r 处

fl      到下一个字符 l 处
```

### 复制

```
yaw     复制整个单词


y4j     向下复制 4 行


y4k     向上复制 4 行
```

### 删除

```
daw     删除整个单词


d4j     向下删除 4 行


d4k     向上删除 4 行
```


### 撤销

```
u       撤销
```
