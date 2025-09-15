books = {}
users = {}
loans = []

print("=== LIBRARY ===")

while True:
    print("\n1. Add book")
    print("2. Add user") 
    print("3. Borrow book")
    print("4. Return book")
    print("5. View books")
    print("6. View users")
    print("7. View loans")
    print("0. Exit")
    
    op = input("Option: ")
    
    if op == '0':
        print("End")
        break
    
    elif op == '1':
        book_id = len(books) + 1
        title = input("Title: ")
        author = input("Author: ")
        quantity = int(input("Quantity: "))
        books[book_id] = {"title": title, "author": author, "total": quantity, "borrowed": 0}
        print(f"Book added with ID {book_id}")
    
    elif op == '2':
        user_id = input("User ID: ")
        name = input("Name: ")
        users[user_id] = {"name": name}
        print("User added")
    
    elif op == '3':
        user_id = input("User ID: ")
        if user_id not in users:
            print("User does not exist")
            continue
        book_id = int(input("Book ID: "))
        if book_id not in books:
            print("Book does not exist")
            continue
        book = books[book_id]
        if book["borrowed"] >= book["total"]:
            print("Not available")
            continue
        loans.append({"user": user_id, "book": book_id})
        book["borrowed"] += 1
        print("Book borrowed")
    
    elif op == '4':
        user_id = input("User ID: ")
        book_id = int(input("Book ID: "))
        for i, l in enumerate(loans):
            if l["user"] == user_id and l["book"] == book_id:
                loans.pop(i)
                books[book_id]["borrowed"] -= 1
                print("Book returned")
                break
        else:
            print("Loan not found")
    
    elif op == '5':
        print("\nBooks:")
        for book_id, book in books.items():
            available = book["total"] - book["borrowed"]
            print(f"{book_id}. {book['title']} - {book['author']} (Available: {available})")
    
    elif op == '6':
        print("\nUsers:")
        for user_id, user in users.items():
            print(f"{user_id} - {user['name']}")
    
    elif op == '7':
        print("\nLoans:")
        for l in loans:
            user = users[l["user"]]["name"]
            book = books[l["book"]]["title"]
            print(f"{user} has '{book}'")
    
    else:
        print("Invalid option")
