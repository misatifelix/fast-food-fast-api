import psycopg2
import os 
from .tables import queries, to_drop

#create a connection
def create_conn():
	conn = psycopg2.connect(os.getenv('DB_URL'))
	return conn


#Create Database tables
def create_db(): 
    conn = create_conn()
    curr = conn.cursor()
    for query in queries:
        curr.execute(query)

    curr.close()
    conn.commit()
    return conn

def drop_db():
    conn = create_conn()
    curr = conn.cursor()
    try: 
        for query in to_drop:
            curr.execute(query)

        curr.close()
        conn.commit()
    except:
        print("failed")
