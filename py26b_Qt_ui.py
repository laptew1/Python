from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit
from py17a_app_dal import getAllProducts

# Костыль на случай, если Qt оказался на пути с русскими буквами
#import os
#os.environ['QT_PLUGIN_PATH'] = r"E:\USER_FILES\мифи\группа 7\venv\Lib\site-packages\PyQt5\Qt5\plugins"
#os.environ['QT_PLUGIN_PATH'] = r".\venv\Lib\site-packages\PyQt5\Qt5\plugins"


class AWProducts(QWidget):

    def __init__(self):
        super().__init__() # вызов конструктора класса-предка

        self.setWindowTitle("Products")
        # Задайте размер окну(10:40)
        self.setFixedSize(300, 500)

        # self.txt_user = QLineEdit(self) # self - указание родительского окна
        # self.txt_user.setGeometry(10, 10, 280, 20)

        txt_products = QTextEdit(self)
        txt_products.setGeometry(10, 40, 280, 450)

        products = getAllProducts()
        output = ""
        for p in products:
            output += p["name"] + "\n"
        txt_products.setText(output)

        self.show()

    def btn_click(self):
        # print("Hello, world!")
        message = f"Hello, {self.txt_user.text()}"
        self.setWindowTitle(message)
        # Выведите надпись на кнопку (11:23)
        self.btn.setText(message)


if __name__ == "__main__":
    app = QApplication([])
    window = AWProducts()
    app.exec()