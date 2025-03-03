import psycopg2 # To import the module

#Calling the object name as conn

conn = psycopg2.connect(dbname="postgres", user = "postgres", password ="Samurai31$", host = 'localhost', port ='5433')

cursor = conn.cursor #Creating the CURSOR blinking vertical line

cursor.execute('''create table employees(name Text, ID int, age int);''') #Passing the command line in between 3 quotes - once we created table we need to commit
print("Table Created Successfully")



conn.commit() #To commit the changes

conn.close() # We need to colse the connection
















