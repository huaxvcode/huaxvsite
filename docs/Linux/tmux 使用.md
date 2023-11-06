# tmux 使用

## 新建一个 session

```bash
tmux new -s session
```

## 挂起一个 session

```bash
ctrl+b, d
```

## 列出所有的 session

```bash
tmux ls
```

## 使用某 session

```bash
tmux attach -t session
```


## 删除 session

```bash
tmux kill-session -s session
```

## 左右窗口

```bash
ctrl+b, %
```

## 上下窗口

```bash
ctrl+b, "
```

## 关闭某窗口

```bash
ctrl+d
```
