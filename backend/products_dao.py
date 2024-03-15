import sql_connection as sql

def get_all_products(connection):
    cursor = connection.cursor()

    query = """SELECT product_id, name, uom_name, price_per_unit from grocery_store.products 
            INNER JOIN grocery_store.uom ON grocery_store.uom.uom_id = grocery_store.products.uom_id;"""

    cursor.execute(query)
    ans = []
    for (product_id, name, uom_name, price_per_unit) in cursor.fetchall():
        ans.append({
            "product_id": product_id,
            "name": name,
            "uom_name": uom_name,
            "price_per_unit": price_per_unit
        })


    connection.close()
    return ans

if __name__ == "__main__":
    connection = sql.get_sql_connection()
    print(get_all_products(connection))