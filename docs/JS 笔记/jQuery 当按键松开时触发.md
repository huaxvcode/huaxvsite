# [jQuery 当按键松开时触发]()

```html
<script>
    $().keyup(
        
    );
</script>
```

按键松开时会触发该事件

---

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></>
</head>
<body>
<!-- =========================================== -->
    <input type="text">
    <p>你按了 <span>0</span> 次按键</p>
    <script>
        $(function(){
            var ip = $("input");
            var sp = $("span");
            var cnt = 0;
            ip.keyup(function(e){
                sp.text(++ cnt);
            });
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```