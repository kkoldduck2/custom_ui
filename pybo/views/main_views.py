from flask import Blueprint, url_for
from werkzeug.utils import redirect
import pyodbc
import os

bp = Blueprint('main', __name__, url_prefix='/')

# DSN = os.environ['DSN']
# UID = os.environ['DB_UID']
# PWD = os.environ['DB_PWD']

# conn_str = f"DSN={DSN};UID={UID};PWD={PWD}"

@bp.route('/hello/')
def hello_pybo():
    return "hello"
#     db = pyodbc.connect(conn_str)
#     db.setdecoding(pyodbc.SQL_CHAR,encoding='utf-8');
#     db.setdecoding(pyodbc.SQL_WCHAR,encoding='utf-8');
#     db.setdecoding(pyodbc.SQL_WMETADATA,encoding='utf-32le');
#     db.setencoding(encoding='utf-8')
#     cursor = db.cursor()

#     SQL_QUERY = """
#     SELECT * from emp
#     ;
#     """ 
#     cursor.execute(SQL_QUERY)
#     data = cursor.fetchall();

#     answer = 'a'
#     for x in data:
#         answer = x[0]
#     cursor.close()
#     db.close()

#     return answer 