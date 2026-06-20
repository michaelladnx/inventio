#Import
import sqlite3

#Class

class ItemsDB:
    def __init__(self, db_name="inventory.db"):
        try :
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"[ERROR] Database connection failed : {e}")

    def create_table(self):
        try :
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, isbn TEXT, name TEXT, used BOOLEAN, author TEXT, category TEXT, purchase_price REAL, current_value REAL, storage_location TEXT, status TEXT, comment TEXT, added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"[ERROR] Table creation failed : {e}")
            return False

    def insert_item(self, item):
        try :
            columns = ', '.join(item.keys())
            placeholders = ', '.join(['?'] * len(item))
            sql = f"INSERT INTO items ({columns}) VALUES ({placeholders})"
            self.cursor.execute(sql, tuple(item.values()))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"[ERROR] Item insertion failed : {e}")
            return False
        
    def fetch_all_items(self):
        try :
            self.cursor.execute("SELECT * FROM items")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[ERROR] Fetching items failed : {e}")
            return []

    def close(self):
        try :
            self.conn.close()
        except sqlite3.Error as e:
            print(f"[ERROR] Close connection failed : {e}")

# --- TEST ---
if __name__ == "__main__":
    # Create an instance of ItemsDB
    db = ItemsDB()
    print("Database and table created successfully.")