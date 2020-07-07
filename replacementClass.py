# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:17:52 2020

@author: CVPR
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from queue           import PriorityQueue
from itertools       import count

import sys
import copy
import random



class nodeTree:
    def __init__(self, current_state, zero_index, parentNode):
        self.current_state = current_state
        self.zero_index    = zero_index
        self.parentNode    = parentNode
    
    
    
class PuzzleGUI(QMainWindow):
    def __init__(self, parent = None):
        super(PuzzleGUI, self).__init__(parent)
        global puzzleList

        # 초기화
        self.goal_state     = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]        # 퍼즐 pannel
        self.queue          = PriorityQueue()
        self.solutionNumber = count()
        self.answerNode     = None

        # Main
        self.setWindowTitle("류원정짱") 
        self.now_slot = -1

        # Widget 생성
        wid                 = QWidget(self)
        self.restartButton  = QPushButton()
        self.oneBlockButton = QPushButton()
        self.endButton      = QPushButton()
        self.exitButton     = QPushButton()
        self.label00        = QLabel()
        self.label01        = QLabel()
        self.label02        = QLabel()
        self.label10        = QLabel()
        self.label11        = QLabel()
        self.label12        = QLabel()
        self.label20        = QLabel()
        self.label21        = QLabel()
        self.label22        = QLabel()
        self.ListView       = QListView()
        self.ItemView       = QStandardItemModel(self.ListView)
        
        # Widget text 설정
        self.restartButton.setText("재시작")
        self.oneBlockButton.setText("1스텝 이동")
        self.endButton.setText("끝까지 이동")
        self.exitButton.setText("종료")
        self.label00.setPixmap(QPixmap("1.png"))
        self.label01.setPixmap(QPixmap("2.png"))
        self.label02.setPixmap(QPixmap("3.png"))
        self.label10.setPixmap(QPixmap("4.png"))
        self.label11.setPixmap(QPixmap("5.png"))
        self.label12.setPixmap(QPixmap("6.png"))
        self.label20.setPixmap(QPixmap("7.png"))
        self.label21.setPixmap(QPixmap("8.png"))
        
        # Widget 기능 설정
        self.oneBlockButton.setEnabled(False)
        self.endButton.setEnabled(False)
        self.restartButton.clicked.connect(self.reset)
        self.oneBlockButton.clicked.connect(self.nextStep)
        self.endButton.clicked.connect(self.endStep)
        self.exitButton.clicked.connect(self.exitCall)
        
        # Widget 크기 설정
        self.restartButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.oneBlockButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.endButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.exitButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.ListView.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        self.label00.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label00.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label00.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label10.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label11.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label12.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label20.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label21.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label22.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Widget 위치 설정
        self.setCentralWidget(wid)
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.restartButton)
        buttonLayout.addWidget(self.oneBlockButton)
        buttonLayout.addWidget(self.endButton)
        buttonLayout.addWidget(self.exitButton)

        controlLayout = QVBoxLayout()
        controlLayout.addWidget(self.ListView)
        controlLayout.addLayout(buttonLayout)

        puzzleFirstLayout = QHBoxLayout()
        puzzleFirstLayout.addWidget(self.label00)
        puzzleFirstLayout.addWidget(self.label01)
        puzzleFirstLayout.addWidget(self.label02)

        puzzleSecondLayout = QHBoxLayout()
        puzzleSecondLayout.addWidget(self.label10)
        puzzleSecondLayout.addWidget(self.label11)
        puzzleSecondLayout.addWidget(self.label12)

        puzzleThridLayout = QHBoxLayout()
        puzzleThridLayout.addWidget(self.label20)
        puzzleThridLayout.addWidget(self.label21)
        puzzleThridLayout.addWidget(self.label22)

        puzzleLayout = QVBoxLayout()
        puzzleLayout.addLayout(puzzleFirstLayout)
        puzzleLayout.addLayout(puzzleSecondLayout)
        puzzleLayout.addLayout(puzzleThridLayout)

        WholeLayout = QHBoxLayout()        
        WholeLayout.addLayout(puzzleLayout)
        WholeLayout.addLayout(controlLayout)
        
        wid.setLayout(WholeLayout)
            
    
    # 판 생성    
    def reset(self):
        self.oneBlockButton.setEnabled(True)
        self.endButton.setEnabled(True)
        self.current_state = copy.deepcopy(self.goal_state)           # goal_state 변경하진 않음
        self.zero_index    = [2, 2]                                   # 0의 현재 위치
        self.loopCount     = 200
        self.puzzleList    = list()
        self.ItemView.clear()        

        for i in range(self.loopCount):
            prevX = self.zero_index[1]
            prevY = self.zero_index[0]
            x     = self.zero_index[1]
            y     = self.zero_index[0]

            while (1):
                direction = random.randrange(0, 4)
                if direction == 0: 
                    if y < 1: continue
                    else: y -= 1

                elif direction == 1:
                    if x < 1: continue
                    else: x -= 1

                elif direction == 2:
                    if x > 1: continue
                    else: x += 1

                elif direction == 3:
                    if y > 1: continue
                    else: y += 1
                    
                prev_state                       = copy.deepcopy(self.current_state)
                self.current_state[y][x]         = prev_state[prevY][prevX]
                self.current_state[prevY][prevX] = prev_state[y][x]

                if copy.deepcopy(self.goal_state) == copy.deepcopy(self.current_state): self.current_state = copy.deepcopy(prev_state)
                else: 
                    self.zero_index[0] = y
                    self.zero_index[1] = x
                    break

        self.updateBoard()
        self.aSearch()

 
    # 다음 스텝           
    def nextStep(self):
        self.current_state = self.path.pop()
        if self.current_state == self.goal_state:
            self.oneBlockButton.setEnabled(False)
            self.endButton.setEnabled(False)
            self.updateBoard()

        else:
            self.ItemView.appendRow(QStandardItem(str(self.current_state)))  
            self.ListView.setModel(self.ItemView)
            self.updateBoard()


    # 완료           
    def endStep(self):
        while (1):
            self.current_state = self.path.pop()
            if self.current_state == self.goal_state:
                self.oneBlockButton.setEnabled(False)
                self.endButton.setEnabled(False)
                self.updateBoard()
                return

            else:
                self.ItemView.appendRow(QStandardItem(str(self.current_state)))  
                self.ListView.setModel(self.ItemView)


    # 종료           
    def exitCall(self):
        sys.exit(app.exec_())


    # A search
    def aSearch(self):
        node  = self.createNode(self.current_state, self.zero_index, None)
        self.queue.put((self.calcValue(self.getDepth(node), self.current_state), next(self.solutionNumber), node))

        while not self.queue.empty():
            self.answerNode = self.queue.get()
            if self.answerNode[2].current_state == self.goal_state: 
                self.answerNode = self.answerNode[2]
                break

            if self.answerNode[2].parentNode != None: self.makeChildNode(self.answerNode[2], self.answerNode[2].parentNode.zero_index)
            else: self.makeChildNode(self.answerNode[2], None)

        self.path = list()
        while (1):
            if self.answerNode.parentNode == None: break
            self.path.append(copy.deepcopy(self.answerNode.current_state))
            self.answerNode = self.answerNode.parentNode


    # make childNode
    def makeChildNode(self, node, parent_zero_index):
        for direction in range(4):
            x            = node.zero_index[1]
            y            = node.zero_index[0]
            currentState = copy.deepcopy(node.current_state)

            if direction == 0: 
                if y < 1: continue
                else: 
                    y -= 1
                    self.createLeaf(parent_zero_index, x, y, currentState, node)

            elif direction == 1:
                if x < 1: continue
                else:
                    x -= 1
                    self.createLeaf(parent_zero_index, x, y, currentState, node)

            elif direction == 2:
                if x > 1: continue
                else:
                    x += 1
                    self.createLeaf(parent_zero_index, x, y, currentState, node)

            elif direction == 3:
                if y > 1: continue
                else:
                    y += 1
                    self.createLeaf(parent_zero_index, x, y, currentState, node)


    # createLeaf
    def createLeaf(self, parent_zero_index, x, y, currentState, node):
        if parent_zero_index != None:
            if parent_zero_index[0] == y and parent_zero_index[1] == x: return

        currentState[y][x], currentState[node.zero_index[0]][node.zero_index[1]] = currentState[node.zero_index[0]][node.zero_index[1]], currentState[y][x]
        newNode = self.createNode(currentState, [y, x], node)
        self.queue.put((self.calcValue(self.getDepth(newNode), newNode.current_state), next(self.solutionNumber), newNode))


    # createNode
    def createNode(self, current_state, zero_index, parentNode):
        node = nodeTree(current_state, zero_index, parentNode)
        return node
    
    
    # getDepth
    def getDepth(self, node):
        depth = 0
        tempNode = node
        
        while (1):
            if tempNode.parentNode == None: break
            depth += 1
            tempNode = tempNode.parentNode
        
        return depth


    # calc Value
    def calcValue(self, depth, current_state):
        value = 0

        for i in range(3):
            for j in range(3):
                x = (current_state[i][j] - 1) % 3
                y = (current_state[i][j] - 1) // 3
                value += (j - x) + (y - i)

        return (depth + value)


    # board reset
    def updateBoard(self):
        self.label00.setPixmap(QPixmap("%d.png"%self.current_state[0][0]))
        self.label01.setPixmap(QPixmap("%d.png"%self.current_state[0][1]))
        self.label02.setPixmap(QPixmap("%d.png"%self.current_state[0][2]))
        self.label10.setPixmap(QPixmap("%d.png"%self.current_state[1][0]))
        self.label11.setPixmap(QPixmap("%d.png"%self.current_state[1][1]))
        self.label12.setPixmap(QPixmap("%d.png"%self.current_state[1][2]))
        self.label20.setPixmap(QPixmap("%d.png"%self.current_state[2][0]))
        self.label21.setPixmap(QPixmap("%d.png"%self.current_state[2][1]))
        self.label22.setPixmap(QPixmap("%d.png"%self.current_state[2][2]))


# 메인 함수
if __name__  == "__main__":
    # GUI 생성
    app = QApplication(sys.argv)

    pannel = PuzzleGUI()
    pannel.resize(640, 480)
    pannel.show()
    sys.exit(app.exec_())
