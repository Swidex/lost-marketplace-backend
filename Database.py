from errno import errorcode
import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values, load_dotenv

config = dotenv_values(".env")
DB_NAME = config.get("MYSQL_DB")

class Database():

    def __init__(self):
        
        self.__con = mysql.connector.connect(
            user        = config.get("MYSQL_USR"),
            password    = config.get("MYSQL_PWD"),
            host        = config.get("MYSQL_URL"))
        self.__cursor = self.__con.cursor()

        TABLES = {}

        TABLES['items'] = (
            "CREATE TABLE `items` ("
            "  `id` int NOT NULL,"
            "  `name` varchar(50) NOT NULL,"
            "  `price` int NOT NULL,"
            "  PRIMARY KEY (`id`), KEY `name` (`name`))")

        # INIT DB AND TABLES
        try:
            self.__cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.__create_database(self.__cursor)
                print("Database {} created successfully.".format(DB_NAME))
                self.__con.database = DB_NAME
            else:
                print(err)
                exit(1)

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.__cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

        self.__cursor.close()
        self.__con.close()

    def __create_database(self, cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def close(self):
        self.con.close()

database = Database()