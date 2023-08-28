# [jQuery 鼠标「离开正上方」时]()

```html
<script>
    $().mouseleave(
        
    );
</script>
```

鼠标离开选中的元素正上方时触发该事件.

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

        $(function() {
            $("p").css({"color":"black", "font-size":"30px"});
            
            $("p").mouseenter(function(){
                $("p").css({"color": "red"});
            });
            $("p").mouseleave(function(){
                $("p").css({"color": "black"});
            });
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```