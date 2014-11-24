import sys
from cx_Freeze import setup, Executable

setup(  name = "scheduler",
        version = "0.1",
        description = "Scheduler",
        executables = [Executable("scheduler.py")] ,
        )
