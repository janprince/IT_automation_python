import requests
import socket


# To check whether the localhost is correctly configured, we use the socket module
def check_localhost():
    localhost = socket.gethostbyname("localhost")
    return localhost == "127.0.0.1"


def check_connectivity():
    """
    This function checks if our computer can make successful calls to the internet.
    """
    conn = requests.get("http://www.google.com")
    return conn.status_code == 200
