import psycopg2 #importing the module

def table():


    #Creating a connection with object name 'conn' to postgress database
    conn = psycopg2.connect(dbname = "postgres", user="postgres", password ="Samurai31$", host ="localhost",port ="5433" ) #Object name is conn

    # Creating a table we should create a cursor

    cursor = conn.cursor() #This function helps us to create the cursor

    #Executing the command line we should always use the triple quotes
    cursor.execute('''create table emp_2(Name Text, Emp_ID int, Age int);''')
    #print("Table Created Successfully")

    #Commiting the database changes

    conn.commit()

    #Once committed close the connection

    conn.close()

def data():

    
    conn = psycopg2.connect(dbname = "postgres", user="postgres", password ="Samurai31$", host ="localhost",port ="5433" ) #Object name is conn

   

    cursor = conn.cursor() 

    #User Input variables

    name = input("Enter Employee Name >> ")
    id = input("Enter Employee ID >><")
    age = input("Enter Employee Age >> ")
    query = '''insert into emp_2(Name, Emp_ID , Age ) values(%s, %s, %s);''' #PASSING DYNAMIC VALUES use %s inside the values FUNCTION

    #To execute the data under table
    cursor.execute(query, (name, id, age))
    print("Data Added Successfully")
    
    conn.commit()

    conn.close()

#table()
data()