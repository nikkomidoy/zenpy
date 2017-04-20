__author__ = 'facetoe'


class ZenpyException(Exception):
    """
    A ZenpyException is raised for internal errors
    """


class ZenpyCacheException(ZenpyException):
    """
    A ZenpyCacheException is raised for errors relating the the ZenpyCache
    """


class APIException(Exception):
    """
    An APIException is raised when the API rejects a query.
    """


class RecordNotFoundException(APIException):
    """
    A RecordNotFoundException is raised when the API cannot find a record
    """


class TooManyValuesException(APIException):
    """
    A TooManyValuesException is raised when too many values have been passed to an endpoint. 
    """
