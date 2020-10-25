import logging

from src.utils import mysql
from src.config.config import read_config_file
from src import mysql
import settings

def create_database(mysql):
    pass

def insert_data(mysql):
    pass

def remove_data(mysql):
    pass

def main():
    config = read_config_file(settings.config_file)
    if config['debug']:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug('Start test mysql application with config: %s', config)
    
    mysql = mysql.DB(config)
    create_database(mysql)
    insert_data(mysql)
    remove_data(mysql)

if __name__ == "__main__":
    main()