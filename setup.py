# -*- coding: utf-8 -*-

from setuptools import setup

entry_points = [
    # todo
    "todos = PyTodos.todo:todos"
]

setup(
    name="pytodos",
    version='1.0.1',
    description="",
    long_description="",
    author="chuanwu",
    author_email="chuanwusun@gmail.com",
    packages=['pytodos'],
    url="https://github.com/chuanwu/PyToDos.py",
    entry_points={"console_scripts": entry_points},
    install_requires=[],

)
