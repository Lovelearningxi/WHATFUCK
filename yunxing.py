#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 09:08
# @Author  : WangXi
# @File    : yunxing.py
# @Software: PyCharm

import sys

from PyQt5.QtWidgets import QApplication

from cao import MainWindow

app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())
