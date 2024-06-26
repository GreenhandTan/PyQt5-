from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from ui.add_book_window import Ui_Form
from util.books_rep import getBooksMessage
from util.common_util import msg_box, get_current_time, APP_ICON, SYS_STYLE
# from util.common_util import msg_box, get_current_time, APP_ICON
from util.dbutil import DBHelp


class AddBookWindow(Ui_Form, QWidget):
    add_book_don_signal = pyqtSignal()

    def __init__(self):
        super(AddBookWindow, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('添加新图书')
        self.add_book_pushButton.clicked.connect(self.add)
        self.add_book_pushButton_2.clicked.connect(self.list_add)
        self.setWindowIcon(QIcon(APP_ICON))
        self.add_book_pushButton.setProperty('class', 'Aqua')
        self.add_book_pushButton_2.setProperty('class', 'Aqua')
        self.setStyleSheet(SYS_STYLE)

    def add(self):
        book_name = self.book_name_lineEdit.text()
        author = self.author_lineEdit.text()
        publish_company = self.publish_company_lineEdit.text()
        publish_date = self.publish_date_lineEdit.text()
        store_num = self.store_num_lineEdit.text()
        if '' in [book_name, author, publish_company, publish_date, store_num]:
            msg_box(self, '错误', '请输入图书的关键信息!')
            return
        db = DBHelp()
        count, res = db.query_super(table_name='book', column_name='book_name', condition=book_name)
        if count:
            msg_box(self, '错误', '已存在同名书籍!')
            return
        book_info = [book_name, author, publish_company, store_num, 0, get_current_time(), publish_date]
        db.add_book(data=book_info)
        db.db_commit()
        db.instance = None
        del db
        self.add_book_don_signal.emit()
        self.close()
        msg_box(self, '提示', '添加新图书成功!')

    def list_add(self):
        db = DBHelp()
        books = getBooksMessage()
        # print(books)
        for sign_data in books:
            # print(sign_data)
            db.add_book(data=sign_data)
        db.db_commit()
        db.instance = None
        del db
        self.add_book_don_signal.emit()
        self.close()
        msg_box(self, '提示', '爬虫批量添加新图书成功!')
