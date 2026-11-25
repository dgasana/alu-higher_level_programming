#!/usr/bin/python3
"""Defines a file appending function."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
