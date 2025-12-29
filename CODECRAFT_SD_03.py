import json
import os

file = "contacts.json"

if os.path.exists(file):
    with open(file, "r") as f:
        contacts = json.load(f)
else:
    contacts = []

while True:
    print("\n1.Add  2.View  3.Edit  4.Delete  5.Exit")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts.append({"name": name, "phone": phone, "email": email})

    elif choice == "2":
        for i in range(len(contacts)):
            c = contacts[i]
            print(i + 1, c["name"], c["phone"], c["email"])

    elif choice == "3":
        i = int(input("Number: ")) - 1
        contacts[i]["name"] = input("Name: ")
        contacts[i]["phone"] = input("Phone: ")
        contacts[i]["email"] = input("Email: ")

    elif choice == "4":
        i = int(input("Number: ")) - 1
        contacts.pop(i)

    elif choice == "5":
        with open(file, "w") as f:
            json.dump(contacts, f)
        break

    else:
        print("Invalid")