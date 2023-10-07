import polars as pl
from aux_functions import *

## To Do List 
# Set Up MySQL to SQL Server Migration

## Reading from MySQL
connection_uri = create_connection(config_file='connections.json')

# Testing out the connection from MySQL
query = "SELECT * FROM city"
df = pl.read_database(query=query, connection=connection_uri).lazy() #Read as Lazy DataFrame
df = df.with_columns((pl.col("Population")/100).alias("Test Pop")).filter(pl.col("Test Pop")>15000)
df.collect().write_database(table_name="city_test", if_exists='replace',connection_uri=connection_uri)