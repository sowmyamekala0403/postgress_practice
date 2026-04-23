import psycopg2
from psycopg2 import extras

hostname = "<Hostname>"
pwd = "admin"
port_id = 1234
username = "sowmya"
dbname = "users"

conn = None
cur = None

try:
    # connection creation
    conn = psycopg2.connect(
        host=hostname,
        dbname=dbname,
        user=username,
        password=pwd,
        port=port_id
    )

    # cursor creation
    cur = conn.cursor(cursor_factory=extras.DictCursor)

    # DROP TABLE
    cur.execute("DROP TABLE IF EXISTS employee")

    # CREATE TABLE
    create_script = '''
    CREATE TABLE IF NOT EXISTS employee (
        id INT PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        salary INT,
        dept_id VARCHAR(20)
    )
    '''
    cur.execute(create_script)

    # INSERT DATA
    insert_script = '''
    INSERT INTO employee (id, name, salary, dept_id)
    VALUES (%s, %s, %s, %s)
    '''
    insert_values = [
        (1, "sowmya", 10000, "HR"),
        (2, "ram", 15000, "IT"),
        (3, "krishna", 20000, "FIN")
    ]

    for record in insert_values:
        cur.execute(insert_script, record)

    # UPDATE
    update_script = '''
    UPDATE employee
    SET salary = salary * 10 + salary
    WHERE id = 1
    '''
    cur.execute(update_script)

    # DELETE
    delete_script = '''
    DELETE FROM employee
    WHERE name = %s
    '''
    cur.execute(delete_script, ("sowmya",))

    # SELECT query
    cur.execute("SELECT * FROM employee")

    # fetch all rows
    rows = cur.fetchall()

    # print data
    for row in rows:
        print(row["id"], row["name"], row["salary"], row["dept_id"])


    # commit changes
    conn.commit()

except Exception as e:
    print("Exception raised:", e)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
