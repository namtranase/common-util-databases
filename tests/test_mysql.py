import logging

import settings
from src.config.config import read_config_file
from src import mysql

def create_database():
    pass

def insert_data():
    pass

def remove_data():
    pass

def main():
    mysql = mysql.DB(config)
    create_database()
    insert_data()
    remove_data()

if __name__ == "__main__":
    main()