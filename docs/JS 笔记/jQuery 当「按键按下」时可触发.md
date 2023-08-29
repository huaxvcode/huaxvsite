# [jQuery 当「按键按下」时可触发]()

```html
<script>
    $().keydown(
        function
    )
</script>
```

还有一种事件也能实现类似的效果，但是有一些特殊键不支持：

```html
<script>
    $().keypress(
        function
    )
</script>
```

---

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
</head>
<body>
<!-- =========================================== -->
    <input type="text">
    <p>你总共按下了 <span id="cnt">0</span> 次键盘</p>
    <p>你按下的按键是：<span id="char"></span></p>
    <script>
        cnt = 0
        $(function(){
            var ip = $("input");
            // ip.keypress(function(e){ // 都可以
            ip.keypress(function(){     // 都可以
                $("#cnt").text(++ cnt);
            });
            ip.keydown(function(e){
                var keynum = window.event ? e.keyCode : e.which;
                var keychar = String.fromCharCode(keynum);
                $("#char").text(keychar);
            })
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```