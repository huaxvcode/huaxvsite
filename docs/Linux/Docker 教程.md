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
