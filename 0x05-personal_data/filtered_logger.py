#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    :param fields:
    :param redaction:
    :param message:
    :param separator:
    :return: log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f"{field}={redaction}{separator}",
                         message)
    return message


def get_logger() -> logging.Logger:
    """
    :return: function that takes no arguments and returns a
    logging.Logger object
    """
    logger = logging.getLogger("user_data")  # logger name is "user_data"
    logger.propagate = False  # not propagate messages to other loggers
    logger.setLevel(logging.INFO)  # handle only INFO level
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns a connector to the database """
    return mysql.connector.connect(
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum
        :param record:
        :return:
        """
        return filter_datum(self.fields, self.REDACTION,
                            logging.Formatter(self.FORMAT).format(record),
                            self.SEPARATOR)


def main():
    """
    retrieve all rows in the users table and display
     each row under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    userFound = cursor.fetchall()
    log = get_logger()
    for user in userFound:
        record = f"name={user[0]}; email={user[1]}; phone={user[2]};\
         ssn={user[3]}; password={user[4]}; ip={user[5]};\
         last_login={user[6]}; user_agent={user[7]};"
        log.info(record)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
