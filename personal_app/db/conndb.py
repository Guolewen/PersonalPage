import sqlalchemy
import os
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
#db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

def connect2db():
    if os.environ.get('GAE_ENV') == 'standard':

        cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")
        db = sqlalchemy.create_engine(f'mysql+pymysql://{db_user}:{db_password}@/{db_name}?unix_socket=/cloudsql/'
                                      f'{cloud_sql_connection_name}/personal',
                                      pool_size=5,
                                      pool_timeout=30,
                                      pool_recycle=1800)
    else:
        db = sqlalchemy.create_engine(f'mysql+pymysql://root:Guolewen1234@35.241.95.147/personal')
    return db
