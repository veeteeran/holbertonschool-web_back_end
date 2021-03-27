#!/usr/bin/env python3
"""Filtered logger module"""
import logging
import re
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
        filter_datm returns the log message obfuscated

            Parameters:
                    fields: a list of strings, the fields to obfuscate
                    redaction: a string representing obfuscated data
                    message: a string representing the log line
                    separator: a string representing which character
                               separates fields in the log line (message)
    """
    for field in fields:
        regex = field + f'[^{separator}]*'
        message = re.sub(regex, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    # Create logger
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # Add RedactingFormatter to ch
    ch.setFormatter(RedactingFormatter)
    # Add ch to logger
    logger.addHandler(ch)

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
        '''Filter values in incoming log records'''
        message = super().format(record)
        log_message = filter_datum(self.fields, self.REDACTION, message,
                                   self.SEPARATOR)
        return log_message
