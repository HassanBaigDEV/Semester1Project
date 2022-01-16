import mysql.connector
from datetime import date
import re
from mysql.connector.errors import DataError

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="DBMS_database"
)

mycursor = db.cursor()


def sign_up():
    username = str(input("username:"))
    email = input("email:")
    password = str(input("password:"))

    def add_user():
        signup_query = "INSERT INTO users(username, email, password) VALUES (%s,%s,%s)"
        mycursor.execute(signup_query, (username, email, password))
        db.commit()

    if (username and email and password):
        check_data_query = "SELECT COUNT(*) FROM users WHERE username='" + \
            username+"' OR Email = '"+password+"'"
        mycursor.execute(check_data_query)
        myresult = mycursor.fetchone()
        if myresult == (0,):
            pass
        else:
            print('This username or email address already exists')
            sign_up()
        if (isValid(email)):
            add_user()
        else:
            while isValid(email) is False:
                print("Provided email is invalid. Please enter email again!")
                email = input("email:")
            add_user()
    tourist()


def signIn():
    username = str(input("username:"))
    password = (input("password:"))
    if (username and password):
        sql = "select * from users where username = %s and password = %s"
        mycursor.execute(sql, [(username), (password)])
        results = mycursor.fetchall()
        if results:
            for i in results:
                tourist()
                break
        else:
            print("NO SUCH USER EXISTS! ")
            print("Enter a Valid Email and Password")
            signIn()
    else:
        print("Enter a Valid Email and Password")
        signIn()


def admin():

    admin_menu = {"1": ("Add Tour", add_tours),
                  "2": ("List all Tours", tour_list),
                  "3": ("List all reservations", reservation_list),
                  "4": ("List all the users", list_users),
                  "5": ("Log Out", log_out)}

    menu(admin_menu)


def add_tours():
    tour_name = str(input("Enter the name of the tour:"))
    start_date = (input("Start Date(YYYYMMDD):"))
    if start_date <= date.today().strftime('%Y%m%d'):
        while start_date <= date.today().strftime('%Y%m%d'):
            print("Please enter a valid date!")
            start_date = (input("Start Date(YYYYMMDD):"))
    else:
        pass
    end_date = (input("End date(YYYYMMDD):"))
    source = str(input("Source Location:")).lower()
    destination = str(input("Destination:")).lower()
    price = (input("Price:"))
    max_tourists = (input("Max tourists:"))
    add_tour_query = "INSERT INTO tours(tour_name, start_date, end_date, source, destination,price, total_no_tourist,avail_seats) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    if tour_name and start_date and end_date and source and destination and price and max_tourists:
        try:
            mycursor.execute(add_tour_query, (tour_name, start_date, end_date,
                             source, destination, price, max_tourists, max_tourists))
            db.commit()
        except DataError as e:
            print("Enter Valid Data in all fields ")
            add_tours()
    else:
        print("Please Enter valid data in all fields")
        add_tours()
    add_tour_menu = {"1": ("Add another Tour", add_tours),
                     "2": ("Go back", admin)
                     }

    menu(add_tour_menu)


def tour_list():
    tour_list_menu = {"1": ("List All Tours", list_all_tours),
                      "2": ("Search a tour", search_tours),
                      "3": ("Go Back", admin),
                      }

    menu(tour_list_menu)


def list_all_tours():
    mycursor.execute("SELECT *FROM tours")
    for i in mycursor:
        print(i)

    list_all_tours_menu = {"1": ("Add another Tour", add_tours),
                           "2": ("Go back", tour_list),
                           }

    for i in sorted(list_all_tours_menu):
        print('Enter {} to {}'.format(i, list_all_tours_menu[i][0]))

    entry = input('Command: ')
    if entry in list_all_tours_menu:
        list_all_tours_menu[entry][1]()
    else:
        print("No such command")


def search_tours():
    x = input("Search by source location or destination (source/destination): ")
    y = input("Enter location: ")
    if x == ("source" or "destination") and y:
        sql = "select * from tours where {}='{}'"
        mycursor.execute(sql.format(x, y))
        results = mycursor.fetchall()
        if results:
            for i in results:
                print(i)
        else:
            print("NO SUCH TOUR EXISTS! ")
    else:
        print("Enter Valid Data!!")
        search_tours()

    search_tours_menu = {"1": ("Search another Tour", search_tours),
                         "2": ("Go back", tour_list), }

    menu(search_tours_menu)


def tour_list_users():
    ask1 = {"1": ("list all tours", list_all_tours_users),
            "2": ("search a tour", search_tours_users),
            "3": ("Go back", tourist)
            }
    menu(ask1)


def list_all_tours_users():
    mycursor.execute("SELECT *FROM tours")
    for i in mycursor:
        print(i)

    ask = {"1": ("Add another Tour", add_tours),
           "2": ("Go back", tour_list_users),
           }

    for i in sorted(ask):
        print('Enter {} to {}'.format(i, ask[i][0]))

    entry = input('Command: ')
    if entry in ask:
        ask[entry][1]()
    else:
        print("No such command")


def search_tours_users():
    x = input("Search by source location or destination (source/destination): ")
    y = input("Enter location: ")
    if x == ("source" or "destination") and y:
        sql = "select * from tours where {}='{}'"
        mycursor.execute(sql.format(x, y))
        results = mycursor.fetchall()
        if results:
            for i in results:
                print(i)
        else:
            print("NO SUCH TOUR EXISTS! ")
    else:
        print("Enter Valid Data!!")
        search_tours_users()

    search_tours_users_menu = {"1": ("Search another Tour", search_tours_users),
                               "2": ("Go back", tour_list_users),
                               }
    menu(search_tours_users_menu)


