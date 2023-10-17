# ssh 连接

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
ssh-copy-id -p 16610 huaxvubuntu@192.168.42.131
```
