# ssh

## 密码连接

输入下面命令，会提示你输入密码登陆

```bash
ssh user@hostname

ssh user@hostname -p port # 以特定端口号登录，默认是 22
```

## 便捷登陆

```bash
sudo vim ~/.ssh/config

Host 服务器别名
    HostName IP地址或域名
    User 用户名
    Port 端口号

Host 服务器别名
    HostName IP地址或域名
    User 用户名
```

下次登陆时就可以直接使用别名登陆：

```bash
ssh 别名
```
