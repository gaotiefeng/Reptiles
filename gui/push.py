#!/usr/bin/python3
# -*- encoding:utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    version="1.0",
    description="文件处理工具",
    name="文件处理工具",
    zipfile=None,
    windows=['start.py'],
    #console=["start.py"]
)
