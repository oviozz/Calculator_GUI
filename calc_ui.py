from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from decimal import Decimal



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(528, 697)
        Form.setStyleSheet("background-color:rgb(50, 112, 60)        ;")
        self.calculaltion_display = QtWidgets.QLabel(Form)
        self.calculaltion_display.setGeometry(QtCore.QRect(10, 10, 501, 191))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.calculaltion_display.setFont(font)
        self.calculaltion_display.setStyleSheet("")
        self.calculaltion_display.setFrameShape(QtWidgets.QFrame.Box)
        self.calculaltion_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calculaltion_display.setLineWidth(6)
        self.calculaltion_display.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.calculaltion_display.setIndent(-1)
        self.calculaltion_display.setObjectName("calculaltion_display")
        self.clear_full = QtWidgets.QPushButton(Form)
        self.clear_full.setGeometry(QtCore.QRect(30, 260, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.clear_full.setFont(font)
        self.clear_full.setAcceptDrops(False)
        self.clear_full.setStyleSheet("background-color: rgb(71, 98, 40);")
        self.clear_full.setAutoDefault(False)
        self.clear_full.setDefault(False)
        self.clear_full.setFlat(False)
        self.clear_full.setObjectName("clear_full")
        self.seven = QtWidgets.QPushButton(Form)
        self.seven.setGeometry(QtCore.QRect(30, 340, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.seven.setFont(font)
        self.seven.setMouseTracking(False)
        self.seven.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.seven.setAutoFillBackground(False)
        self.seven.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.seven.setFlat(False)
        self.seven.setObjectName("seven")
        self.module = QtWidgets.QPushButton(Form)
        self.module.setGeometry(QtCore.QRect(150, 260, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.module.setFont(font)
        self.module.setFlat(True)
        self.module.setObjectName("module")
        self.divide = QtWidgets.QPushButton(Form)
        self.divide.setGeometry(QtCore.QRect(270, 260, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.divide.setFont(font)
        self.divide.setFlat(True)
        self.divide.setObjectName("divide")
        self.clear_index = QtWidgets.QPushButton(Form)
        self.clear_index.setEnabled(True)
        self.clear_index.setGeometry(QtCore.QRect(400, 260, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.clear_index.setFont(font)
        self.clear_index.setStyleSheet("background-color: rgb(71, 98, 40);")
        self.clear_index.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_index.setIcon(icon)
        self.clear_index.setIconSize(QtCore.QSize(80, 60))
        self.clear_index.setAutoDefault(False)
        self.clear_index.setFlat(False)
        self.clear_index.setObjectName("clear_index")
        self.four = QtWidgets.QPushButton(Form)
        self.four.setGeometry(QtCore.QRect(30, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.four.setFont(font)
        self.four.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.four.setFlat(False)
        self.four.setObjectName("four")
        self.one = QtWidgets.QPushButton(Form)
        self.one.setGeometry(QtCore.QRect(30, 500, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.one.setFont(font)
        self.one.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.one.setFlat(False)
        self.one.setObjectName("one")
        self.zero = QtWidgets.QPushButton(Form)
        self.zero.setGeometry(QtCore.QRect(30, 580, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.zero.setFont(font)
        self.zero.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.zero.setFlat(False)
        self.zero.setObjectName("zero")
        self.eight = QtWidgets.QPushButton(Form)
        self.eight.setGeometry(QtCore.QRect(150, 340, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.eight.setFont(font)
        self.eight.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.eight.setFlat(False)
        self.eight.setObjectName("eight")
        self.two = QtWidgets.QPushButton(Form)
        self.two.setGeometry(QtCore.QRect(150, 500, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.two.setFont(font)
        self.two.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.two.setFlat(False)
        self.two.setObjectName("two")
        self.five = QtWidgets.QPushButton(Form)
        self.five.setGeometry(QtCore.QRect(150, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.five.setFont(font)
        self.five.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.five.setFlat(False)
        self.five.setObjectName("five")
        self.dot = QtWidgets.QPushButton(Form)
        self.dot.setGeometry(QtCore.QRect(150, 580, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.dot.setFont(font)
        self.dot.setFlat(True)
        self.dot.setObjectName("dot")
        self.nine = QtWidgets.QPushButton(Form)
        self.nine.setGeometry(QtCore.QRect(270, 340, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.nine.setFont(font)
        self.nine.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.nine.setFlat(False)
        self.nine.setObjectName("nine")
        self.three = QtWidgets.QPushButton(Form)
        self.three.setGeometry(QtCore.QRect(270, 500, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.three.setFont(font)
        self.three.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.three.setFlat(False)
        self.three.setObjectName("three")
        self.six = QtWidgets.QPushButton(Form)
        self.six.setGeometry(QtCore.QRect(270, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.six.setFont(font)
        self.six.setStyleSheet("background-color: rgb(123, 170, 70);")
        self.six.setFlat(False)
        self.six.setObjectName("six")
        self.times = QtWidgets.QPushButton(Form)
        self.times.setGeometry(QtCore.QRect(400, 340, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.times.setFont(font)
        self.times.setFlat(True)
        self.times.setObjectName("times")
        self.plus = QtWidgets.QPushButton(Form)
        self.plus.setGeometry(QtCore.QRect(400, 500, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.plus.setFont(font)
        self.plus.setFlat(True)
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(Form)
        self.minus.setGeometry(QtCore.QRect(400, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.minus.setFont(font)
        self.minus.setFlat(True)
        self.minus.setObjectName("minus")
        self.equals = QtWidgets.QPushButton(Form)
        self.equals.setGeometry(QtCore.QRect(260, 580, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.equals.setFont(font)
        self.equals.setStyleSheet("\n"
"background-color: rgb(101, 139, 57);")
        self.equals.setFlat(False)
        self.equals.setObjectName("equals")
        self.calculation_steps = QtWidgets.QLabel(Form)
        self.calculation_steps.setGeometry(QtCore.QRect(30, 130, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.calculation_steps.setFont(font)
        self.calculation_steps.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.calculation_steps.setObjectName("calculation_steps")
        self.calculaltion_display.raise_()
        self.calculation_steps.raise_()
        self.clear_full.raise_()
        self.seven.raise_()
        self.module.raise_()
        self.divide.raise_()
        self.clear_index.raise_()
        self.four.raise_()
        self.one.raise_()
        self.zero.raise_()
        self.eight.raise_()
        self.two.raise_()
        self.five.raise_()
        self.dot.raise_()
        self.nine.raise_()
        self.three.raise_()
        self.six.raise_()
        self.times.raise_()
        self.plus.raise_()
        self.minus.raise_()
        self.equals.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.calculaltion_display.setText(_translate("Form", "300"))
        self.clear_full.setText(_translate("Form", "C"))
        self.seven.setText(_translate("Form", "7"))
        self.module.setText(_translate("Form", "%"))
        self.divide.setText(_translate("Form", "/"))
        self.four.setText(_translate("Form", "4"))
        self.one.setText(_translate("Form", "1"))
        self.zero.setText(_translate("Form", "0"))
        self.eight.setText(_translate("Form", "8"))
        self.two.setText(_translate("Form", "2"))
        self.five.setText(_translate("Form", "5"))
        self.dot.setText(_translate("Form", "."))
        self.nine.setText(_translate("Form", "9"))
        self.three.setText(_translate("Form", "3"))
        self.six.setText(_translate("Form", "6"))
        self.times.setText(_translate("Form", "×"))
        self.plus.setText(_translate("Form", "+"))
        self.minus.setText(_translate("Form", "-"))
        self.equals.setText(_translate("Form", "="))
        self.calculation_steps.setText(_translate("Form", "100+200"))

        # numbers pressed
        self.zero.clicked.connect(partial(self.number_pressed, 0))
        self.one.clicked.connect(partial(self.number_pressed,1))
        self.two.clicked.connect(partial(self.number_pressed, 2))
        self.three.clicked.connect(partial(self.number_pressed, 3))
        self.four.clicked.connect(partial(self.number_pressed, 4))
        self.five.clicked.connect(partial(self.number_pressed, 5))
        self.six.clicked.connect(partial(self.number_pressed, 6))
        self.seven.clicked.connect(partial(self.number_pressed, 7))
        self.eight.clicked.connect(partial(self.number_pressed, 8))
        self.nine.clicked.connect(partial(self.number_pressed, 9))
        self.dot.clicked.connect(partial(self.number_pressed, '.'))


        # operator_pressed
        self.plus.clicked.connect(partial(self.number_pressed, '+'))
        self.minus.clicked.connect(partial(self.number_pressed, '-'))
        self.times.clicked.connect(partial(self.number_pressed, '*'))
        self.divide.clicked.connect(partial(self.number_pressed, '/'))
        self.module.clicked.connect(partial(self.number_pressed, '%'))


        # clear_pressed
        self.clear_full.clicked.connect(partial(self.number_pressed,'back'))

        # back_delete
        self.clear_index.clicked.connect(partial(self.number_pressed,'index_clear'))

        # calcuation_equals

        self.equals.clicked.connect(self.calculation)



        self.calc_steps = ''
        self.check = True
    def number_pressed(self, number_sign):

        if number_sign == 'index_clear':
            self.calc_steps = self.calc_steps[:-1]
            self.calculation_steps.setText(self.calc_steps)

        elif number_sign == 'back':
            self.calc_steps = ''
            self.calculation_steps.setText(self.calc_steps)

        else:
            self.calc_steps += str(number_sign)
            self.calculation_steps.setText(self.calc_steps)



    def calculation(self):
        try:
            for j in range(len(self.calc_steps)):
                if (self.calc_steps[j] in '+-*/%.' and self.calc_steps[j + 1] in '+-*/%.') and (self.calc_steps[j],self.calc_steps[j + 1],self.calc_steps[j + 2] in '+-*/%'):
                    self.check = False

                if (self.calc_steps[0] in '+*/%') or (self.calc_steps[-1] in '+*/%' ):
                    raise ValueError

            if self.check:
                self.calculaltion_display.setText(str(round(eval(self.calc_steps), 5)))

            else:
                self.calculaltion_display.setText('Error')
                self.calc_steps = ''
                self.check = True

        except ValueError:
            self.calculaltion_display.setText('Error')
            self.calc_steps = ''
            self.check = True










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
