# business_logic.py
# This is the Business Logic Layer

from data_access import get_all_books

def search_books(query):
    query = query.lower()
    all_books = get_all_books()
    results = []

    for book in all_books:
        if query in book['title'].lower() or query in book['author'].lower():
            results.append(book)

    return results
