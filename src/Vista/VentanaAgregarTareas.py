# Form implementation generated from reading ui file '.\VentanaAgregarTareas.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmAgregarTarea(object):
    def setupUi(self, frmAgregarTarea):
        frmAgregarTarea.setObjectName("frmAgregarTarea")
        frmAgregarTarea.resize(750, 576)
        frmAgregarTarea.setMinimumSize(QtCore.QSize(750, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/icono_principal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        frmAgregarTarea.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(parent=frmAgregarTarea)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 70, 691, 415))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblTitulo = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lblTitulo.setObjectName("lblTitulo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblTitulo)
        self.txtTitulo = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.txtTitulo.setObjectName("txtTitulo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtTitulo)
        self.lblPrioridad = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lblPrioridad.setObjectName("lblPrioridad")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblPrioridad)
        self.cbxPrioridad = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.cbxPrioridad.setObjectName("cbxPrioridad")
        self.cbxPrioridad.addItem("")
        self.cbxPrioridad.addItem("")
        self.cbxPrioridad.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbxPrioridad)
        self.lblAsignatura = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lblAsignatura.setObjectName("lblAsignatura")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblAsignatura)
        self.cbxAsignatura = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.cbxAsignatura.setObjectName("cbxAsignatura")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbxAsignatura)
        self.lblDescripcion = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lblDescripcion.setObjectName("lblDescripcion")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblDescripcion)
        self.rtxtDescripcion = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
        self.rtxtDescripcion.setObjectName("rtxtDescripcion")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.rtxtDescripcion)
        self.lblFechaLimite = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lblFechaLimite.setObjectName("lblFechaLimite")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblFechaLimite)
        self.lblSubTareas = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lblSubTareas.setObjectName("lblSubTareas")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblSubTareas)
        self.jgdTablaSubTareas = QtWidgets.QTableWidget(parent=self.formLayoutWidget)
        self.jgdTablaSubTareas.setObjectName("jgdTablaSubTareas")
        self.jgdTablaSubTareas.setColumnCount(0)
        self.jgdTablaSubTareas.setRowCount(0)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jgdTablaSubTareas)
        self.dtpFechaLimite = QtWidgets.QDateTimeEdit(parent=self.formLayoutWidget)
        self.dtpFechaLimite.setCalendarPopup(True)
        self.dtpFechaLimite.setObjectName("dtpFechaLimite")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dtpFechaLimite)
        self.lblEstadoActual = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lblEstadoActual.setObjectName("lblEstadoActual")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblEstadoActual)
        self.cbxEstadoActual = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.cbxEstadoActual.setObjectName("cbxEstadoActual")
        self.cbxEstadoActual.addItem("")
        self.cbxEstadoActual.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbxEstadoActual)
        self.lblAgregarTarea = QtWidgets.QLabel(parent=frmAgregarTarea)
        self.lblAgregarTarea.setGeometry(QtCore.QRect(30, 20, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblAgregarTarea.setFont(font)
        self.lblAgregarTarea.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.lblAgregarTarea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblAgregarTarea.setObjectName("lblAgregarTarea")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=frmAgregarTarea)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 500, 691, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAgregarSubTarea = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/agregar_tarea.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAgregarSubTarea.setIcon(icon1)
        self.btnAgregarSubTarea.setIconSize(QtCore.QSize(24, 24))
        self.btnAgregarSubTarea.setObjectName("btnAgregarSubTarea")
        self.horizontalLayout.addWidget(self.btnAgregarSubTarea)
        self.btnEliminarSubTarea = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/eliminar_tarea.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnEliminarSubTarea.setIcon(icon2)
        self.btnEliminarSubTarea.setIconSize(QtCore.QSize(24, 24))
        self.btnEliminarSubTarea.setObjectName("btnEliminarSubTarea")
        self.horizontalLayout.addWidget(self.btnEliminarSubTarea)
        self.btnSubTareaCompletada = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/aceptar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSubTareaCompletada.setIcon(icon3)
        self.btnSubTareaCompletada.setIconSize(QtCore.QSize(24, 24))
        self.btnSubTareaCompletada.setObjectName("btnSubTareaCompletada")
        self.horizontalLayout.addWidget(self.btnSubTareaCompletada)
        self.btnCrearTarea = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/guardar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCrearTarea.setIcon(icon4)
        self.btnCrearTarea.setIconSize(QtCore.QSize(24, 24))
        self.btnCrearTarea.setObjectName("btnCrearTarea")
        self.horizontalLayout.addWidget(self.btnCrearTarea)
        self.btnCancelar = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/cancelar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCancelar.setIcon(icon5)
        self.btnCancelar.setIconSize(QtCore.QSize(24, 24))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)

        self.retranslateUi(frmAgregarTarea)
        QtCore.QMetaObject.connectSlotsByName(frmAgregarTarea)

    def retranslateUi(self, frmAgregarTarea):
        _translate = QtCore.QCoreApplication.translate
        frmAgregarTarea.setWindowTitle(_translate("frmAgregarTarea", "::Sistema Gestión de Tareas:: Agregar Tareas"))
        self.lblTitulo.setText(_translate("frmAgregarTarea", "Titulo:"))
        self.lblPrioridad.setText(_translate("frmAgregarTarea", "Prioridad: "))
        self.cbxPrioridad.setItemText(0, _translate("frmAgregarTarea", "Alta"))
        self.cbxPrioridad.setItemText(1, _translate("frmAgregarTarea", "Media"))
        self.cbxPrioridad.setItemText(2, _translate("frmAgregarTarea", "Baja"))
        self.lblAsignatura.setText(_translate("frmAgregarTarea", "Asignatura: "))
        self.lblDescripcion.setText(_translate("frmAgregarTarea", "Descripción: "))
        self.lblFechaLimite.setText(_translate("frmAgregarTarea", "Fecha Límite:"))
        self.lblSubTareas.setText(_translate("frmAgregarTarea", "Sub tareas: "))
        self.lblEstadoActual.setText(_translate("frmAgregarTarea", "Estado actual:"))
        self.cbxEstadoActual.setItemText(0, _translate("frmAgregarTarea", "No Finalizada"))
        self.cbxEstadoActual.setItemText(1, _translate("frmAgregarTarea", "Finalizada"))
        self.lblAgregarTarea.setText(_translate("frmAgregarTarea", "Agregar Tarea"))
        self.btnAgregarSubTarea.setText(_translate("frmAgregarTarea", "Agregar Sub Tarea"))
        self.btnAgregarSubTarea.setShortcut(_translate("frmAgregarTarea", "+"))
        self.btnEliminarSubTarea.setText(_translate("frmAgregarTarea", "Eliminar Sub Tarea"))
        self.btnEliminarSubTarea.setShortcut(_translate("frmAgregarTarea", "Del"))
        self.btnSubTareaCompletada.setText(_translate("frmAgregarTarea", "Sub Tarea Completada"))
        self.btnCrearTarea.setText(_translate("frmAgregarTarea", "Crear Tarea"))
        self.btnCrearTarea.setShortcut(_translate("frmAgregarTarea", "Ctrl+Return"))
        self.btnCancelar.setText(_translate("frmAgregarTarea", "Cancelar"))
        self.btnCancelar.setShortcut(_translate("frmAgregarTarea", "Esc"))
