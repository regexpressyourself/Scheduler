#!/bin/bash
pyinstaller -F scheduler.py
rm scheduler.exe
cp dist/scheduler scheduler.exe
git add scheduler.py
git add README.md
git add schedule.xls
git add scheduler.exe
git commit
git push

