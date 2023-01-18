from sqlalchemy import create_engine  #py -m pip install sqlalchemy
import pandas as pd

db_connection_str = 'mysql+pymysql://root:rpsconsulting@localhost/kpmg'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM employees', con=db_connection)
print(df)