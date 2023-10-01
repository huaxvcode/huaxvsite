# vscode 连接 ubuntu20.04

## 安装 ubuntu20.04 子系统

powershell 运行：

```shell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```


## 换源

```shell
sudo su

vim /etc/apt/sources.list
```

复制清华源 (20.04)

```shell
# 清华镜像
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```

## 更新源

```shell
sudo apt-get update
sudo apt-get upgrade
```

## 安装 openssh-server

```shell
sudo apt install openssh-server
```

## 开启服务

```shell
/etc/init.d/ssh start
```

## 修改 sshd_config

```shell
sudo vim /etc/ssh/sshd_config

Port 22
PermitRootLogin yes
PasswordAuthentication yes

sudo /etc/init.d/ssh restart
```

![](./img/修改.png)
![](./img/修改2.png)

## ifconfig 查看 ip 地址

```shell
apt install net-tools

ifconfig
```

## 快捷登陆，无密码，靠密钥

powershell 下运行

```shell
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

```shell
ssh-copy-id huaxvcode@127.0.0.1
```

## 登陆

powershell 下运行：

```shell
ssh huaxvcode@127.0.0.1
```

## vscode 下载插件

```
remote - ssh

remote explorer
```

## 连接

![](./img/vscode连ubuntu.png)
![](./img/vscode-config.png)

## 下载编译环境

```shell
sudo su

sudo apt install build-essential manpages-dev software-properties-common gcc g++ make bison binutils gcc-multilib flex

sudo apt install openjdk-17-jre-headless
```

## 测试编译环境

```shell
gcc -v
g++ -v
python3
java -version
```
