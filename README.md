# Scheduler.py
=========

An employee scheduling script. 

This is meant largely as an excercise for myself. Take this app with a grain of salt. 


## Inpiration
=============

After 7 years of retail and countless excuses from management about the
difficulty of creating a schedule, I decided to try to ease the process.

## What Scheduler.py Is
=====================

Scheduler.py is designed to give a comprehensive starting point for a schedule. It
randomly assigns shifts to employees based on their available days and hours
and.py neatly exports the data to an excel file for further manipulation. 

Currently, Scheduler.py is simply a python script and can be run from the command
line. I plan on porting to a web app for use in the future.

## What Scheduler.py Is Not
=========================

Scheduler.py is not meant to be interactive scheduling software. Its purpose is 
simply to give you a starting point to build on. It will randomly assign shifts 
to employees while adhering to days off, hours per week, and some other nuanced
shift constraints. While the process is not interactive, a  well-formatted 
excel schedule is produced which you are free to manipulate to your will.

## How to use
=============

Short version: run the executable and follow the prompts.

Long version: To run the app from the source, you must have 
[python 2.7.*](www.python.org/downloads) and the [xlwt](pypi.python.org/pypi/xlwt) 
library. I have also packaged the app up into a .exe using [pyinstaller](www.pyinstaller.org),
which you can simply download and run, if that's easier. Scheduler.py will output 
your .xls schedule in the same directory as the program itself. Look for "schedule.xls".

Once you have the app running, the process is relatively intuitive. You are first
walked through the week and asked for how many shifts in a given day, along with
the shift times. The times can take most any format, and will let you know if
they are unreadable. I recommend 9a, or 9:30a for 9:00 AM and 9:30 AM, respectively.

After times are taken down, the app asks for the names, total hours, shifts off, 
and days off for each employee. 

The app will log any unassigned shift at the bottom of the schedule, under 
"unassigned." You are free to adjust these shifts according to your need. It's 
your schedule now!


