import polars as pl
from typing import *
import json


def create_connection(config_file : str) -> str :
    '''
    Function for creating a connection url for DB

    '''
    creds = json.load(open(config_file))
    if creds['type'].lower() == "mysql":
        return f"mysql://{creds['user']}:{creds['password']}@{creds['url']}:{creds['port']}/{creds['database']}"
    else:
        raise Exception("Sorry this connection type is not supported")