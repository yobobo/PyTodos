# -*- coding: utf-8 -*-
import time

from PyTodos.file_handler import read_file, write_file

TEST_FILE = './test_data.txt'


def test_file_handler():
    now = int(time.time())
    write_todos = [
        {
            'id': 1,
            'task_detail': '1st_todo_detail',
            'timestamp': now
        },
        {
            'id': 2,
            'task_detail': '2nd_todo_detail',
            'timestamp': now
        }
    ]
    write_file(write_todos, TEST_FILE)
    read_todos = read_file(TEST_FILE)
    assert read_todos == write_todos
