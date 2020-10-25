import logging

import settings
from src.config.config import read_config_file
from src.utils import mysql

def create_table(config, table_name):
    mysql_db = mysql.DB(config['mysql'])

    try:
        mysql.create_table(mysql_db, table_name)
        tables = mysql.check_table_exist(mysql_db, table_name)
    finally:
        mysql_db.close()
    logging.debug('Tables: %s', tables)

def insert_data(mysql_db):
    pass

def remove_data(mysql_db):
    pass

def main():
    config = read_config_file(settings.config_file)
    if config['debug']:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug('Start test mysql application with config: %s', config)
    
    table_name = 'test_table'

    # Create database
    create_table(config, table_name)

    insert_data(config)

    remove_data(config)

if __name__ == "__main__":
    main()