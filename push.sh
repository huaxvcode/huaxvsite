#!/bin/bash

mkdocs -q build && git add . && git commit -m "%*" && git push -u origin master -f

# 强制推送，丢弃远程