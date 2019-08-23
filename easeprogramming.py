from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from subprocess import *
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
	QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setStyleSheet("""QPushButton[Test=true] {
                border: 2px solid #8f8f91;
                border-radius: 99px;}""")
		self.Demo()
	def Demo(self):
		self.text=QPlainTextEdit(self)
		self.text.move(70,20)
		self.text.resize(500,400)
		self.text1=QPlainTextEdit(self)
		self.text1.move(690,20)
		self.text1.resize(500,400)
		choose=QPushButton("Open File",self)
		choose.move(120,450)
		choose.clicked.connect(self.choosefile)
		execute=QPushButton("Execute",self)
		execute.move(750,450)
		execute.clicked.connect(self.executefile)
		save=QPushButton("save changes",self)
		save.move(400,450)
		save.clicked.connect(self.savechange)
		self.cb=QComboBox(self)
		self.cb.addItem("please choose")
		self.cb.addItem("C")
		self.cb.addItem("C++")
		self.cb.addItems(["Java", "C#", "Python"])
		self.cb.currentIndexChanged.connect(self.selectionchange)
		self.cb.move(270,450)
		self.name=('','')
		self.lang=''
		self.progress = QProgressBar(self)
		self.progress.resize(200,25)
		self.progress.move(880,452)
		self.show()
	def savechange(self):
		mytext = self.text.toPlainText()
		if self.name[0]!='':
			a=open(self.name[0],'w')
			a.write(mytext)
			a.close()
		else:
			QMessageBox.question(self, 'Error', "No file is selected", QMessageBox.Ok)
				
	def selectionchange(self):
		self.lang=self.cb.currentText()
		
	def choosefile(self):
		self.name=QFileDialog.getOpenFileName(self,"Files")
		if self.name[0]!='':
			data=open(str(self.name[0]),'r').read()
			self.text.setPlainText(data)
	def executefile(self):
		self.download()
		if self.lang=='' or self.name[0]=='' or self.lang=="please choose":
			QMessageBox.question(self, 'Error', "no language is selected", QMessageBox.Ok)
		else:
			self.files=open('output.txt','r+')
			if self.lang=='C':
				if call(["gcc",self.name[0] ]) == 0:
					call(["./a.out>output.txt"], shell=True)
					w=self.files.read()
					self.text1.setPlainText(w)
					self.files.seek(0)
					self.files.truncate(0)
				else: 
					self.text1.setPlainText("compilation error")
			elif self.lang=="Python":
				Popen("python3 "+self.name[0],stdout=self.files,shell=True)
				w=self.files.read()
				self.text1.setPlainText(w)
				self.files.seek(0)
				self.files.truncate(0)
			self.files.close()
		self.progress.setValue(0)
	def download(self):
		self.completed = 0
		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)
	
if __name__=='__main__':
	app=QApplication(sys.argv)
	a=Example()
	sys.exit(app.exec_())
