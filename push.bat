@echo off

@REM mkdocs -q build && git add . && git commit -m "%*" && git push -u origin master -f

mkdocs -q build && git add . && git commit -m "%*" && git push
