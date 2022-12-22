import psycopg2
import config
from PyQt5 import QtCore, QtGui, QtWidgets


from configparser import ConfigParser

def config(filename='D:\\education\\RBD\\RBD\\UI_RBD\\database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def Get_data_from_table(conn, cur, name_table, data = []):
    cur.execute('SELECT * from public.' + name_table)
    ans = cur.fetchall()
    return ans

def Insert_data_to_table(conn, cur, name_table, data):
    if name_table == 'management_company':
        print(data[1])
        str = f'INSERT INTO public.management_company ("ID_management_company", name) VALUES ({data[0]}, \'{data[1]}\');'
        cur.execute(str)
        conn.commit()
        ans = cur.fetchall()
        print(ans)
    if name_table == 'driver':
        str = f'INSERT INTO public.driver ("ID_driver", full_name, seniority, penalties, driver_license) VALUES({data[0]}, \'{data[1]}\', {data[2]}, {data[3]}, \'{data[4]}\');'
        cur.execute(str)
        conn.commit()
        ans = cur.fetchall()
        print(ans)



def connect(func, name_table, dt = []):
    """ Connect to the PostgreSQL database server """
    data = []
    conn = None
    try:
        # read connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()

        data = func(conn, cur, name_table, dt)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

    return data
