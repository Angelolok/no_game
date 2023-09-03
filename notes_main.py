#Библиотеки😫
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit, QListWidget, QLineEdit
import json

def add_tyagi():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print('Заметка для добавления тега не выбрана!')        

#Приложение
app = QApplication([])
main_win = QWidget() 
main_win.setWindowTitle('Умные заметки(нет)')

#Слои
Main_Layout = QHBoxLayout()
Part1_Layout = QVBoxLayout()
Part2_Layout = QVBoxLayout()
Note_Button_1_Layout = QVBoxLayout()
Note_Button_2_Layout = QVBoxLayout()
Tag_Button_1_Layout = QVBoxLayout()
Tag_Button_2_Layout = QVBoxLayout()
Buttons_1_Layout = QHBoxLayout()
Buttons_2_Layout = QHBoxLayout()
Write_layout = QHBoxLayout()
Note_List_Layout = QHBoxLayout()
Tag_Search_Layout = QHBoxLayout()

#Кнопки
button_Create_Note = QPushButton("Создать заметку")
button_Delite_Note = QPushButton("Удалить заметку")
button_Safe_Note = QPushButton("Сохранить заметку")
button_Add_Tag = QPushButton("Прикрепить к заметке")
button_Delite_Tag = QPushButton("Открепить от заметки")
button_Search_Tag = QPushButton("Искать заметки по тегу")

#Ввод большого текста
Write_Text = QTextEdit()

#Поиск тега
Search_Tag = QLineEdit()
Search_Tag.setPlaceholderText('Введите тег...')

#Списки тегов и заметок
Note_List = QListWidget()
Tag_List = QListWidget()

#Тексты
Note_label = QLabel('Список заметок')
Tag_label = QLabel('Список тегов')

#Прикрепить слои и виджеты к слоям

Write_layout.addWidget(Write_Text, stretch= 3)

Part1_Layout.addStretch(0)
Part1_Layout.addLayout (Write_layout, stretch= 4) #Ввод большого текста к первой половине
Part1_Layout.addStretch(0)

#Part1_Layout.addStretch(0) #Растяжка большого текста
Part2_Layout.addWidget (Note_label, alignment = Qt.AlignVCenter) #надпись Список заметок ко второй половине
Part2_Layout.addWidget (Note_List, alignment = Qt.AlignCenter) #Списки заметок ко второй половине
Note_Button_1_Layout.addWidget (button_Create_Note, stretch = 2) #Кнопка сделать заметку 
Note_Button_2_Layout.addWidget (button_Delite_Note, stretch = 2) #Кнопка удалить заметку
Buttons_1_Layout.addLayout(Note_Button_1_Layout) #прикрепить кнопку сделать заметку к общему слою 
Buttons_1_Layout.addLayout(Note_Button_2_Layout) #прикрепить кнопку удалить заметку к общему слою 
Part2_Layout.addLayout(Buttons_1_Layout) #Общий слой кнопок заметок к слою второй половины
Part2_Layout.addWidget(button_Safe_Note, stretch = 2) 
Part2_Layout.addWidget(Tag_label, alignment = Qt.AlignVCenter) #надпись Список заметок ко второй половине
Part2_Layout.addWidget(Tag_List, alignment = Qt.AlignCenter) #Прикрепить список тегов к слою второй половины
Part2_Layout.addWidget(Search_Tag, alignment = Qt.AlignCenter) #Прикрепить поиск к слою второй половины
Tag_Button_1_Layout.addWidget(button_Add_Tag, stretch = 2) #Кнопка добавить к заметке
Tag_Button_2_Layout.addWidget(button_Delite_Tag, stretch = 2) #Кнопка открепить от заметки
Buttons_2_Layout.addLayout(Tag_Button_1_Layout) #прикрепить кнопку добавить к заметке к общему слою 
Buttons_2_Layout.addLayout(Tag_Button_2_Layout) #прикрепить кнопку открепить от заметки к общему слою
Part2_Layout.addLayout(Buttons_2_Layout) #Общий слой кнопок тегов к слою второй половины
Main_Layout.addLayout (Part1_Layout) #прикрепляем слой первой половины к общему слою
Main_Layout.addLayout (Part2_Layout) #прикрепляем слой второй половины к общему слою
Part2_Layout.addWidget(button_Search_Tag, stretch = 0)



main_win.setLayout(Main_Layout)
main_win.resize(900, 600)
main_win.show()
app.exec_()