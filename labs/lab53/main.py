from github import Github
import requests

# Configuración
# Reemplaza 'TU_CLAVE_API' con tu clave API real de GitHub
# Asegúrate de que esta clave no se suba a ningún repositorio público por seguridad
api_key = 'api_key'
usuario_github = 'hansperu'
nombre_repositorio = 'data-representation-coursework'

# Inicializar la conexión con GitHub utilizando PyGitHub
g = Github(api_key)

# Obtener el repositorio
repo = g.get_repo(f"{usuario_github}/{nombre_repositorio}")

# Imprimir la URL de clonación del repositorio
print("URL de Clonación del Repositorio:", repo.clone_url)

# Obtener información del archivo específico 'test.txt'
# Asegúrate de que 'test.txt' exista en tu repositorio
archivo_path = 'test.txt'
file_info = repo.get_contents(archivo_path)

# Leer el contenido actual del archivo
url_del_archivo = file_info.download_url
contenido_actual = requests.get(url_del_archivo).text
print("Contenido Actual del Archivo:", contenido_actual)

# Agregar más contenido al archivo
nuevo_contenido = contenido_actual + "\nTexto adicional añadido por el script."

# Actualizar el archivo en GitHub
respuesta_github = repo.update_file(file_info.path, "Actualización del archivo por script", nuevo_contenido, file_info.sha)
print("Archivo actualizado. URL del commit:", respuesta_github['commit'].html_url)
