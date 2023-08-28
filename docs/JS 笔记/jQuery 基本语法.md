# [jQuery 基本语法]()

写法一：

```html
<script>
    $(function() {
        // 在这里写 jQuery 语法
    });
</script>
```

---

写法二：

```html
<script>
    $(document).ready(function() {
        // 在这里写 jQuery 语法
    });
</script>
```

---

基本使用形式：

```html
<script>
    $(css 选择器).事件(
        
    );
</script>
```

---

举例：

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
        $(function(){
            $("p").css({"color":"red", "font-size":"30px"});
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```