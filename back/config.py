import os

__all__ = ['DATABASE_URI', 'SECRET_KEY', 'EXPIRATION_SEC']

# MySQL
mysql_host = os.getenv('MYSQL_HOST')
if mysql_host:
    DATABASE_URI = f'mysql://root:camrsti@{mysql_host}:3306/camrstidb'
else:
    DATABASE_URI = 'mysql://root:camrsti@127.0.0.1:3306/camrstidb'

# JWT
SECRET_KEY = "jjjyeerffdfsaewrtyufx9hZCJ9.4twFt5NiznN84AWoo1dzz"
EXPIRATION_SEC = 24 * 60 * 60   # 24h

