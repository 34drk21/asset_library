import sys
from PySide2 import QtWidgets, QtCore

tabwidget = QtWidgets.QTabWidget()
widget = QtWidgets.QTabWidget()
layout = QtWidgets.QGridLayout(widget)
tabwidget.addTab(widget, "Tab 1")
tabwidget.show()
sys.exit(app.exec_())