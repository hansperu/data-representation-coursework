import subprocess
import json

# Función para ejecutar comandos cURL usando subprocess
def run_curl_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# 1. Probar cURL con Google.com
print("1. Probar cURL con Google.com")
print(run_curl_command("curl -i google.com"))
print("-------------------------------------------------------------")

# 2. Obtener Todos los Libros desde la API
print("2. Obtener Todos los Libros desde la API")
print(run_curl_command("curl http://andrewbeatty1.pythonanywhere.com/books"))
print("-------------------------------------------------------------")

# 3. Obtener un Libro Específico por ID
print("3. Obtener un Libro Específico por ID")
book_id = 17 # Reemplazar con el ID del libro deseado
print(run_curl_command(f"curl http://andrewbeatty1.pythonanywhere.com/books/{book_id}"))
print("-------------------------------------------------------------")

# 4. Crear un Nuevo Libro
print("4. Crear un Nuevo Libro")
new_book = {"Title": "New Book", "Author": "John Doe", "Price": 1000}
command_create = f"curl -H \"Content-Type:application/json\" -X POST -d '{json.dumps(new_book)}' http://andrewbeatty1.pythonanywhere.com/books"
print(run_curl_command(command_create))
print("-------------------------------------------------------------")

# 5. Actualizar un Libro
print("5. Actualizar un Libro")
book_update = {"Price": 2000}
command_update = f"curl -H \"Content-Type:application/json\" -X PUT -d '{json.dumps(book_update)}' http://andrewbeatty1.pythonanywhere.com/books/{book_id}"
print(run_curl_command(command_update))
print("-------------------------------------------------------------")

# 6. Eliminar un Libro
print("6. Eliminar un Libro")
command_delete = f"curl -X DELETE http://andrewbeatty1.pythonanywhere.com/books/{book_id}"
print(run_curl_command(command_delete))
