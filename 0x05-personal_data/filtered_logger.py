#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re
import logging

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
