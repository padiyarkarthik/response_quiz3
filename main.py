from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

	
@app.route('/search', methods=['POST'])
def search():

    if conn:
        
        tic = time()
        count=1
        while(count<=1000):
            r = random.uniform(0.6, 6.0)
            sequel = "select * from edata where mag >= ?"
            # Note that for security reasons we are preparing the statement first,
            statement = ibm_db.prepare(conn, sequel)
            ibm_db.bind_param(statement, 1, r)
            ibm_db.execute(statement)
            # obtaining the results
            res = ibm_db.fetch_assoc(statement)
            count = count + 1
        toc = time()
        totalTime = toc - tic
        ibm_db.close(conn)
    return render_template('view2.html', rows=totalTime)



def main():
    database = "C:\\Users\Karthik Padiyar\Documents\laptop_hp\Documents\MS_CS_SUMMER_2018\Cloud Computing\assignment3\Assignment3"
 
    # create a database connection
    conn = create_connection(database)


if __name__ == '__main__':
    main()	
	
conn = sqlite3.connect('database.db')
# print("Opened database successfully")

# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print("Table created successfully")
# conn.close()


if __name__ == '__main__':
   app.run(debug = True)