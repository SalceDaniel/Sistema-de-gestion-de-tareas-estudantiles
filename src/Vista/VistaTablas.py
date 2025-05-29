from PyQt6 import QtWidgets


class VistaTablas:

    def inicializar_tabla(self, tabla: QtWidgets.QTableWidget):
        tabla.setRowCount(0)
        tabla.setSortingEnabled(True)
        tabla.setEnabled(True)
        tabla.setDragEnabled(False)
        tabla.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        tabla.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        tabla.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.NoDragDrop)
        tabla.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        tabla.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def obtener_dato_columa(self, tabla:QtWidgets.QTableWidget, columna):
        fila_seleccionada = tabla.currentRow()
        if fila_seleccionada >= 0:
            item = tabla.item(fila_seleccionada, columna)
            if item:
                return item.text()
        return None

