from typing import Sequence

__all__: Sequence[str] = ("CrescentException", "CommandNotFoundError")


class CrescentException(Exception):
    """Base Exception for all exceptions Crescent throws"""


class CommandNotFoundError(CrescentException):
    """Command was not registered locally"""


class AlreadyRegisteredError(CrescentException):
    """Command or exception catch function was already registered"""
