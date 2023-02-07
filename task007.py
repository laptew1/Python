from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit
from py17a_app_dal import getAllProducts



class AWProducts(QWidget):

    def __init__(self):
        super().__init__() # вызов конструктора класса-предка

        self.setWindowTitle("Products")
        self.setFixedSize(300, 500)

        self.setWindowTitle("Products")
        self.setFixedSize(300, 500)

        self.txt_user = QLineEdit(self)  # self - указание родительского окна
        self.txt_user.setGeometry(10, 40, 280, 20)

        self.txt_user1 = self.txt_user
        self.txt_user.textEdited.connect(self.read_txt)

        self.read_txt1()

    def read_txt1(self):
        txt_products = QTextEdit(self)
        txt_products.setGeometry(10, 80, 280, 450)
        txt_products.clear()
        products = getAllProducts()
        output = ""
        if self.txt_user != '\n':
            for p in products:
                if (p["name"].find(self.txt_user.text()) == 0) or (self.txt_user.text() == ''):
                    output += p["name"] + "\n"
        txt_products.setText(output)
        txt_products.show()
        self.show()

    def read_txt(self):
        window.read_txt1()

if __name__ == "__main__":

    app = QApplication([])
    window = AWProducts()
    app.exec()