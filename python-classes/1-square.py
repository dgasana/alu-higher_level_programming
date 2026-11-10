#!/usr/bin/python3
"""Defines a class Square with a private size."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: the size of the square (no validation).
        """
        self.__size = size
