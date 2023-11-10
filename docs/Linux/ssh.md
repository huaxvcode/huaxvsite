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

## scp 传文件

```bash
# 将 path1 下的文件传入到 path2 中
scp path1 path2
```

举例

```bash
## 将文件夹 tmp 复制到 myserver:/home/acs/ 目录下
scp -r ~/tmp myserver:/home/acs/

## 将文件复制到当前目录下
scp huaxvcode:/home/huaxvcode/huaxvubuntu-2023.11.4.tar .
```

## ssh 连接 ubuntu

修改 dns：

```bash
vim /etc/systemd/resolved.conf

DNS=8.8.8.8 114.114.115.115
FallbackDNS=8.8.8.8

# 然后重启
reboot
```

```bash
sudu su
sudo apt install openssh-server

/etc/init.d/ssh start
```

```bash
sudo vim /etc/ssh/sshd_config

Port 16610
PermitRootLogin yes
PasswordAuthentication yes

sudo /etc/init.d/ssh restart
```

```bash
apt install net-tools

# 查看 ip 地址
ifconfig
```

## powershell

```bash
function ssh-copy-id([string]$userAtMachine, $args){   
    $publicKey = "$ENV:USERPROFILE" + "/.ssh/id_rsa.pub"
    if (!(Test-Path "$publicKey")){
        Write-Error "ERROR: failed to open ID file '$publicKey': No such file"            
    }
    else {
        & cat "$publicKey" | ssh $args $userAtMachine "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys || exit 1"      
    }
}
```

```bash
ssh-copy-id -p 16610 huaxvubuntu@192.168.109.128
```

vscode：

```bash
Host 192.168.109.128
  HostName 192.168.109.128
  User huaxvubuntu
  Port 16610
```

