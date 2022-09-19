import socket


def connectToInternet():
    try:
        socket.create_connection(
            ("www.google.com", 80)
        )  # better to set timeout as well
        return True
    except OSError:
        return False
