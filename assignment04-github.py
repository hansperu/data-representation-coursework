import subprocess

def read_and_replace(filename, old_text, new_text):
    with open(filename, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(old_text, new_text)

    with open(filename, 'w') as file:
        file.write(filedata)

def git_commit_push(filename, commit_message):
    try:
        subprocess.run(['git', 'add', filename], check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Changes committed and pushed to repository.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = 'test.txt'  # Asegúrate de que 'test.txt' esté en el mismo directorio que este script
    old_text = 'Andrew'
    new_text = 'YourName'  # Reemplaza con tu nombre

    read_and_replace(file_path, old_text, new_text)
    git_commit_push(file_path, 'Replace Andrew with YourName')

