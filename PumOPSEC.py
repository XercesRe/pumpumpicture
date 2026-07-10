import webbrowser

def search_google(option):
    queries = {
        1: "site:cosmote.ro filetype:pdf",
        2: "intitle:\"index of\" \"parent directory\"",
        3: "filetype:pdf romtelecom",
        4: "site:cosmote.ro intitle:\"index of\"",
        5: "https://cosconor.fr/GSM/Acoperire/Romania/Cosmote/"
    }
    
    if option in queries:
        webbrowser.open(f"https://www.google.com/search?q={queries[option]}")
    else:
        print("Invalid option. Please choose a valid number.")

print("Choose an option to search on Google:")
print("1: site:cosmote.ro filetype:pdf")
print("2: intitle:\"index of\" \"parent directory\"")
print("3: filetype:pdf romtelecom")
print("4: site:cosmote.ro intitle:\"index of\"")
print("5: Open link")

user_choice = int(input("Enter your choice (1-5): "))
search_google(user_choice)
