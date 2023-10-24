# scp

复制文件到「远程服务器」

或者复制「远程服务器」文件到「本地机」

`scp` 功能类似 `cp` 命令

```bash
scp -r dir 远程服务器别名:dir

scp -r 远程服务器别名:dir dir

# 有时需要指定端口号：

scp -p 16610 -r dir 远程服务器别名:dir

scp -p 16610 -r 远程服务器别名:dir dir
```

举例：

```bash
scp -r huaxv huaxvtemp:huaxv

scp -r huaxvtemp:test test
```
