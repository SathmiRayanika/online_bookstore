# main.py
# This is the Presentation Layer

from business_logic import search_books

def main():
    print("=== Welcome to the Online Bookstore ===")
    
    while True:
        query = input("\nEnter a book title or author to search (or type 'exit' to quit): ")
        
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        
        results = search_books(query)
        
        if results:
            print(f"\nFound {len(results)} result(s):")
            for book in results:
                print(f"- {book['title']} by {book['author']}")
        else:
            print("No matching books found.")

if __name__ == "__main__": main()
