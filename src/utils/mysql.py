"""
Copyright 2020 ASE Laboratory.
@author namtran.ase

Implement python class for connect with mysql. 
Support connect, execute query and close when finish.
"""
import mysql

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
        if self.config is None:
            self.connect()

            with self.conn.cursor() as cursor:
                nrows = cursor.execute(query, args)
                if nrows == 0:
                    return None
                
                return cursor.fetchall()
    
    def close(self):
        if self.conn is not None:
            self.conn.close()