from flask import Flask, render_template, request
import pymssql

app = Flask(__name__)

def connect_to_sql_server():
    conn = pymssql.connect(
        server='ec2-3-92-194-19.compute-1.amazonaws.com',
        database='AdventureWorks2016',
        user='sa',
        password='SqlServer2024**'
    )
    return conn
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        # Conectar a la base de datos
        conn = connect_to_sql_server()
        cursor = conn.cursor(as_dict=True)
        consulta= f"SELECT firstname, MiddleName, lastname  FROM Person.Person WHERE firstname = %s"
        cursor.execute(consulta,nombre)
        users = cursor.fetchall()
        conn.close()
        return render_template('resultado.html', nombre=users)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
