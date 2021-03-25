#!/usr/bin/env python3
"""Filtered logger module"""
import logging
import re
from typing import List


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
    log_message = message
    for field in fields:
        regex = field + f'[^{separator}]*'
        log_message = re.sub(regex, f"{field}={redaction}", log_message)
    return log_message
