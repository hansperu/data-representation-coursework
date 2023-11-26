import requests
import json

def get_repo_info(api_key, repo_url, output_file):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        repo_data = response.json()
        with open(output_file, 'w') as file:
            json.dump(repo_data, file, indent=4)
        print("Información del repositorio guardada")
    else:
        print("Error al obtener información", response.status_code)

# Uso del método
api_key = "password API"  # Reemplaza con tu clave API real
repo_url = "https://api.github.com/repos/hansperu/data-representation-coursework"
output_file = "repo_info.json"
get_repo_info(api_key, repo_url, output_file)
