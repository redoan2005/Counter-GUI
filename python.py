import sys
from PySide6 import QtWidgets as qtw

def increaser():
  global counter
  counter=counter+1
  resultlabel.setText(f"btn clicked: {str(counter)} times")
  resultlabel.adjustSize()

def decreaser():
  global counter
  counter=counter-1
  resultlabel.setText(f"btn clicked: {str(counter)} times")
  resultlabel.adjustSize()

counter=0
app=qtw.QApplication(sys.argv)
window=qtw.QWidget()
window.resize(500,500)
window.setWindowTitle("Counter GUI")

label1=qtw.QLabel("Counter:",window)
label1.move(50,40)

resultlabel=qtw.QLabel(f"btn clicked: {str(counter)} times",window)
resultlabel.move(90,200)

btn1=qtw.QPushButton("+",window)
btn1.move(50,100)
btn1.clicked.connect(increaser)

btn2=qtw.QPushButton("-",window)
btn2.move(200,100)
btn2.clicked.connect(decreaser)

window.show()
sys.exit(app.exec())
