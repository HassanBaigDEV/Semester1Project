import mysql.connector


db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="DBMS_database"
   
    )
    
mycursor = db.cursor()

Q1="""CREATE TABLE tours(tour_ID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
tour_name CHAR(20),
start_date DATE,
end_date DATE,
source CHAR(30),
destination CHAR(30),
price int,
total_no_tourist int
avail_seats int
  )"""
Q2="""CREATE TABLE driver(driver_ID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
driver_CNIC bigint,
age int,
lisc_no bigint,
phone int(11))"""
Q3="""CREATE TABLE hotel
(hotel_ID int PRIMARY KEY AUTO_INCREMENT,
hotel_name VARCHAR(20),
hotel_phone int(11),
address VARCHAR(60),
tour_ID int,
FOREIGN KEY (tour_ID) REFERENCES tours(tour_ID))"""
Q4="""CREATE TABLE tourist(
    tourist_ID INT PRIMARY KEY AUTO_INCREMENT,
    tourist_name VARCHAR(15),
    phone int(11),
    email VARCHAR(30),
    age int(3),
    address VARCHAR(50),
    CNIC bigint)"""
Q5="""CREATE TABLE vehicle(
    vehicle_ID int PRIMARY KEY AUTO_INCREMENT,
    vehicle_no int,
    chasis_no bigint,
    model VARCHAR(13),
    reg_year int)"""
Q6="""CREATE TABLE transport(
    trans_ID int PRIMARY KEY AUTO_INCREMENT,
    vehicle_ID int,
    FOREIGN KEY(vehicle_ID) REFERENCES vehicle(vehicle_ID),
    driver_ID int,
    FOREIGN KEY(driver_ID) REFERENCES driver(driver_ID),
    tour_ID int,
    FOREIGN KEY(tour_ID) REFERENCES tours(tour_ID))"""
Q7="""CREATE TABLE reservation(
    R_ID int PRIMARY KEY AUTO_INCREMENT,
    tour_ID int,
    FOREIGN KEY(tour_ID) REFERENCES tours(tour_ID),
    tourist_ID int,
    FOREIGN KEY(tourist_ID) REFERENCES tourist(tourist_ID))"""   
Q8="""CREATE TABLE users(
    user_ID int PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(15) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(25) NOT NULL)
    """
Q9= "ALTER TABLE tours MODIFY COLUMN destination char(30)"
# mycursor.execute(Q9)
# db.commit()
# add_tourist_query="INSERT INTO tourist(tourist_name, phone, email, age, address,CNIC) VALUES (%s,%s,%s,%s,%s,%s)"
# mycursor.execute(add_tourist_query,("ali","123456","ali@test1.com","33","xyz","12344567245"))
# db.commit()

# x="tour_name"
# # # y="naran tour"
mycursor.execute("SELECT *FROM tours")
for i in mycursor:
    print(i)