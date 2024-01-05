class Contact:
    def __init__(self):
        self.contact = {}
    
    def add_contact(self, name, phone, email=None):
        if name in self.contact:
            print("User alredy existed!")
            return
        
        if not email:
            self.contact[name] = {'phone': phone}
        else:
            self.contact[name] = {'phone': phone, 'email': email}
        
    def view_contact(self, ):
        for name, info in self.contact.items():
            print(f"name: {name}")
            print(f"phone: {info['phone']}")
            print(f"emai: {info['email']}")
            print("_" * 50)
    
    def delete(self, name):
        if name in self.contact:
            del self.contact[name]
            print("your request is done!")
        else:
            print("user not found!")
    
    def update_contact(self, name, phone=None, email=None):
        if name in self.contact:
            if phone:
                self.contact[name]['phone'] = phone
            if email:
                self.contact[name]['email'] = email
        
            print("your request done!")
            
        if phone:
            print(f"phone number change to {phone}")
        if email:
            print(f"email address change to {email}")


if __name__ == "__main__":
        
    book = Contact()
    while True:
        print("\n Enput contact book")
        print("1 -> Add Contact")
        print("2 -> Edit Conta~ct")
        print("3 -> View Contact")
        print("4 -> Delete Contact")
        print("5 -> Quit")
        user_choice = input("Select your request: ")

        if user_choice == "5":
            break
        
        elif user_choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email(optional): ")

            book.add_contact(name, phone, email)

        elif user_choice == "2":
            print("for edit: ")
            name = input("Enter name: ")
            phone = input("Enter phone(optional): ")
            email = input("Enter email(optional): ")
            book.update_contact(name, phone, email)

        elif user_choice == "3":
            print("list of Contacts:")
            print("_" *50)
            book.view_contact()

        elif user_choice == "4":
            name = input("Enter name for delete: ")
            book.delete(name)
            