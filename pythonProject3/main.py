# # This is a sample Python script.
#
# # Press F5 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# #burada bir fonksiyon var
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#

#kullanıcı bilgilerini ve sepet içeriklerini tutmak için bir veri yapısı oluştur
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.basket_items = []
        self.blocked = False


users = {
    "admin": User("admin", "qwerty"),
    "ahmet": User("ahmet", "123456"),
    "zeynep": User("zeynep", "4444"),
}


#burada kullanıcıdan kullanıcı adı ve şifre istenecek
def login():
    incorrectLogin = 0
    blocked = False

    while not blocked:
        #kullanıcı adını alıyoruz
        userName = input("""Please log in by providing your user credentials:
User Name:""")
        #kullanıcı şifresini alıyoruz
        password = input("Password:")

        if userName == "admin" and password == "qwerty":
            print("admin by logged in")
            admin_panel()
            return
            # eğer kullanıcı adı ve şifre doğruysa kullanıcı adını döndür değilse mesajı oku
        elif verify(userName, password):
            if userName not in users:
                users[userName] = User(userName, password)
                return users[userName]
            elif users[userName].username != "admin":
                print("You are already logged in!")
                return users[userName]
            else:
                return users[userName]
        else:
            incorrectLogin += 1
            # eğer yanlış giriş 3ten küçükse bu mesajı oku
            if incorrectLogin < 3:
                print("Your user name and/or password is not correct. Please try again!", 3 - incorrectLogin)
            # eğer yanlış giriş 3e denkse bu mesajı oku
            if incorrectLogin == 3:
                blocked = True
                print("""Your user name and/or password is not correct.
Your account has been blocked. please contact the administrator.""")

#kullanıcı adı ve şifre doğrulama
def verify(userName, password):
    #kullanıcı adı VE şifrenin ikisinin de doğru olup olmadığını kontrol et
    if userName in users:
        if users[userName].password == password:
            return True
        elif userName == "admin" and password == "qwerty":
            return True
    return False

#admin menüsü
def admin_menu():
    print("""Please choose one of the following services:
1. Activate User Account
2. Deactivate User Account
3. Add User
4. Remove User
5. Logout
6. Exit""")


def admin_panel():
    while True:
        admin_menu()
        admin_choice = input("Your Choice: ")

        if admin_choice == "1":
            blocked_username = input("Enter the username of the blocked account you want to reactivate: ")
            if blocked_username in users and users[blocked_username].blocked:
                users[blocked_username].blocked = False
                print(f"User account '{blocked_username}' has been reactivated.")
            else:
                print("Invalid username or user account is not blocked.")


        elif admin_choice == "2":
            username_to_block = input("Enter the username of the account you want to deactivate (block): ")
            if username_to_block in users and not users[username_to_block].blocked:
                users[username_to_block].blocked = True
                print(f"User account '{username_to_block}' has been deactivated (blocked).")
            else:
                print("Invalid username or user account is already blocked.")


        elif admin_choice == "3":
            # admin tarafından eklenen yeni kullanıcı
            new_username = input("Enter the new username: ")
            new_password = input("Enter the new password: ")
            if new_username not in users:
                users[new_username] = User(new_username, new_password)
                print(f"New user '{new_username}' has been added.")
            else:
                print("Username already exists. Please choose another username.")


        elif admin_choice == "4":
            # admin tarafından silinen kullanıcı
            user_to_remove = input("Enter the username of the account you want to remove: ")
            if user_to_remove in users:
                del users[user_to_remove]
                print(f"User account '{user_to_remove}' has been removed.")
            else:
                print("Invalid username.")


        elif admin_choice == "5":
            # admin logout
            print("Admin logged out.")
            logout(user)
            break

        elif admin_choice == "6":
            # exit
            exit()

        else:
            print("Invalid menu entry! Try again")


#menüler
def menu(user):

    print("""
Please choose one of the following services:
1. Search for a product
2. See Basket
3. Check Out
4. Logout
5. Exit
""")

#ürünler için dictionary kullandım
products = {
    "asparagus": {"Stock Amount":10, "Price": 5},
    "broccoli": {"Stock Amount":15, "Price": 6},
    "carrots": {"Stock Amount":18, "Price": 7},
    "apples": {"Stock Amount":20, "Price": 5},
    "banana": {"Stock Amount":10, "Price": 8},
    "berries": {"Stock Amount":30, "Price": 3},
    "eggs": {"Stock Amount":50, "Price": 2},
    "mixed fruit juice": {"Stock Amount":0, "Price": 8},
    "fish sticks": {"Stock Amount":25, "Price": 12},
    "apple juice": {"Stock Amount":40, "Price": 7},
    "orange juice": {"Stock Amount":30, "Price": 8},
    "grape juice": {"Stock Amount":10, "Price": 9},
}

#kullanıcının sepeti(liste)
basket_items = []

