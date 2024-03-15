import sql_connection as sql


def get_all_products(connection) -> list[dict]:
    cursor = connection.cursor()

    query = ("SELECT product_id, name, uom_name, price_per_unit "
             "FROM grocery_store.products"
             " INNER JOIN grocery_store.uom "
             "ON grocery_store.uom.uom_id = grocery_store.products.uom_id")

    cursor.execute(query)
    response = []
    for (product_id, name, uom_name, price_per_unit) in cursor.fetchall():
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_name": uom_name,
            "price_per_unit": price_per_unit
        })

    connection.close()
    return response


def insert_new_product(connection, product) -> int:
    cursor = connection.cursor()
    query = """INSERT INTO grocery_store.products
                (name, uom_id, price_per_unit)
                VALUES (%s, %s, %s)"""

    data = (product["product_name"], product["uom_id"], product["price_per_unit"])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id) -> None:
    cursor = connection.cursor()
    query = ("DELETE FROM grocery_store.products WHERE product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == "__main__":
    connection = sql.get_sql_connection()
    # print(get_all_products(connection))
    # print(insert_new_product(connection, {
    #     'product_name': 'cabbage',
    #     'uom_id': '2',
    #     'price_per_unit': '20'
    # }))
    print(delete_product(connection, 12))