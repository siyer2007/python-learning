library = {
    "Fiction": {
        "Novels": ["Book1", "Book2"],
        "Short Stories": ["Book3"]
    },
    "Non-Fiction": {
        "Biographies": ["Book4"],
        "Self-Help": ["Book5", "Book6"]
    }
}

def print_books(library):
    for key, value in library.items():
        if isinstance(value, list):
            for book in value:
                print(book)
        else:
            print_books(value)