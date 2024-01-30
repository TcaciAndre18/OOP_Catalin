class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f'{self.title} by {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            return 'Nu există cărți în bibliotecă.'
        
        book_list = '\n'.join(book.display_info() for book in self.books)
        return f'Cărțile din bibliotecă sunt:\n{book_list}'


# Exemplu de utilizare:

library = Library()

while True:
    print("\n1. Adaugă carte")
    print("2. Afișează cărți")
    print("3. Ieșire")

    choice = input("Alege o opțiune: ")

    if choice == '1':
        title = input("Introdu titlul cărții: ")
        author = input("Introdu autorul cărții: ")
        new_book = Book(title, author)
        library.add_book(new_book)
        print("Carte adăugată cu succes!")
    elif choice == '2':
        print(library.display_books())
    elif choice == '3':
        break
    else:
        print("Opțiune invalidă. Te rog să alegi din nou.")
