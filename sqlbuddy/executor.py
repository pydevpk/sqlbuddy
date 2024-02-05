import sqlite3


class SQLite3Executor:
    def __init__(self, sql, connection_str):
        self.sql = sql
        self.connection_str = connection_str

    def _execute_sql(self):
        try:
            conn = sqlite3.connect(self.connection_str)  # create a memory database for testing
            cursor = conn.cursor()
            cursor.execute(self.sql)
            if 'INSERT' in self.sql or 'UPDATE' in self.sql or 'DELETE' in self.sql:
                conn.commit()
                print('SQL executed successfully')
            else:
                return cursor.fetchall()
        except sqlite3.InterfaceError:
            raise sqlite3.InterfaceError
        except sqlite3.DatabaseError:
            raise sqlite3.DatabaseError
        except sqlite3.Error as e:
            raise sqlite3.Error(f"An error occurred: {e}")
        finally:
            conn.close()


class MySQLExecutor:
    def __init__(self, sql, connection_str):
        self.sql = sql
        self.connection_str = connection_str

    def _execute_sql(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                user='scott', 
                password='password',
                host='127.0.0.1',
                database='employees'
            )
            cursor = conn.cursor()
            cursor.execute(self.sql)
            if 'INSERT' in self.sql or 'UPDATE' in self.sql or 'DELETE' in self.sql:
                conn.commit()
                print('SQL executed successfully')
            else:
                return cursor.fetchall()
        except mysql.connector.InterfaceError:
            raise mysql.connector.InterfaceError("Failed to connect to MySQL server")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
        finally:
            conn.close()


class PostgreSQLExecutor:
    def __init__(self, sql, connection_str):
        self.sql = sql
        self.connection_str = connection_str

    def _execute_sql(self):
        import psycopg2
        try:
            conn = psycopg2.connect(self.connection_str)
            cursor = conn.cursor()
            cursor.execute(self.sql)
            if 'INSERT' in self.sql or 'UPDATE' in self.sql or 'DELETE' in self.sql:
                conn.commit()
                print('SQL executed successfully')
            else:
                return cursor.fetchall()
        except psycopg2.InterfaceError:
            raise psycopg2.InterfaceError("Failed to connect to PostgreSQL server")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
        finally:
            conn.close()

class SQLExecutor:
    def __init__(self, sql, engine, connection_str):
        self.sql = sql
        self.engine = engine
        self.connection_str = connection_str
        self.errors = False

    def validate(self):
        if not self.sql:
            self.errors = True
            print("Error: No SQL provided")
        else:
            self._execute_sql()

        return self.errors

    def _execute_sql(self):
        if self.engine == 'sqlite':
            executor = SQLite3Executor(self.sql, self.connection_str)
            return executor._execute_sql()
        elif self.engine == 'mysql':
            executor = MySQLExecutor(self.sql, self.connection_str)
            return executor._execute_sql()
        elif self.engine == 'postgres':
            executor = PostgreSQLExecutor(self.sql, self.connection_str)
            return executor._execute_sql()
        else:
            raise Exception("Error: Unsupported database engine")
    
if __name__ == "__main__":
    sql = "SELECT * FROM employees;"
    # create table query 
    # sql = "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, salary REAL, designation TEXT, location TEXT);"
    engine = "sqlite"
    connection_str = ":memory:"
    executor = SQLExecutor(sql, engine, connection_str)
    if not executor.validate():
        print("SQL executed successfully")
    else:
        print("Error executing SQL")