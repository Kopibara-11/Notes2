from PyQt5.QtWidgets import*
from ui import*
import json 

app=QApplication([])
class MainNoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes={
            "Ласкаво просимо":
            {
            "текст":'Ласкаво просимо в найшій програмі!' ,
            "теги" : ["вітання","інструкція"] 
            }
          
        } 
        self.LoadNotes()
        self.ReadFile()
        self.ui.listView.itemSelectionChanged.connect(self.ShowNotes)
    def ReadFile(self):
        with open("notes.json","r") as file:
            self.notes=json.load(file)
            self.ui.listView.addItems(self.notes)
        print("файл прочитано")
    def LoadNotes(self):
        with open('notes.json','w') as file:
            json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
        print("Файл загружено")
    def ShowNotes(self):
        key = self.ui.listView.selectedItems()[0].text()
        self.ui.textEdit.setText(self.notes[key]['текст'])
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.notes[key]['теги'])
        print("Замітка обрана") 


ex=MainNoteWindow()
ex.show()
app.exec_()