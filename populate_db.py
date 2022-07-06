import sqlite3
# from utils import init_connectDB
#
# con = init_connectDB()
# cur = con.cursor()
#
# # CREATING TABLES
#
# create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, title text, description text, price float)"
# create_stores_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, title text)"
#
# cur.execute(create_users_table)
# cur.execute(create_items_table)
# cur.execute(create_stores_table)
#
# # INITIALIZING WITH DATA TESTS
# insert_users = [
#     "INSERT INTO users VALUES (NULL, 'robsu', '12345')",
#     "INSERT INTO users VALUES (NULL, 'ana', '12345')",
#     "INSERT INTO users VALUES (NULL, 'rita', '12345')",
#     "INSERT INTO users VALUES (NULL, 'paulo', '12345')",
#     "INSERT INTO users VALUES (NULL, 'bia', '12345')"
#     ]
#
# for u in insert_users:
#     cur.execute(u)
#
#
# insert_items = [
#     "INSERT INTO items VALUES (NULL, 'Lavadora Consul 9Kg', 'Magazine Luiza', 1499.00)",
#     "INSERT INTO items VALUES (NULL, 'Geladeira Continental', 'Casas Bahia', 3500.00)",
#     "INSERT INTO items VALUES (NULL, 'TV 32 pol Philco', 'Ricardo Electro', 2499.00)",
#     "INSERT INTO items VALUES (NULL, 'Ferro elétrico Decker', 'Magazine Luiza', 45.99)",
#     ]
#
# for i in insert_items:
#     cur.execute(i)
#
# con.commit()
# con.close()

