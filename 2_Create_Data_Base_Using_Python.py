import psycopg2 #importing the module



#Creating a connection with object name 'conn' to postgress database
conn = psycopg2.connect(dbname = "postgres", user="postgres", password ="Samurai31$", host ="localhost",port ="5433" ) #Object name is conn

# Creating a table we should create a cursor

cursor = conn.cursor() #This function helps us to create the cursor

#Executing the command line we should always use the triple quotes
cursor.execute('''create table employeess(Name Text, Emp_ID int, Age int);''')
print("Table Created Successfully")

#Commiting the database changes

conn.commit()

#Once committed close the connection

conn.close()










