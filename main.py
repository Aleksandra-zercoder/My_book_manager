def show_books():

    print("Список книг (main)")

    # Строка, которую мы будем менять в разных ветках
    print("Список книг (add_book)")


    books = ["Граф Монте-Кристо", "Гордость и предубеждение"]
    for book in books:
        print("- " + book)

if __name__ == "__main__":
    show_books()

