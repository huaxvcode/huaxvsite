# [jQuery 鼠标「悬停离开」时触发]()

```html
<script>
    $().hover(
        function(){}, // mouseenter
        function(){}  // mouseleave
    );
</script>
```

鼠标悬停离开正上方时分别触发，联合了 `mouseenter` 和 `mouseleave`

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
        document.onselectstart = function(){return false;}
        $(function(){
            var p = $("p");
            p.css({"color":"black", "font-size":"18px"});
            p.hover(
                function(){ // 鼠标悬停正上方时触发 mouseenter
                    p.css({"color":"red", "font-size":"18px"});
                },
                function(){ // 鼠标离开正上方时触发 mouseleave
                    p.css({"color":"black", "font-size":"18px"});
                }
            );
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```