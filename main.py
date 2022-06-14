from dataclasses import replace
import pickle
import re
import sys
import spacy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from sklearn.feature_extraction.text import *
from sklearn.linear_model import *
from gui import Ui_MainWindow
import csv


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_1.clicked.connect(self.upgrd)
        self.ui.pushButton_2.clicked.connect(self.workfoler)
        self.ui.label_4.setText(fold[0])

        con=mywindow.continue_()

        if con[1] == ' 1':
            self.ui.label_2.setText("Подозрительный")
            self.ui.label_2.setStyleSheet("background-color: #FF0000;")
        if con[1] == ' 0':
            self.ui.label_2.setText("Чисто")
            self.ui.label_2.setStyleSheet("background-color: #00FF00;")

        self.ui.label.setText(con[0])

        self.ui.textBrowser.setHtml(str(con[3]))

    def continue_():
        rez = []
        with open('param.csv','r',newline='',encoding="utf-8") as param:
            p = csv.reader(param)
            for row in p:
                if row[0]=='save_param':
                    sf[1]=row[1]
                    sf[2]=row[2]
                    sf[3]=row[3]
                    if row[1] == ' -':
                        for i in range(3):
                            rez.append("")
                        break
                    else:
                        for i in range(3):
                            rez.append(row[i+1])
                        break
            if rez[0] == '':
                rez.append('')
            else:
                fs = open('save_text.txt', 'r', encoding="utf-8")
                rez.append(fs.read())
                fs.close()
        return rez

    def btnClicked(self):
        filename , check = QFileDialog.getOpenFileName(
            None, 
            "QFileDialog.getOpenFileName()",
            "", 
            "Text Files (*.txt)"
        )
        if check:
            sf[1] = ' '+filename
            text = textwork.fileread(filename)
            self.ui.label.setText(filename)
            pred, doc = textwork.textcreate(text)
            if pred == 1:
                self.ui.label_2.setText("Подозрительный")
                self.ui.label_2.setStyleSheet("background-color: #FF0000;")
                sf[2]=' '+str(1)
            if pred == 0:
                sf[2]=' '+str(0)
                self.ui.label_2.setText("Чисто")
                self.ui.label_2.setStyleSheet("background-color: #00FF00;")

            self.ui.textBrowser.setHtml(doc)
        else:
            self.ui.label.setText("")
            self.ui.label_2.setText("")
            self.ui.textBrowser.setText("")
            self.ui.label_2.setStyleSheet("background-color: white;")

    def upgrd(self):
        QMessageBox.about(self,"Предупреждение", "Замена файлой моделей самостоятельно не рекомендуется.\n Это может привести к ошибкам работы программы.")
        filename1 , check1 = QFileDialog.getOpenFileName(
            None, 
            "QFileDialog.getOpenFileName()",
            "", 
            "Text Files (*)"
        )
        if check1:
            with open(filename1, 'rb') as tm1:
                f1 = pickle.load(tm1)
            with open('text_classifier_ru_1', 'wb') as picklefile:
                pickle.dump(f1,picklefile)
            filename11 , check11 = QFileDialog.getOpenFileName(
                None, 
                "QFileDialog.getOpenFileName()",
                "", 
                "Text Files (*)"
            )
            if check11:
                with open(filename11, 'rb') as tm11:
                    f11 = pickle.load(tm11)
                with open('text_vectorizer_ru_1', 'wb') as picklefile:
                    pickle.dump(f11,picklefile)

    def workfoler(self):
        filename2 = QFileDialog.getExistingDirectory(
            None, 
            "Выберите рабочую папку",
            ""
        )
        if filename2:
            with open('param.sav', 'wb') as picklefile:
                pickle.dump([filename2],picklefile)
            fold=filename2
            self.ui.label_4.setText(fold)

    def closeEvent(self, event):
        with open('param.csv', 'w', newline='', encoding='utf-8') as sp:
            wr = csv.writer(sp)
            wr.writerow([sf[0], sf[1], sf[2], sf[3]])
        event.accept()

class textwork():
    #загрузка файла
    def fileread(filename1):
        with open(filename1, "r", encoding="utf-8") as filetext1:
            text1=filetext1.read()
        return text1

    # вызов предобработки, анализа и составление результата вывода
    def textcreate(text2):
        split_text21 = '' + text2
        split_text2 = list(filter(None, re.split('([^!|^?|^.]+[\!|\?|\.])', text2)))
        split_text22 = split_text2.copy()
        zamena_new=[]

        target2 = 0
        count_=0
        document2 = ""
        zamena_old = []
        pred2 = textwork.classification(split_text2)
        for i02 in range(len(pred2)):
            if pred2[i02] == 1:
                document2 = "<a style=\'background-color:#FF0000;\'>" + split_text22[i02] + "</a>"
                count_+=1
                zamena_new.append(document2)
                zamena_old.append(split_text22[i02])
                if target2 == 0:
                    target2 = 1
        for i021 in range(len(zamena_old)):
            split_text21 = split_text21.replace(zamena_old[i021], zamena_new[i021])
        split_text21="<pre style=\'white-space: pre-wrap;\'>"+split_text21+"</pre>"

        rename=sf[1].replace(".","_")
        rename=rename.replace(":","_")
        rename=rename.replace("/","_")
        rename=rename.replace(" ","_")
        otchet=open(
            fold[0] + "/"+rename + ".html",
            "w",
            encoding="utf-8"
        )
        otchet.write(
            "<pre style=\'white-space: pre-wrap;\'>Имя файла: " + sf[1] + "</pre>Обнаружено деструктивных элементов: " + str(count_) + "</pre><pre style=\'white-space: pre-wrap;\'>Текст документа</pre>" + split_text21
        )
        otchet.close()

        f = open('save_text.txt', 'w', encoding='utf-8')
        f.write(split_text21)
        f.close()

        rez2=[target2, split_text21]
        return rez2

    # предварительная обработка текста
    def textprework(text3):
        sp3=spacy.load("ru_core_news_sm")
        for i03 in range(len(text3)):
            text3[i03] = text3[i03].replace('\n', ' ')
            text3[i03] = text3[i03].lower()
            document3 = sp3(text3[i03])
            document3 = [token3.lemma_ for token3 in document3]
            document3 = ' '.join(document3)
            document3 = re.sub(r'\W', ' ', document3)
            document3 = re.sub(r'\s+', ' ', document3)
            text3[i03] = document3
        return text3

    def vector(text4):
        with open('text_vectorizer_ru_1', 'rb') as tm4:
            vector4 = pickle.load(tm4)
        tokens4=vector4.transform(text4)
        return tokens4

    # проверка на деструктивный контент
    def classification(text4):
        text4 = textwork.textprework(text4)
        tokens4 = textwork.vector(text4)
        with open('text_classifier_ru_1', 'rb') as tm4:
            clf4 = pickle.load(tm4)
        pred4 = clf4.predict(tokens4)
        return pred4

sf=['save_param', '-', '-', '0']

with open('param.sav', 'rb') as paramfile:
    #рабочая папка
    fold = pickle.load(paramfile)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
