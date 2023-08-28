# [jQuery 鼠标点击元素时触发]()

```html
<script>
    $(selector).click(
        
    );
</script>
```

当鼠标点击选中的元素时，会运行 `click` 里面的内容；

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
    <p> hello world </p>
    <script>
        var cl = 0;
        $(function(){
            $("p").click(function(){
                cl ++;
                if (cl & 1) $("p").css({"color":"red"});
                else $("p").css({"color":"black"});
            });
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```