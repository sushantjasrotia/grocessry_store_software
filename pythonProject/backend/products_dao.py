from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

# def update_product(connection, product_id, new_name, new_price):
#     try:
#         cursor = connection.cursor()
#         query = "UPDATE products SET name = %s, price = %s WHERE product_id = %s"
#         cursor.execute(query, (new_name, new_price, product_id))
#         connection.commit()
#         return cursor.rowcount  # Return the number of rows affected
#     except Exception as e:
#         connection.rollback()  # Rollback the transaction if there is an error
#         print(f"An error occurred: {e}")
#         return None
#     finally:
#         cursor.close()

def update_product(connection, new_data):
    cursor = connection.cursor()
    query = ("UPDATE products SET name = %s, uom_id = %s, price_per_unit = %s WHERE product_id = %s")
    data = (new_data['new_name'], new_data['new_uom_id'], new_data['new_price_unit'], new_data['product_id'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.rowcount


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    # print(insert_new_product(connection, {
    #     'product_name': 'potatoes',
    #     'uom_id': '1',
    #     'price_per_unit': 10
    # }))

    new_data = {
        'new_name': 'apple',
        'new_uom_id': '1',
        'new_price_unit': '22',
        'product_id': '1',
    }
    print(update_product(connection, new_data))