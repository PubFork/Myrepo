WSIP = '127.0.0.1'
WSPORT = 8080

USERNAME = 'root'
PASSWD  = '123456'
DBIP = '192.168.0.88'
DBPORT = 3306
DBNAME = 'blog'
PARAMS = 'charset=utf8mb4'
URL = 'mysql+pymysql://{}:{}@{}:{}/{}?{}'.format(USERNAME,PASSWD,DBIP,DBPORT,DBNAME,PARAMS)
DATABASE_DEBUG = True

AUTHORIZE_SECRET= "yuhelg@yhl.com"
EXPIRED = 8*60*60