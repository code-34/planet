 c xampp/ apache/ conf/httpd.conf

AddHandler cgi-script .py
ScriptInterpreterSource Registry-Strict

 On the bottom of file


 Find <IfModule dir_module>
  and add index.py  default.py home.py


  pip install flask_mysqldb
  pip install mysql-connector-python