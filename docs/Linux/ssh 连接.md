# ssh 连接

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
