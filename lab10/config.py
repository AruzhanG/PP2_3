import psycopg2 
import csv,sys
from main import host, user, password, db_name 
 
 

connection = psycopg2.connect 
connection.autocommit = True
try: 
    connection = psycopg2.connect( 
        host=host, 
        user=user, 
        password=password, 
        database=db_name 
    ) 
    connection.autocommit=True 
 
    #cursor=connection.cursor() 
 
    with connection.cursor() as cursor: 
        cursor.execute( 
            "SELECT version();" 
        ) 
 
        print(f"Server version: {cursor.fetchone()}") 
    # create new table
    
    #with connection.cursor() as cursor:
    #   cursor.execute("""CREATE TABLE phonebook_2(
    #        first_name varchar(50) NOT NULL,
    #        id varchar(255) PRIMARY KEY,
    #        study_year INT,
    #        phone_number varchar(20)
    #        );""")
     
       
    #print("[INFO] Table created succesfully")
    # insert data into a table
    #with connection.cursor() as cursor: 
    #    data = (input("first_name:"),input("id: "), input("study_year: "), input("phone_number: "))
    #    cursor.execute( 
    #        """INSERT INTO phonebook_2 (first_name, id, study_year,phone_number) VALUES 
    #        (%s,%s,%s,%s);""", data
    #    ) 
    #    print("[INFO] DATA was succesfully inserted")
        
    # insert data from csv file
    #with open('/Users/aruzhan/pp2_3/lab10/data.csv','r') as file:
    #    rows = csv.reader(file)
    #    for data in rows:
    #        with connection.cursor() as cursor:
    #            cursor.execute(
    #                """INSERT INTO phonebook_2(first_name,id,study_year,phone_number) VALUES(%s,%s,%s,%s);""",
    #                data
    #            )      
            
    #change user name
    
    #with connection.cursor() as cursor:
    #   cursor.execute("""UPDATE  phonebook_2
    #       SET first_name = 'Almas'
    #       WHERE id = '23B040506'
    #       """)
    #print("[INFO] The Data changed succesfully")
    
    #querying 
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM phonebook_2;
                       WHERE first_name = 'Zhibek';
                       ORDER BY """)
    
    #deleting
    #name=input("Name: ")
    #with connection.cursor() as cursor:
    #    cursor.execute(
    #        """DELETE FROM phonebook_2 WHERE first_name=%s;""",(name,)
    #    )
    #    print(f"Deleted")
    
        

 
except Exception as _ex: 
    print("[INFO] Error while working with PostgreSQL", _ex) 
finally: 
    if connection==True:  
        connection.close() 
        print("[INFO] PostgreSQL connection closed")
        
        