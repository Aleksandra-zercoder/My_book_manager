def show_books():
    # Строка, которую мы будем менять в разных ветках
    print("Список книг (ветка remove_book)")

    books = ["Граф Монте-Кристо", "Гордость и предубеждение"]
    for book in books:
        print("- " + book)

if __name__ == "__main__":
    show_books()
