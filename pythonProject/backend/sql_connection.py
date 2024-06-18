import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='Nokia?tl3',database='gs')

  return __cnx
#
# import mysql.connector
#
# cnx = mysql.connector.connect(user='root', password='Nokia?tl3',
#                               host='127.0.0.1',
#                               database='gs')
#
# # Create a cursor object
# cursor = cnx.cursor()
#
# # Define the query
# query = "SELECT * FROM products"  # Adjusted query assuming 'gs' is the database already selected
#
# # Execute the query
# cursor.execute(query)
#
# # Fetch and print the results
# for (product_id, name, uom_id, price_per_unit) in cursor:
#     print(product_id, name, uom_id, price_per_unit)
#
# # Properly close the cursor and connection
# cursor.close()
# cnx.close()


