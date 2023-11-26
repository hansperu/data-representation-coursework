import mysql.connector

class StudentDAO:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='datarepresentation'
            )
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            raise

    def get_cursor(self):
        if not self.connection.is_connected():
            self.connection.reconnect()
        return self.connection.cursor()
    def create(self, values):
        cursor = self.get_cursor()
        sql = "INSERT INTO student (name, age) VALUES (%s, %s);"
        cursor.execute(sql, values)
        self.connection.commit()
        lastRowId = cursor.lastrowid
        cursor.close()
        return lastRowId

    def getAll(self):
        cursor = self.get_cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        return results

    def findByID(self, studentId):
        cursor = self.get_cursor()
        sql = "SELECT * FROM student WHERE id = %s"
        cursor.execute(sql, (studentId,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def update(self, values):
        cursor = self.get_cursor()
        sql = "UPDATE student SET name = %s, age = %s WHERE id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()

    def delete(self, studentId):
        cursor = self.get_cursor()
        sql = "DELETE FROM student WHERE id = %s"
        cursor.execute(sql, (studentId,))
        self.connection.commit()
        cursor.close()


    # Resto de métodos (create, getAll, findByID, update, delete)...

# Ejemplo de uso
if __name__ == '__main__':
    studentDAO = StudentDAO()
    print(studentDAO.getAll())
    newId = studentDAO.create(('John', 21))
    print("New student ID:", newId)

    # Resto del código para probar los métodos...
