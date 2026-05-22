from sqlalchemy import create_engine
import pandas as pd

host = 'localhost' 
user = 'root'
password = ''
database = 'bd_mod2_aula04'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)
query = 'select produto, marca from cadastro_produtos'
df_produtos = pd.read_sql(query, engine)
print(df_produtos)