"""
Copyright 2020 ASE Laboratory.
@author namtran.ase

Implement python class for connect with mysql. 
Support connect, execute query and close when finish.
"""
import pymysql

class DB():
    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host=self.config['host'],
            port=self.config['port'],
            db=self.config['db'],
            user=self.config['user'],
            password=self.config['password'],
            charset=self.config['charset'])

    def execute(self, query, *args):
        if self.conn is None:
            self.connect()

        with self.conn.cursor() as cursor:
            nrows = cursor.execute(query, args)
            if nrows == 0:
                return []

            return cursor.fetchall()

    def close(self):
        if self.conn is not None:
            self.conn.close()

def create_table(db, table_name):
    """Returns status when create table.
    """
    query = ("CREATE TABLE {} (name VARCHAR(255), address VARCHAR(255))".format(table_name))

    return db.execute(query)

def check_table_exist(db, table_name):
    """Returns status if  table exist.
    """
    query_check = ("SELECT * FROM information_schema.tables" +
                   "  WHERE table_schema = 'test'")
    query_show = ("SHOW TABLES")
    return db.execute(query_show)