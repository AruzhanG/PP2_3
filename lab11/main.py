import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS phonebook_2(
            first_name VARCHAR(50) NOT NULL,
            id VARCHAR(50) PRIMARY KEY,
            study_year INT,
            phone_number VARCHAR(20) NOT NULL
            )"""
        )

    def search_records(pattern):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM phonebook_2 WHERE first_name LIKE %s OR id LIKE %s OR phone_number LIKE %s""",
                           ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                
    def create_user_list():
        user_list=[]

        while True:
            first_name=input("Enter first name (or type 'done' to finish):")
            if first_name.lower()=='done':
                break
            id=input("Enter id number")
            phone_num=input("Enter phone number:")

            user_list.append((first_name,id,phone_num))
        
        with connection.cursor() as cursor:
            cursor.executemany("INSERT INTO phonebook_2 (first_name, id, phone_number) VALUES (%s, %s, %s)", user_list)

    def delete_data(username=None, phone_number=None):
        with connection.cursor() as cursor:
            if username:
                cursor.execute("""DELETE FROM phonebook_2 WHERE first_name = %s """, (username))
            if phone_number:
                cursor.execute("""DELETE FROM phonebook_2 WHERE phone_number = %s""", (phone_number,))
except Exception as ex:
    print("[INFO] Error while working with PostgreSQL:", ex)
search_records("Ruslan")
create_user_list()
delete_data(phone_number="87777895432")