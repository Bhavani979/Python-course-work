'''print("Welcome to Netflix")

users = []
logged_in = False
current_user = None

tv_shows = ["Stranger Things", "You", "Breaking Bad", "The Crown"]
movies = ["Extraction", "The Irishman", "Bird Box", "Enola Holmes"]
new_and_popular = ["3 Body Problem", "Beef", "The Night Agent", "Wednesday"]
languages = {
    "English": ["Bridgerton", "The Queen's Gambit"],
    "Hindi": ["Delhi Crime", "Sacred Games"],
    "Spanish": ["Money Heist", "Elite"],
    "Korean": ["All of Us Are Dead", "Crash Landing on You"]
}

# Registration/Login System
while not logged_in:
    print("\n1. Register\n2. Login")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")

        exists = False
        for user in users:
            if user["username"] == username:
                exists = True
                break

        if exists:
            print("Username already exists. Try another.")
        else:
            users.append({"username": username, "password": password})
            print("Registered successfully. Please login now.")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                logged_in = True
                current_user = user
                print("Login successful! Welcome", username)
                break
        if not logged_in:
            print("Invalid credentials.")

# Main Menu
while True:
    print("\n===== Netflix Menu =====")
    print("1. Home")
    print("2. TV Shows")
    print("3. Movies")
    print("4. New & Popular")
    print("5. Browse by Languages")
    print("6. Logout")

    option = input("Choose an option: ")

    if option == "1":
        print("\n Home - Featured Content")
        for content in tv_shows[:2] + movies[:2]:
            print("- ", content)

    elif option == "2":
        print("\n TV Shows")
        for show in tv_shows:
            print("- ", show)

    elif option == "3":
        print("\n Movies")
        for movie in movies:
            print("- ", movie)

    elif option == "4":
        print("\n New & Popular")
        for item in new_and_popular:
            print("- ", item)

    elif option == "5":
        print("\n Browse by Languages")
        for lang in languages:
            print(f"{lang}:")
            for show in languages[lang]:
                print("   -", show)

    elif option == "6":
        print("Goodbye! Thanks for using  Netflix!")
        break

    else:
        print("Invalid option. Try again.")
'''
print("Welcome to Netflix")

users = []
logged_in = False
current_user = None

plans = {
    "Mobile": 149,
    "Basic": 199,
    "Standard": 499,
    "Premium": 649
}

tv_shows = ["Stranger Things", "You", "Breaking Bad", "The Crown"]
movies = ["Extraction", "The Irishman", "Bird Box", "Enola Holmes"]
new_and_popular = ["3 Body Problem", "Beef", "The Night Agent", "Wednesday"]
languages = {
    "English": ["Bridgerton", "The Queen's Gambit"],
    "Hindi": ["Delhi Crime", "Sacred Games"],
    "Spanish": ["Money Heist", "Elite"],
    "Korean": ["All of Us Are Dead", "Crash Landing on You"]
}

# Registration/Login
while not logged_in:
    print("\n1. Register\n2. Login")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        exists = False
        for user in users:
            if user["username"] == username:
                exists = True
                break
        if exists:
            print("Username already exists.")
        else:
            users.append({
                "username": username,
                "password": password,
                "subscription": None,
                "watchlist": []
            })
            print("Registered successfully. Please login.")
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                logged_in = True
                current_user = user
                print("Login successful! Welcome", username)
                break
        if not logged_in:
            print("Invalid credentials.")

# Main Menu
while True:
    print("\n===== Netflix Menu =====")
    print("1. Subscribe / View Subscription")
    print("2. Home")
    print("3. TV Shows")
    print("4. Movies")
    print("5. New & Popular")
    print("6. Browse by Languages")
    print("7. Search")
    print("8. Watchlist")
    print("9. Logout")

    option = input("Choose an option: ")

    if option == "1":
        if current_user["subscription"] is None:
            print("\nAvailable Plans:")
            for plan in plans:
                print(f"- {plan} Plan : ₹{plans[plan]}/month")
            selected = input("Choose a plan (Mobile/Basic/Standard/Premium): ")
            if selected in plans:
                current_user["subscription"] = selected
                print("Subscribed to", selected, "Plan.")
            else:
                print("Invalid plan.")
        else:
            print("You are already subscribed to:", current_user["subscription"])

    elif option in ["2", "3", "4", "5", "6"]:
        if current_user["subscription"] is None:
            print("Please subscribe to access this feature.")
            continue

        if option == "2":
            print("\nHome - Featured Content")
            for content in tv_shows[:2] + movies[:2]:
                print("- ", content)

        elif option == "3":
            print("\nTV Shows")
            for show in tv_shows:
                print("- ", show)
            add = input("Add a show to your watchlist? (y/n): ")
            if add.lower() == 'y':
                name = input("Enter show name: ")
                current_user["watchlist"].append(name)
                print("Added to watchlist.")

        elif option == "4":
            print("\nMovies")
            for movie in movies:
                print("- ", movie)
            add = input("Add a movie to your watchlist? (y/n): ")
            if add.lower() == 'y':
                name = input("Enter movie name: ")
                current_user["watchlist"].append(name)
                print("Added to watchlist.")

        elif option == "5":
            print("\nNew & Popular")
            for item in new_and_popular:
                print("- ", item)
            add = input("Add to your watchlist? (y/n): ")
            if add.lower() == 'y':
                name = input("Enter the name: ")
                current_user["watchlist"].append(name)
                print("Added to watchlist.")

        elif option == "6":
            print("\nBrowse by Languages")
            for lang in languages:
                print(f"{lang}:")
                for show in languages[lang]:
                    print("  -", show)
            add = input("Add a movie to your watchlist? (y/n): ")
            if add.lower() == 'y':
                name = input("Enter the name: ")
                current_user["watchlist"].append(name)
                print("Added to watchlist.")

    elif option == "7":
        if current_user["subscription"] is None:
            print("Please subscribe to use search.")
        else:
            query = input("Enter title to search: ").lower()
            found = False
            for section in [tv_shows, movies, new_and_popular]:
                for item in section:
                    if query in item.lower():
                        print("Found:", item)
                        found = True
            for lang in languages:
                for item in languages[lang]:
                    if query in item.lower():
                        print("Found:", item, f"({lang})")
                        found = True
            if not found:
                print("No results found.")

    elif option == "8":
        
     
        if current_user["subscription"] is None:
           print("Please subscribe to access your watchlist.")
        else:
           print("\nWatchlist:")
           if len(current_user["watchlist"]) == 0:
              print("Your watchlist is empty.")
           else:
              for item in current_user["watchlist"]:
                 print("- ", item)



    elif option == "9":
        print("Goodbye! Thanks for using Netflix!")
        break

    else:
        print("Invalid option.")
