

class Credentials:
    FACEBOOK = {'ACCESS_TOKEN' : ""}

class DatabaseConfig:
    mssql = {'host': 'dbhost',
         'user': 'dbuser',
         'passwd': 'dbPwd',
         'db': 'db'}

    postgresql = {'host': '0.0.0.0',
         'user': 'postgres',
         'passwd': 'magical_password',
         'db': 'db'}


    mssqlConfig = "mssql+pyodbc://{}:{}@{}:1433/{}?driver=SQL+Server+Native+Client+10.0".format(mssql['user'], mssql['passwd'], mssql['host'], mssql['db'])
    postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])