def basket_submenu():
    print("Basket Submenu:")
    if not basket_items:
        print("Your basket is empty.")
        total_cost = 0
    else:
        total_cost = 0
        for index, item in enumerate(basket_items, start=1):
            product_name, price, amount, total_price = item
            total_cost += total_price
            print(f"{index}. {product_name} - price: {price}$ - amount: {amount} - total: {total_price}$")

    print(f"Total cost: {total_cost}$")

    while True:
        print("""
Please choose an option:
1.Update amount
2.Remove an item
3.Check out
4.Go back to main menu""")
        selection = input("Your selection: ")

        if selection == "1":
            #kullanıcı sepetinden ürün seçip miktarını güncelleyecek
            if not basket_items:
                print("Your basket is empty.")
            else:
                #sepetteki ürünleri listele
                print("Your basket now contains:")
                for index, item in enumerate(basket_items, start=1):
                    product_name, price, amount, total_price = item
                    total_cost += total_price
                    print(f"{index}. {product_name} - price: {price}$ - amount: {amount} - total: {total_price}$")

                #hangi öğenin miktarını değiştirmek istediğini seçtir
                index = int(input("Please select which item to change its amount: "))
                if 1 <= index <= len(basket_items):
                    new_amount = int(input("Please type the new amount: "))
                    if new_amount <= products[basket_items[index - 1][0]]["Stock Amount"]:
                        #yeni miktarı güncelle
                        basket_items[index - 1] = (basket_items[index - 1][0], basket_items[index - 1][1], new_amount, basket_items[index - 1][1] * new_amount)
                        print("Your basket now contains:")

                        #güncellenmiş sepeti göster
                        for index, item in enumerate(basket_items, start=1):
                            product_name, price, amount, total_price = item
                            print(f"{index}.{product_name} price={price}$ amount={amount} total={total_price}$")
                        else:
                            print("Sorry! The amount exceeds the limit.")
                    else:
                        print("Invalid index.")

        elif selection == "2":
            #kullanıcı sepetinden çıkarılacak bir ürünü seçecek
            if not basket_items:
                print("Your basket is empty.")
            else:
                index = int(input("Enter the index of the item you want to remove: "))
                if 1 <= index <= len(basket_items):
                    removed_item = basket_items.pop(index - 1)
                    print(f"{removed_item[0]} removed from basket.")
                else:
                    print("Invalid index.")

        elif selection == "3":
            for item in basket_items:
                product_name, price, amount, total_price = item
                products[product_name]["Stock Amount"] -= amount
                # Print receipt
            print_receipt()
            break


        elif selection == "4":
            #kullanıcı logout olur
            logout(user)
        else:
            print("Invalid selection. Please choose a valid option.")


def print_receipt():
    print("Processing your receipt...")
    print(""""
******* XLC Online Market ********
**************************************
444 8 000
xtremelab.co
————————————""")
    #sepetteki ürünler
    for item in basket_items:
        product_name, price, amount, total_price = item
        # print(f"- {product_name}: ${price} x {amount} = ${total_price}")
        print(f"{product_name} price={price}$ amount={amount} total={total_price}$")

    print("————————————")

    #toplamı göster
    total_cost = sum(item[3] for item in basket_items)
    print(f"Total: ${total_cost}")

    print("————————————")

    #tarihi ve saati göster
    import datetime
    print(datetime.datetime.now())
    print("Thank You for using our Market!")


#kullanıcı oturumunu kapatan fonk
def logout(user):
    #sepet içeriğini kaydet
    user.basket_items.clear()
    print("Logged out successfully")
    user = None
    return None

#programı başlatma
if __name__ == '__main__':
    print("****Welcome to  XLC Online Market****")
    user = login()
    if user.username is not None:
        print("Successfully logged in!")

    if user.username == "admin":
        if user.password == "qwerty":
            print("admin by logged in")
            admin_panel()
        else:
            print("incorrect password for admin")
    else:
        print(f"Welcome, {user.username}! Please choose one of the following options by entering the corresponding menu number.")
        while True:
            menu(user)
            #seçim yaptır
            choice = input("Your Choice: ")

            #eğer 1.yi seçerse
            if choice == "1":
                while True:
                    #kullanıcının istediği ürün
                    request = input("What are you searching for? ").lower()
                    #0 yazarsa menüye döndür
                    if request == "0":
                        break
                    else:
                        #kullanıcının aradığı ürünü listelemek için sayaç koy
                        counter = 0
                        #aradığıyla eşleşen ürünleri koymak için boş bir liste
                        product_list = []
                        for product, information in products.items():
                            if request in product:
                                counter += 1
                                print(f"{counter}.", product, information["Price"], "$")
                                #eşleşen ürünleri listeye ekle (adı ve fiyatıyla birlikte)
                                product_list.append((product, information["Price"]))
                        if not product_list:
                            print("Your search did not match any items. Please try something else.")
                            continue
                        if product_list:
                            selected_index = int(input("Please select which item you want to add to your basket (Enter 0 for main menu):"))
                            if selected_index == "0":
                                break
                            else:
                                # kullanıcın seçtiği ürün
                                selected_product, price = product_list[selected_index - 1]
                                # kullanıcının istediği ürünün stok miktarı
                                basket_amount = int(input(f"Adding {selected_product}. Enter Amount: "))
                                while True:
                                    # stok miktarı yeterli mi
                                    if basket_amount <= products[selected_product]["Stock Amount"]:
                                        total_price = price * basket_amount
                                        #ürünü sepete ekle
                                        basket_items.append((selected_product, price, basket_amount, total_price))
                                        # sepete eklendi bilgisini ver
                                        print(f"Added {selected_product} into your Basket.")
                                        # sepete ekledikten sonra stok güncelle
                                        products[selected_product]["Stock Amount"] -= basket_amount
                                        break
                                    else:
                                        #stok miktarı yeterli değilse daha az girmesini iste
                                        print("Sorry! The amount exceeds the limit, Please try again with smaller amount")
                                        basket_amount = int(input("Amount (Enter 0 for main menu): "))
                                        if basket_amount == "0":
                                            break
                                        else:
                                            # uygun stok miktarı girilene kadar devam ettir
                                            continue
            elif choice == "2":
                basket_submenu()
            elif choice == "3":
                for item in basket_items:
                    product_name, price, amount, total_price = item
                    products[product_name]["Stock Amount"] -= amount
                    # Print receipt
                print_receipt()
                break
            elif choice == "4":
                logout(user)
                user = login()
            elif choice == "5":
                print("Exit")
                exit()
            else:
                print("Invalid menu entry! Try again")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
