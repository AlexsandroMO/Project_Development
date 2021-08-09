import pandas as pd
import sqlite3


def read_sql_read(): #Information Tables Read
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM django_admin_log;
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

read_sql_read()

def read_sql_read2(): #Information Tables Read
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM django_content_type;
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

read_sql_read()