# Form implementation generated from reading ui file '.\VentanaAgregarDocente.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmAgregarProfesor(object):
    def setupUi(self, frmAgregarProfesor):
        frmAgregarProfesor.setObjectName("frmAgregarProfesor")
        frmAgregarProfesor.resize(750, 600)
        frmAgregarProfesor.setMinimumSize(QtCore.QSize(750, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/icono_principal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        frmAgregarProfesor.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(parent=frmAgregarProfesor)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 90, 671, 391))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblCedula = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.lblCedula.setFont(font)
        self.lblCedula.setObjectName("lblCedula")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblCedula)
        self.txtCedula = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.txtCedula.setFont(font)
        self.txtCedula.setObjectName("txtCedula")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCedula)
        self.lblPrimerNombre = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.lblPrimerNombre.setFont(font)
        self.lblPrimerNombre.setObjectName("lblPrimerNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblPrimerNombre)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName("txtNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtNombre)
        self.lblPrimerApellido = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.lblPrimerApellido.setFont(font)
        self.lblPrimerApellido.setObjectName("lblPrimerApellido")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblPrimerApellido)
        self.txtApellido = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.txtApellido.setFont(font)
        self.txtApellido.setObjectName("txtApellido")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtApellido)
        self.lblEmail = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblEmail)
        self.txtEmail = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtEmail)
        self.lblCelular = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.lblCelular.setFont(font)
        self.lblCelular.setObjectName("lblCelular")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblCelular)
        self.txtCelular = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.txtCelular.setFont(font)
        self.txtCelular.setObjectName("txtCelular")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCelular)
        self.lblAgregarDocente = QtWidgets.QLabel(parent=frmAgregarProfesor)
        self.lblAgregarDocente.setGeometry(QtCore.QRect(20, 30, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(18)
        self.lblAgregarDocente.setFont(font)
        self.lblAgregarDocente.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblAgregarDocente.setObjectName("lblAgregarDocente")
        self.layoutWidget = QtWidgets.QWidget(parent=frmAgregarProfesor)
        self.layoutWidget.setGeometry(QtCore.QRect(122, 520, 531, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAgregarDocente = QtWidgets.QPushButton(parent=self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/agregar_docente.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAgregarDocente.setIcon(icon1)
        self.btnAgregarDocente.setIconSize(QtCore.QSize(24, 24))
        self.btnAgregarDocente.setObjectName("btnAgregarDocente")
        self.horizontalLayout.addWidget(self.btnAgregarDocente)
        self.btnCancelar = QtWidgets.QPushButton(parent=self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/cancelar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setIconSize(QtCore.QSize(24, 24))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)

        self.retranslateUi(frmAgregarProfesor)
        QtCore.QMetaObject.connectSlotsByName(frmAgregarProfesor)

    def retranslateUi(self, frmAgregarProfesor):
        _translate = QtCore.QCoreApplication.translate
        frmAgregarProfesor.setWindowTitle(_translate("frmAgregarProfesor", "::Sistema Gestión de Tareas:: Agregar Docente"))
        self.lblCedula.setText(_translate("frmAgregarProfesor", "Cedula:"))
        self.lblPrimerNombre.setText(_translate("frmAgregarProfesor", "Nombre: "))
        self.lblPrimerApellido.setText(_translate("frmAgregarProfesor", "Apellido:"))
        self.lblEmail.setText(_translate("frmAgregarProfesor", "Correo electrónico: "))
        self.lblCelular.setText(_translate("frmAgregarProfesor", "Celular:"))
        self.lblAgregarDocente.setText(_translate("frmAgregarProfesor", "Agregar Docente"))
        self.btnAgregarDocente.setText(_translate("frmAgregarProfesor", "Agregar Docente"))
        self.btnAgregarDocente.setShortcut(_translate("frmAgregarProfesor", "Return"))
        self.btnCancelar.setText(_translate("frmAgregarProfesor", "Cancelar"))
        self.btnCancelar.setShortcut(_translate("frmAgregarProfesor", "Esc"))
