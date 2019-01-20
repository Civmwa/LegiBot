import requests
from cx_Freeze import setup, Executable
import sys, os
from idna import idnadata
from multiprocessing import Queue
import os
import csv

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

sys.argv.append("build")
filename="LegiBot.py"
icon= "scrapercon.ico"

base = None

options={
        "build_exe": {
            "packages": ["idna"],
            },
        },

if sys.platform=="win64":
    base="Win64GUI"

exe = Executable(script='LegiBot.py', base = base, icon='scrapercon.ico')
includefiles = ['blacks_Law_Dict.csv']
additional_mods = ['numpy.core._methods', 'numpy.lib.format']
additional_packages = ['asyncio', 'asyncio.compat', 'appdirs', 'csv', 'pkg_resources._vendor', 'tkinter']

setup(
    name = "Desktop Professional Support Lawyer",
    version = "1.0.1",
    description = 'Desktop Professional Support Lawyer.',
    author = 'Wakili.AI',
    author_email = 'hello@nomeon.technology',
    options = {
        'build_exe': {
            'includes': additional_mods,
            'packages': additional_packages,
            'include_files':includefiles,
            'include_files':[
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                ],
            
        }},
    executables=[exe])


