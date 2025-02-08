import mysql.connector
from mysql.connector import Error

class PacientesDB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='1234',
                database='pacientes'
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.conn = None
            self.cursor = None

    def crear_tabla(self):
        if self.cursor:
            query = """
                CREATE TABLE IF NOT EXISTS pacientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    apellido VARCHAR(100) NOT NULL,
                    telefono VARCHAR(8),
                    direccion VARCHAR(35),
                    tiposangre VARCHAR(3)
                );
            """
            try:
                self.cursor.execute(query)
                self.conn.commit()
                print("Tabla 'pacientes' creada o ya existente.")
            except Error as e:
                print(f"Error al crear la tabla: {e}")

    def registrar_pacientes(self, nombre, apellido, telefono, direccion, tiposangre):
        if self.cursor:
            sql = """
                INSERT INTO pacientes (nombre, apellido, telefono, direccion, tiposangre)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (nombre, apellido, telefono, direccion, tiposangre)
            try:
                self.cursor.execute(sql, valores)
                self.conn.commit()
                print(f"Pacientes {nombre} {apellido} registrado exitosamente.")
            except Error as e:
                print(f"Error al registrar pacientes: {e}")

    def cerrar_conexion(self):
        if self.cursor and self.conn:
            self.cursor.close()
            self.conn.close()
            print("Conexión cerrada.")

# Crear instancia y tabla
pacientes = PacientesDB()
pacientes.crear_tabla()

# Obtener datos del usuario
nombre = input("Ingrese el nombre del paciente: ")
apellido = input("Ingrese el apellido del paciente: ")
telefono = input("Ingrese el telefono del paciente: ")
direccion = input("Ingrese la direccion del paciente: ")
tiposangre = input("Ingrese el tipo de sangre del paciente: ")

# Registrar paciente con los datos ingresados
pacientes.registrar_pacientes(nombre, apellido, telefono, direccion, tiposangre)

# Cerrar la conexión
pacientes.cerrar_conexion()