# [jQuery 鼠标「双击」元素时触发]()

```html
<script>
    $(selector).dblclick(
        
    );
</script>
```

给选中的元素绑定鼠标双击事件.

如果单击和双击同时绑定，那么会非常难触发双击事件！

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
    <p> hello world </p>
    <script>
        // 禁止文字被选中
        document.onselectstart = function(){ return false; };
        
        var dblcl = 0, cl = 0;
        $(function(){
            $("p").css({"color": "black", "font-size":"18px"});
            $("p").dblclick(function(){
                dblcl ++;
                if (dblcl & 1) $("p").css({"color":"red"});
                else $("p").css({"color":"black"});
            });
            // $("p").click(function(){ 
            //     cl ++;
            //     if (cl & 1) $("p").css({"color":"green", "font-size":"30px"}); 
            //     else $("p").css({"color": "black", "font-size":"18px"});
            // });
        });
    </script>
<!-- =========================================== -->
</body>
</html>
```