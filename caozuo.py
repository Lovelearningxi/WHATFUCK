#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 09:06
# @Author  : WangXi
# @File    : caozuo.py
# @Software: PyCharm

from time import sleep

from pynput.keyboard import Key, Controller  # 键盘操作
from pyperclip import copy  # 剪切板操作

from marenyongde import Fuck


class Loop:
    def __init__(self, flag, time, queue, type=None, dirs=None):
        self.flag = flag
        self.dirs = dirs
        self.time = time
        self.queue = queue
        self.fuck = Fuck(type)
        self.k = Controller()

    def run(self):
        while True:
            if self.queue.empty() == False:
                return
            if self.flag == '网站':
                try:
                    str = self.fuck.run()
                except Exception:
                    return
                self.out(str)
                sleep(self.time)
            elif self.flag == '字典':
                for one in self.dirs:
                    if self.queue.empty() == False:
                        return
                    self.out(one)
                    sleep(self.time)

    def out(self, str):
        copy(str)
        self.ctrl_v_enter()

    def ctrl_v_enter(self):
        with self.k.pressed(Key.ctrl):
            self.k.press('v')
            self.k.release('v')
        self.k.press(Key.enter)
        self.k.release(Key.enter)