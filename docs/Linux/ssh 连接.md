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
