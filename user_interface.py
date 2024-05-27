# Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.

from library_management_system import Book_Operations, User_Operations, Author_Operations, Genre_Operations
print("\nWELCOME TO THE LIBRARY MANAGEMENT SYSTEM!")

book_operations = Book_Operations()

while True:
    try:
        choice = int(input("""
        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Genre Operations
        5. Quit\n
        CHOICE: """))

        if choice == 1:
            while True:
                book_menu_choice = book_operations.book_menu()
                if book_menu_choice == 1:
                    book_operations.add_book()
                elif book_menu_choice == 2:
                    break

        elif choice == 2:
            user_operations = User_Operations("DKaila", book_operations.library)
            while True:
                user_menu_choice = int(input("""
                User Operations Menu:
                1. Borrow a book
                2. Return a book
                3. Display all books
                4. Quit\n
                CHOICE: """))
                if user_menu_choice == 1:
                    user_operations.borrow_book()
                elif user_menu_choice == 2:
                    user_operations.return_book()
                elif user_menu_choice == 3:
                    user_operations.display_book()
                elif user_menu_choice == 4:
                    break

        elif choice == 3:
            if not book_operations.library:
                print("ERROR: No books available. Please add a book first.")
                continue
            author_operations = Author_Operations(book_operations.library)
            author_operations.update_author()

        elif choice == 4:
            if not book_operations.library:
                print("ERROR: No books available. Please add a book first.")
                continue
            genre_operations = Genre_Operations(book_operations.library)
            genre_operations.update_genre()

        elif choice == 5:
            print("Library Management System Terminated!")
            break

        else:
            raise ValueError("ERROR: Choice must be an integer value within range of 1-5!")

    except ValueError as e:
        print("ERROR:", e)
