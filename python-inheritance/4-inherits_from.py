#!/usr/bin/python3
"""Defines a function that checks for inherited class instances."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class, else False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
