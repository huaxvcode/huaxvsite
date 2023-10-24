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

举例：

```bash
ssh huaxvtemp@192.168.109.128 -p 16610

# 或者
sudo vim ~/.ssh/config

Host huaxvtemp
    HostName 192.168.109.128
    User huaxvtemp
    Port 16610
    
# 下次就可以直接用别名登陆
ssh huaxvtemp
```

## 密钥登陆

本地机创建密钥：

```bash
# 默认在 ~/.ssh/ 创建
ssh-keygen

#   id_rsa      私钥
#   id_rsa.pub  公钥
```
如果想免密码登陆远程服务器，只需要将本地机的公钥传给服务器就行

```bash
# 将公钥的内容复制到
~/.ssh/authorized_keys

# 或者
ssh-copy-id user@hostname
```
