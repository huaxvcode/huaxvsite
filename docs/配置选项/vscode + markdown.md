# [vscode + markdown]()

1. 下载 `markdown pdf`
2. 下载 `markdown all in one`
3. 下载 `markdown preview github styling`

```
C:\Users\13255\.vscode-insiders\extensions\yzane.markdown-pdf-1.5.0\template

在末尾处添加两行：

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>
```

例如：

```html
<!DOCTYPE html>
<html>
<head>
<title>{{{title}}}</title>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">
{{{style}}}
{{{mermaid}}}
</head>
<body>
  <script>
    mermaid.initialize({
      startOnLoad: true,
      theme: document.body.classList.contains('vscode-dark') || document.body.classList.contains('vscode-high-contrast')
          ? 'dark'
          : 'default'
    });
  </script>
{{{content}}}
</body>
</html>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>
```