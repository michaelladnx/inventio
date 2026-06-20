#Import
import sqlite3
import logging

#Class

class ItemsDB:
    def __init__(self, db_name="inventory.db"):
        try :
            self.conn = sqlite3.connect(db_name)
            self.create_table()
        except Exception as e:
            logging.error(f"[ERROR] Database connection failed : {e}")

    def create_table(self):
        try :
            local_cursor = self.conn.cursor()
            local_cursor.execute(
                "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, isbn TEXT, name TEXT, used BOOLEAN, author TEXT, category TEXT, purchase_price REAL, current_value REAL, storage_location TEXT, status TEXT, comment TEXT, added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            self.conn.commit()
            local_cursor.close()
            return True
        except Exception as e:
            logging.error(f"[ERROR] Table creation failed : {e}")
            return False

    def insert_item(self, item):
        try :
            columns = ', '.join(item.keys())
            placeholders = ', '.join(['?'] * len(item))
            sql = f"INSERT INTO items ({columns}) VALUES ({placeholders})"
            local_cursor = self.conn.cursor()
            local_cursor.execute(sql, tuple(item.values()))
            self.conn.commit()
            local_cursor.close()
            return True
        except Exception as e:
            logging.error(f"[ERROR] Item insertion failed : {e}")
            return False
        
    def fetch_all_items(self):
        try :
            local_cursor = self.conn.cursor()
            local_cursor.execute("SELECT * FROM items")
            results = local_cursor.fetchall()
            local_cursor.close()
            return results
        except Exception as e:
            logging.error(f"[ERROR] Fetching items failed : {e}")
            return []

    def close(self):
        try :
            self.conn.close()
        except Exception as e:
            logging.error(f"[ERROR] Close connection failed : {e}")

# --- TEST ---
if __name__ == "__main__":
    # Create an instance of ItemsDB
    db = ItemsDB("inventory.db")
    logging.info("Database and table created successfully.")