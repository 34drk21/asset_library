import os
import sys
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *

libraryPath = '/Users/shotakimura/Documents/Python/Houdini/AssetLibrary/'


class LoadNodesWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        hbox = QtWidgets.QVBoxLayout()
        
        nameLabel = QtWidgets.QLabel(self)
        nameLabel.setText('Asset List:')

        data_list = os.listdir(libraryPath)

        self.model = QtCore.QStringListModel()
        self.model.setStringList(data_list)

        self.view = QtWidgets.QListView()
        self.view.setModel(self.model)

         #make button
        button = QtWidgets.QPushButton('OK', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 150)

        self.connect(button, QtCore.SIGNAL('clicked()'), self.clickMethod)

        self.setGeometry(600, 200, 600, 800)
        self.setWindowTitle('Asset List')

        #Layout
        hbox.addWidget(nameLabel)
        hbox.addWidget(self.view)
        hbox.addWidget(button)


        self.setLayout(hbox)
    ### load Nodes
    def loadNodes(self):
        sel = hou.selectedNodes()
        filePath = libraryPath + self.assetName
        p = sel[0].parent()
        p.loadChildrenFromFile(filePath)
        
    def clickMethod(self):
        modelIndexes = self.view.currentIndex()
        index = modelIndexes.row()
        self.assetName = self.model.stringList()[index]

        self.loadNodes()




class SaveNodesWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
    
        QtWidgets.QWidget.__init__(self, parent)

        hbox = QtWidgets.QFormLayout()
        
        nameLabel = QtWidgets.QLabel(self)
        nameLabel.setText('Asset Name:')


        self.line = QtWidgets.QLineEdit(self)

        self.assetName = self.line.text()

        #make button
        button = QtWidgets.QPushButton('OK', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 150)

        self.connect(button, QtCore.SIGNAL('clicked()'), self.clickMethod)        

        self.setGeometry(600, 200, 600, 800)
        self.setWindowTitle('Configure Asset')

        #Layout
        hbox.addRow(nameLabel, self.line)

        self.setLayout(hbox)

    ### Save selected Nodes
    def saveNodes(self):
        sel = hou.selectedNodes()
        parentNode = hou.node('/obj')
        filePath = libraryPath + self.assetName + ".hip"
        p = sel[0].parent()
        p.saveChildrenToFile(sel,"",filePath)
        print "Saved new hip file to: " + filePath
        
    def clickMethod(self):
        self.assetName = self.line.text()
        self.saveNodes()
    
    

class NodesLibrary(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        hbox = QtWidgets.QVBoxLayout()
        
        ###initialize info.
        self.assetName = None
        self.assetInfo = None
        self.imagePath = None
        
        #make button
        button = QtWidgets.QPushButton('save nodes', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)
        
        button2 = QtWidgets.QPushButton('load nodes', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)
        
        self.connect(button, QtCore.SIGNAL('clicked()'), self.saveNodesWindow)
        self.connect(button2, QtCore.SIGNAL('clicked()'), self.loadNodesWindow)

        self.setGeometry(500, 300, 250, 110)
        self.setWindowTitle('Nodes Library')
        hbox.addWidget(button)
        hbox.addWidget(button2)
        self.setLayout(hbox)

    ### show asset config dialog
    def saveNodesWindow(self):
        conf = SaveNodesWindow()
        conf.show()
        sys.exit(app.exec_())
        

    ### Save selected Nodes
    def loadNodesWindow(self):
        conf = LoadNodesWindow()
        conf.show()
        sys.exit(app.exec_())
        
nl = NodesLibrary()
nl.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
nl.show()