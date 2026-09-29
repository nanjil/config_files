import sys
import os
import pathlib
import math
import cmath
import numpy as np
import importlib
import inspect
import matplotlib.pyplot as plt
import threading
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import functools
import tkinter as tk
from tkinter import ttk
import copy
import inspect
import shutil
import datetime


path = pathlib.Path ('c:/cygwin/projects/git')
pathw = path/'work'
patha = pathw/'asic'


l5 = list (path.rglob ('gmx.py'))
sys.path.insert (1, str (l5[0].parent))
sys.path.insert (1, str (patha))
sys.path.insert (1, str (pathw))
sys.path.insert (1, str(path/'apps'/'stdf'))
sys.path.insert (1, str(path/'apps'/'dkltopt'))
sys.path.insert (1, str(path/'apps'/'dieisrc'))
sys.path.insert (1, str(path/'work_personal'))
l5 = list (path.rglob ('eye.py'))
sys.path.insert (1, str (l5[0].parent))





paths = pathlib.Path ('c:/cygwin/projects/test/sandbox')

import genutl
import readf
import gmx
import nmx
import pda
import sparamsim
import btree2
import eye
import asicdb
import waferyld
import genxml
import djiaction

