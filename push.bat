@echo off

mkdocs -q build && git add . && git commit -m "%*" && git push -u origin master -f

@REM 强制推送，丢弃远程