def reservation_list():
    reservation_list_menu = {"1": ("list all reservations", list_all_reservations),
                             "2": ("search a reservation", search_reservations),
                             }
    menu(reservation_list_menu)


def list_all_reservations():
    mycursor.execute("SELECT *FROM tourist")
    for i in mycursor:
        print(i)

    list_all_reservations_menu = {"1": ("Go back", reservation_list)}

    menu(list_all_reservations_menu)


def list_users():
    list_users_menu = {"1": ("List all users", list_all_users),
                       "2": ("Search a user", search_users),
                       "3": ("Go Back", admin)
                       }
    menu(list_users_menu)


def list_all_users():
    mycursor.execute("SELECT *FROM users")
    for i in mycursor:
        print(i)
    list_all_users_menu = {"1": ("Go back", list_users)
                           }
    menu(list_all_users_menu)


def search_users():
    username = input("Enter a username: ")
    if username:
        sql = "select * from users where username='{}'"
        mycursor.execute(sql.format(username))
        results = mycursor.fetchall()
        if results:
            for i in results:
                print(i)
        else:
            print("NO SUCH USER EXISTS! ")
    else:
        print("Enter Valid Data!!")
        search_tours()

    search_users_menu = {"1": ("Search again", search_users),
                         "2": ("Go Back", list_users)
                         }
    menu(search_users_menu)


def search_reservations():
    tourID = input("Enter Tour ID: ")
    try:
        mycursor.execute(
            "SELECT *FROM tourist WHERE tour_id ='{}'", format(tourID))
        for i in mycursor:
            print(i)
    except:
        print("NO SUCH RESERVATION EXISTS! ")

    ask12 = {"1": ("Search another reservation", search_reservations),
             "2": ("Go back", reservation_list),
             }

    menu(ask12)


def tourist():
    tourist_menu = {"1": ("Check all Tours", tour_list_users),
                    "2": ("Make a reservation", make_reservation),
                    "3": ("Log Out", log_out)}

    menu(tourist_menu)


def enter_info(tourID):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="DBMS_database"
    )

    mycursor = db.cursor()
    print("Please Enter the following information")
    tourist_name = str(input("Enter your name: "))
    phone = int(input("Contact number: "))
    email = (input("Email Address: "))
    age = int(input("Age: "))
    address = str(input("Address: ")).lower()
    CNIC = int(input("CNIC: "))

    add_tourist_query = "INSERT INTO tourist(tourist_name, phone, email, age, address,CNIC,tour_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    def add_tourist():
        mycursor.execute(add_tourist_query, (tourist_name,
                         phone, email, age, address, CNIC, tourID))
        db.commit()
    if tourist_name and phone and email and age and address and CNIC:
        if (isValid(email)):
            add_tourist()
        else:
            while isValid(email) is False:
                print("Provided email is invalid. Please enter email again!")
                email = input("email:")
            add_tourist()
    else:
        print("Please Enter valid data in all fields")
        enter_info()


def make_reservation():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="DBMS_database"
    )

    mycursor = db.cursor()
    mycursor.execute("SELECT *FROM tours")
    for i in mycursor:
        print(i)
        print("\n")
    tourID = input("Enter Tour ID: ")
    # seats available
    testquery = "select avail_seats from tours where tour_ID='{}'".format(
        tourID)
    mycursor.execute(testquery)
    for i in mycursor:

        if i[0] == 0:
            print("Sorry , no seats available")

        else:

            print("Available seats are " + str(i[0]))
            enter_info(tourID)
            print("Thanks for reservation")
            newi = i[0]-1
            query = "update tours set avail_seats='{}'".format(newi)
            mycursor.execute(query)
            db.commit()

    # Make reservation.

    # tourist info ? tourist info add in table
    # if tourID:
    #     insert_reservation_query="INSERT INTO reservation(tour_ID,tourist_ID) VALUES (%s,%s)"

    #     mycursor.execute((insert_reservation_query),(tourID,))


def isValid(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        print("Invalid email")
        return False


def main_start():
    start_menu1 = {"1": ("to login as an Admin", admin_start),
                   "2": ("to login as a User", user_start),
                   }

    for i in sorted(start_menu1):
        print('Enter {} to {}'.format(i, start_menu1[i][0]))

    entry = input('Command: ')
    if entry in start_menu1:
        start_menu1[entry][1]()
    else:
        print("No such command")


def user_start():
    start_menu = {"1": ("Sign In", signIn),
                  "2": ("Sign up", sign_up),
                  }

    menu(start_menu)


def admin_start():
    super_admin = {"username": "admin", "password": "admin"}

    username = str(input("username:"))
    password = str(input("password:"))
    if (username and password):
        if super_admin["username"] == username and super_admin["password"] == password:
            admin()
        else:
            print("WRONG CREDENTIALS!")
            admin_start()
    else:
        print("Enter a Valid username and Password")
        admin_start()
    admin()


def menu(self):
    for i in sorted(self):
        print('Enter {} to {}'.format(i, self[i][0]))
    entry = input('Command: ')

    if entry in self:
        self[entry][1]()
    else:
        print("No such command")
        menu(self)


def log_out():
    log_out_menu = {"1": ("Exit Program", exit),
                    "2": ("Login Again", main_start)
                    }
    menu(log_out_menu)


main_start()
