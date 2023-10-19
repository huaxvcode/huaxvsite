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

## mkdir

```bash
# 创建文件夹
mkdir dir

# 递归创建文件夹
mkdir dir/dir/dir
```

## rm

```bash
# 删除文件夹
rm -r dir 

# 强制删除文件夹
rm -rf dir 

# 强制删除文件
rm -f file
```

## cp

```bash
# 递归复制目录，将 dir1 复制进 dir2 里面
cp -r dir1 dir2 # dir2/dir1

# 强制复制
cp -rf dir1 dir2 
```

## mv

```bash
# 强制移动，将 dir1 移动到 dir2 里面
# 如果 dir2 不存在就是改名
mv -f dir1 dir2
```

## touch 

```bash
# 创建空文件，如果文件存在不执行如何操作
touch file
```

## find

```bash
# 在 dir 文件夹里查找权限为 777 的文件
find dir -perm 777

# 在 dir 文件夹里查找名称为 name 的文件
# find . -name *
find dir -name name

# 按照大小查找文件
# 查找 dir 目录下大小超过 100 MB 的文件
# M、k、c 分别代表 MB、kB、cB
find dir -size +100M
find dir -size -100M
```

## zip、unzip

压缩成 zip 格式

```bash
# 不显示具体过程加：-q
# 将文件压缩成 name.zip
zip -r name.zip file

# 将文件夹 dir 下的所有内容压缩成 name.zip
zip -r name.zip dir
```

解压 zip 格式

```bash

```
