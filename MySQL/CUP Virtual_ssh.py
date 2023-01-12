import pandas as pd
import logging as log
import sshtunnel

from sshtunnel import SSHTunnelForwarder

ssh_host = '198.154.236.235' #CUP_Virtual
ssh_username = 'root'
ssh_password = 'Miercoles-17!'
localhost = '127.0.0.1'

#-------------------------------------------------------------------
def open_ssh_tunnel(verbose=True):
    """Open an SSH tunnel and connect using a username and password.
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """
    
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = log.DEBUG
    
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username = ssh_username,
        ssh_password = ssh_password,
        remote_bind_address = (localhost, 3307)
    )
    
    tunnel.start()


#-------------------------------------------------------------------
def close_ssh_tunnel():
    """Closes the SSH tunnel connection."""
    
    tunnel.close

#-------------------------------------------------------------------
open_ssh_tunnel()
close_ssh_tunnel()




