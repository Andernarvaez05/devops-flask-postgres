from flask import Flask
import psycopg2
 
app = Flask(__name__)
VERSION = "2.0.0"
 
@app.route("/")
def inicio():
    try:
        conexion = psycopg2.connect(
            host="db", database="empresa",
            user="admin", password="admin123"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        cursor.execute("SELECT id, nombre FROM clientes;")
        clientes = cursor.fetchall()
        cursor.close()
        conexion.close()
        filas = "".join(
            f"<tr><td>{c[0]}</td><td>{c[1]}</td></tr>"
            for c in clientes
        )
        return f'''
        <h1>Flask v{VERSION}</h1>
        <p>PostgreSQL: {version[0]}</p>
        <h2>Clientes registrados</h2>
        <table border="1">
          <tr><th>ID</th><th>Nombre</th></tr>
          {filas}
        </table>
        '''
    except Exception as e:
        return str(e)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
