import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget
from ui_index import ProductUI

class ProductApp(ProductUI):
    db_name = "database.db"

    def __init__(self):
        super().__init__()

        # Conectar señales a las funciones
        self.save_button.clicked.connect(self.add_product)
        self.delete_button.clicked.connect(self.delete_product)

        # Llenar la tabla al inicio
        self.get_products()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        self.table.setRowCount(0)
        query = "SELECT * FROM product ORDER BY name DESC"
        for row, (id, name, price) in enumerate(self.run_query(query)):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(price)))

    def add_product(self):
        name = self.name_input.text()
        price = self.price_input.text()
        if name and price.isdigit():
            query = "INSERT INTO product VALUES(NULL, ?, ?)"
            self.run_query(query, (name, price))
            QMessageBox.information(self, "Success", f"Product {name} added!")
            self.name_input.clear()
            self.price_input.clear()
            self.get_products()
        else:
            QMessageBox.warning(self, "Error", "Name and valid Price are required!")

    def delete_product(self):
        selected = self.table.currentRow()
        if selected >= 0:
            name = self.table.item(selected, 0).text()
            query = "DELETE FROM product WHERE name = ?"
            self.run_query(query, (name,))
            QMessageBox.information(self, "Deleted", f"Product {name} deleted!")
            self.get_products()
        else:
            QMessageBox.warning(self, "Error", "No product selected!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec_())