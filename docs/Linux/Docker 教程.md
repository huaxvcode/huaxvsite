# Docker 教程

## 安装 docker

```bash
sudo su

apt-get remove docker docker-engine docker.io containerd runc

sudo apt update && sudo apt upgrade

apt-get install ca-certificates curl gnupg lsb-release

curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"

apt-get install docker-ce docker-ce-cli containerd.io

sudo usermod -aG docker $USER

systemctl start docker

apt-get -y install apt-transport-https ca-certificates curl software-properties-common

service docker restart

sudo docker run hello-world
```
 