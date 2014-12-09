# Scheduler
=========

An employee scheduling script. 

After 7 years of retail and countless excuses from management about the
difficulty of creating a schedule, I decided to try to ease the process.

Scheduler is designed to give a comprehensive starting point for a schedule. It
randomly assigns shifts to employees based on their available days and hours
and exports the data to an excel file for further manipulation. 

Currently, Scheduler is simply a python script and can be run from the command
line. I hope to make either a GUI excecutable or web app for use in the future.

## How to use
=============

Since Scheduler is a python script, you can run it from the command line,
assuming you have python installed. However, you will also need to install the xlwt module to write to an excel file.

**Requirements**

- python
- xlwt module for python

If you do not have python, you can get it here (scheduler uses python 2.7):
https://www.python.org/downloads/
The xlwt module can be found here: https://pypi.python.org/pypi/xlwt

**Setting up xlwt**

- download and extract the directory
- from the command line, cd into the directory and enter the command: 
"python setup.py install"

Once you have all of the requirements insalled, simply run the scheduler.py
file, follow the prompts, and the script will generate a "scheduler.xls" file
containing your schedule! 

## Some Notes
=============

Scheduler is meant to create a starting point for your schedule, not
necessarily a final product. Following this philosophy, scheduler will create
an entry for "unassigned" and allocate any shifts it cannot assign there. After
the schedule is created, you are encouraged to adjust it to your needs. 
