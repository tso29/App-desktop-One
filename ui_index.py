from PyQt5.QtWidgets import ( # type: ignore
    QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget
)

class ProductUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Products Application")
        self.setGeometry(200, 200, 600, 400)

        # Layout principal
        self.layout = QVBoxLayout(self)

        # Input Fields
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Name")
        self.layout.addWidget(self.name_input)

        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Price")
        self.layout.addWidget(self.price_input)

        # Buttons
        self.save_button = QPushButton("Save Product", self)
        self.layout.addWidget(self.save_button)

        self.delete_button = QPushButton("Delete Selected", self)
        self.layout.addWidget(self.delete_button)

        # Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Name", "Price"])
        self.layout.addWidget(self.table)