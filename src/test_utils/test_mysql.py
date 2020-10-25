import logging

from src.utils import mysql
from src.config.config import read_config_file
import settings

def create_database(mysql_db):
    pass

def insert_data(mysql_db):
    pass

def remove_data(mysql_db):
    pass

def main():
    config = read_config_file(settings.config_file)
    if config['debug']:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug('Start test mysql application with config: %s', config)
    
    mysql_db = mysql.DB(config)
    create_database(mysql_db)
    insert_data(mysql_db)
    remove_data(mysql_db)

if __name__ == "__main__":
    main()