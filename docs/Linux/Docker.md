# Docker

## 安装 docker

非常不建议使用子系统 wsl 版本的 ubuntu 安装 docker，目前为止我还没有安装成功！

vmware 安装好 ubuntu20.04 后分别调用下面命令（记得先提前换源）

```bash
sudo apt update


sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -


sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"


sudo apt update


sudo apt install docker-ce docker-ce-cli containerd.io


sudo systemctl status docker


sudo systemctl start docker
```

## 查看 docker 版本号

```bash
docker --version
```

## 给 docker 添加权限

```bash
sudo usermod -aG docker $USER
sudo usermod -aG docker huaxvcode
```

## 拉取一个镜像

```bash
sudo docker pull ubuntu:22.04
```

## 列出当前所有镜像

```bash
sudo docker images
```

## 删除某镜像

```bash
docker rmi ubuntu:20.04
```

## 利用镜像创建一个容器

```bash
docker create -it ubuntu:20.04

# 将容器的 22 端口映射为宿主机的 16610 端口
# 方便后续的 ssh 连接
docker run -p 16610:22 --name huaxvubuntu -itd ubuntu:22.04
```

## 查看本地所有容器

```bash
docker ps -a
```

## 启动容器

```bash
docker start 容器id或名字
```

## 停止容器

```bash
docker stop 容器id或名字
```

## 重启容器

```bash
docker restart 容器id或名字
```

## 进入容器

```bash
docker attach 容器id或名字
```

```bash
ctrl + p, ctrl + q 挂起容器

ctrl + d 结束容器
```

## 在容器中执行命令

```bash
docker exec 容器id或名字  命令
```

## 删除容器

```bash
docker rm 容器id或名字
```

## 重命名容器

```bash
docker rename 容器名字 新名字
```

## 以某容器为板子创建镜像

```bash
docker commit 容器id或名字 镜像名:信息
```

## 将镜像导出成文件

```bash
docker save -o 文件名.tar 镜像名:信息
```

## 加载某镜像文件

```bash
docker load -i 文件名.tar
```


## 配置自动重启容器

```
docker run -d --restart=always --name 设置容器名 使用的镜像
（上面命令  --name后面两个参数根据实际情况自行修改）
 
# Docker 容器的重启策略如下：
 --restart具体参数值详细信息：
       no　　　　　　　 // 默认策略,容器退出时不重启容器；
       on-failure　　  // 在容器非正常退出时（退出状态非0）才重新启动容器；
       on-failure:3    // 在容器非正常退出时重启容器，最多重启3次；
       always　　　　  // 无论退出状态是如何，都重启容器；
       unless-stopped  // 在容器退出时总是重启容器，但是不考虑在 Docker 守护进程启动时就已经停止了的容器。
       
docker update --restart=always 容器ID(或者容器名)
（容器ID或者容器名根据实际情况修改）
```
