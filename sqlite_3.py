import sqlite3 as db_object
from sqlite3 import Error
#_CONSTANTE_STRING_CONNECTION =["Username","password","nombre_db"]

def sqlite_create_database():
    try:
       conexion = db_object.connect ("my_second_database.db")
       return conexion
    except Error as err: 
       print(err) 

def create_table(connection):
    try:
       cursor = connection.cursor()
       cursor.execute("CREATE TABLE personal_adm(_id INTEGER PRIMARY KEY), puesto TEXT, salario INTEGER")
       connection.commit() 
    except Error: 
       print(Error, "Debio ser en el query!")

def insertar_new_row(connection, valores):
    try:
       cursor = connection.cursor()
       cursor.execute("INSERT INTO personal_adm(_id,puesto ,salario) VALUES (?,?,?) ",valores)
       connection.commit() 
    except Error: 
       print(Error, "Debio ser valores erroneos!")            


def actualizar_registro(connection):
    try:
       cursor = connection.cursor()
       cursor.execute("UPDATE personal_adm SET salario=23000  WHERE _id=123")
       connection.commit() 
    except Error: 
       print(Error, "Debio ser valores erroneos!")  


       ###########IMPLEMENTACION DE LAS FUNCIONES ANTERIORES###########################

objeto_coneccion = sqlite_create_database()
create_table(objeto_coneccion)

##creo tupletas con valores a inyectar en mi query
valores_1 = (123,"profesor",8000)
valores_2 = (777,"directora",300000)
valores_3 = (555,"programador",9)
         
         #_id(int pk),puesto(text),salario(int)
valores_dict = {
    1: valores_1,
    2: valores_2,
    3: valores_3
}
#inyecto inset into tatble con valores predeterminados 
for key in valores_dict:
    print(valores_dict[key])
    insertar_new_row(objeto_coneccion,valores_dict[key])

def get_all_row(connection):
    try:
       cursor = connection.cursor()
       cursor.execute("SELECT * FROM personal_adm")#solo ejecuta 
       objeto_resultado = cursor.fetchall()# muestra todos los registror¿s del query
       connection.commit()

       return objeto_resultado 
    except Error: 
       print(Error, "Debio ser valores erroneos!")  
resultado = get_all_row(objeto_coneccion)

for item in resultado:
    print("registro:  ",item)


actualizar_registro(objeto_coneccion)
for item in resultado:
    print("registro:  ",item)