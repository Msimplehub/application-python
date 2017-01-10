#coding=utf-8

"""
python 打包 exe脚本

    create by 14:20 2016-07-21 M.simple
"""

from distutils.core import setup
import py2exe

setup(console=['dataCramler.py'])