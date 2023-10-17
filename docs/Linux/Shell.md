# Shell

## 简单入门

```bash
#!/bin/bash

echo "hello world";
```

## 关机

```bash
# 立刻关机
poweroff

# 立刻关机
hudo halt

# 23:30 才关机
sudo shutdown -h 23:30
```

## 重启

```bash
reboot

# 23:30 才重启
sudo shutdown -r 23:30
```

## 修改用户名

```bash
# 找到用户名并修改
vim /etc/shadow
vim /etc/group

reboot
```

## 取变量值

```bash
# 取变量值
$var

#统计个数
$#vars
```

## 控制结构

```bash
if 条件; then
    语句
elif 条件; then
    语句
else 
    语句
fi;
```

```bash
for 变量名 in 列表; do
    语句
done;
```

```bash
for (语句; 语句; 语句) do
    语句
done;
```

```bash
while 条件; do
    语句
done;
```

## tree

```bash
# 显示目录树
# 限制 3 层显示目录树
tree -L 3 dir_name
```

## pwd

```bash
# 显示当前的工作目录
pwd
```

## ls

```bash
# 列出目录和文件
ls -F dir_name

# 列出最详细的信息
ls -l dir_name 

# 列出文件的大小
ls -h dir_name
```

## cat

```bash
# 显示出 f1 f2 f3 的文件内容
cat f1 f2 f3
```

# 
