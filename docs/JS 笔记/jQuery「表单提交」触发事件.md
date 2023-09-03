# [jQuery「表单提交」触发事件]()

```html
<script>
    $().submit(

    );
</script>
```

表单提交时触发该事件

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
    <form action="">
        姓名: <input type="text", name="firstname">
        <input type="submit">
    </form>
    <script>
        $(function(){
            var is = $("form");
            is.submit(
                alert("hello world")
            );
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```