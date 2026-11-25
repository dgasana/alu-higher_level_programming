#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of the available attributes and methods of obj."""
    return dir(obj)
