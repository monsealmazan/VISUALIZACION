from PyQt5 import QtWidgets, uic
from messagebox import msg_about, msg_error
import sqlite3 as sql

# iniciar la aplicación
app = QtWidgets.QApplication([])
# Cargar archivos .ui
login= uic.loadUi("usuario.ui")
entrada=uic.loadUi("entreada.ui")
error=uic.loadUi("dje9.ui")
registro=uic.loadUi("untitled.ui")

try:
    con = sql.connect("base de datos.db")
    con.commit()
    con.close()
except:
    print("Error de conexion a la base de datos :(")

def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(name)==0 or len(password)==0:
        login.label_6.setText("Ingrese todos los datos")
    else:
        con = sql.connect("base de datos.db")
        cursor = con.cursor()
        cursor.execute('SELECT Nombre, contraseña FROM usuarios WHERE nombre = ? AND contraseña = ?',(name, password))
        if cursor.fetchall():
            gui_entrar()
        else:
            msg_error("Error", "El usuario o la contraseña son incorrectas porfavor de verificar")

def crear_tabla():
    con = sql.connect("base de datos.db")
    cursor = con.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS usuarios (
            nombre text,
            apellido_paterno text, 
            apellido_materno text, 
            edad integer, sexo text, 
            pais text,
            correo text,
            contraseña text )""")
    con.commit()
    con.close()

def registrar(nombre, ap, am, edad, sex, pais, mail, contraseña):
    con = sql.connect("base de datos.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO usuarios VALUES ('{nombre}', '{ap}', '{am}'," \
        f"'{edad}', '{sex}', '{pais}', '{mail}', '{contraseña}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def datos():
    nombre = registro.lineEdit.text()
    apellido_p = registro.lineEdit.text_2()
    apellido_m = registro.lineEdit.text_3()
    edad = int(registro.lineEdit.text_4()) 
    box = str(registro.combobox.currentText())
    pais = registro.lineEdit.text_5.text()
    correo = registro.lineEdit.text_7.text()
    contraseña = registro.lineEdit.text_6.text()
    contraseña_2 = registro.lineEdit.text_8.text()
    if contraseña != contraseña_2:
        msg_error("Error", "Las contraseñas no son iguales...")
    elif contraseña == contraseña_2:
        registrar(nombre, apellido_p, apellido_m, edad, box, pais, correo, contraseña)
        msg_about("Éxito!", "Se ha registrado exitosamente! \n Tu nombre es tu usuario")
        registro.line_nombre.setText("")
        registro.line_ap.setText("")
        registro.line_am.setText("")
        registro.line_edad.setText("") 
        registro.line_cel.setText("")
        registro.line_correo.setText("") 
        registro.line_contra.setText("")
        registro.line_contra_2.setText("")

def gui_entrar():
    login.hide()
    entrada.show()

def gui_error():
    login.hide()
    error.show()
    

def regresar_entrada():
    entrada.hide()
    login.label_6.settext("")
    login.show()

def regresar_ini():
    error.hide()
    login.show()
    

def salir():
    app.exit()



login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)

entrada.pushButton.clicked.connect(regresar_entrada)
entrada.pushButton_2.clicked.connect(salir)


error.pushButton_2.clicked.connect(regresar_ini)



login.show()
app.exec()


#def gui_entrar():
# login.hide()    
# entrar.show()
# def gui_registrar():    
# login.hide()    
# forma.show()    
# 
# crear_tabla()def regresar_forma():    forma.hide()    login.show()def regresar_entrar():    entrar.hide()    login.label_5.setText("")    login.show()def salir():    app.exit()# Botones de loginlogin.pushButton.clicked.connect(gui_login)login.pushButton_3.clicked.connect(gui_registrar)login.pushButton_2.clicked.connect(salir)# Botones de entrarentrar.pushButton.clicked.connect(regresar_entrar)entrar.pushButton_2.clicked.connect(salir)# Botones de formforma.btn_regresar.clicked.connect(regresar_forma)forma.btn_registrar.clicked.connect(datos)# Ejecutablelogin.show()app.exec()