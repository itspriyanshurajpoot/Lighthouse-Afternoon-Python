# import mysql.connector

from mysql.connector import connect, ProgrammingError

def createConnection():
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="priyanshu",
            database="class_db"
        )

        print("Connection established successfully")
        

        return connection

    except ProgrammingError as e:
        print(f"{type(e).__name__} : Failed to establish connection")


def insertData() :
    connection = createConnection()
    query = """
    INSERT INTO employee 
    VALUES (102, "PQR", 23, 2000)
    """
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.rowcount
    print(f"{rows} inserted...")
    connection.commit()

def selectData():
    connection = createConnection()
    cursor = connection.cursor()

    query = "select * from employee"
    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        print(f"Employee id is {row[0]}, Name is {row[1]}, Age is {row[2]} and salary is {row[3]}")

    print(data)

# insertData()
selectData()