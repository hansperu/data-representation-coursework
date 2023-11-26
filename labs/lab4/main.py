import requests

API_URL = "http://andrewbeatty1.pythonanywhere.com/books"

def safe_request(func):
    """
    Decorador para manejar errores en las solicitudes.
    """
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()  # Lanza un error para respuestas fallidas
            if response.text:
                try:
                    return response.json()
                except ValueError:
                    return response.text  # Devuelve texto si la respuesta no es JSON
            else:
                return "No hay respuesta del servidor"
        except requests.exceptions.HTTPError as err:
            return f"Error HTTP: {err}"
        except requests.exceptions.RequestException as err:
            return f"Error en la solicitud: {err}"
    return wrapper

@safe_request
def read_books():
    return requests.get(API_URL)

@safe_request
def read_book(book_id):
    return requests.get(f"{API_URL}/{book_id}")

@safe_request
def create_book(book_data):
    return requests.post(API_URL, json=book_data)

@safe_request
def update_book(book_id, book_data):
    return requests.put(f"{API_URL}/{book_id}", json=book_data)

@safe_request
def delete_book(book_id):
    return requests.delete(f"{API_URL}/{book_id}")

def calculate_average_price(books):
    if not books:
        return 0
    total_price = sum(book.get('Price', 0) for book in books if isinstance(book, dict))
    return total_price / len(books) if books else 0

if __name__ == "__main__":
    all_books = read_books()
    print("Todos los libros:", all_books)

    book_id_to_read = 1  # Cambiar según sea necesario
    book = read_book(book_id_to_read)
    print(f"Libro específico (ID {book_id_to_read}):", book)

    new_book = {"Title": "Nuevo Libro", "Author": "Autor Ejemplo", "Price": 150}
    created_book = create_book(new_book)
    print("Libro creado:", created_book)

    # Actualizar un libro solo si existe
    book_id_to_update = 422  # Cambiar según sea necesario
    if read_book(book_id_to_update) != {}:
        updated_book_data = {"Price": 200}
        updated_book = update_book(book_id_to_update, updated_book_data)
        print(f"Libro actualizado (ID {book_id_to_update}):", updated_book)
    else:
        print(f"No se puede actualizar, el libro con ID {book_id_to_update} no existe")

    # Eliminar un libro solo si existe
    book_id_to_delete = 422  # Cambiar según sea necesario
    if read_book(book_id_to_delete) != {}:
        deleted_book = delete_book(book_id_to_delete)
        print(f"Libro eliminado (ID {book_id_to_delete}):", deleted_book)
    else:
        print(f"No se puede eliminar, el libro con ID {book_id_to_delete} no existe")

    average_price = calculate_average_price(all_books)
    print(f"Precio promedio de todos los libros: {average_price}")
