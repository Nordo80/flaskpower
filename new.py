import os
os.system("mysqldump -u newuser -ppassword flask > " os.path.dirname(os.path.abspath(__file__)) + "/flask.sql")
os.system("mysql -u b12f26d01aa967 -pb85dc090 heroku_b40d4a2594424bc -h eu-cdbr-west-01.cleardb.com < /home/aleksandr/flask.sql")
print(os.path.dirname(os.path.abspath(__file__)) + "/lala")
