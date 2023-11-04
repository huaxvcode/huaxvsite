# Docker 教程

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


