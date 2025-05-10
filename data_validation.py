from urllib import error, request
from urllib.request import urlopen


from validators import url


def address_validation(site_address: str)->bool:
    """
    Func checks if collected string is url
    :param site_address: url provided by client
    :return: true if parameter site_address is string and url, false otherwise
    """

    try:
        if isinstance(site_address, str):
            return url(site_address)
    except error.URLError:
        raise error.URLError("URL is not correct")
    except ValueError:
        raise ValueError("Entered value is wrong")


def address_status_check(site_address: str)-> property:
    """
    Func returns connection to http/s server code in case and url is valid
    :param site_address: url provided by client
    :return: code of succeed/failed connection to http/s server
    """

    try:
        if address_validation(site_address):
            response = urlopen(site_address)
            return response.getcode()
    except error.HTTPError:
        raise error.HTTPError("Can't connect to the website")

