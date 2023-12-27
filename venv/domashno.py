import sqlite3

from flask import Flask ,render_template
from models.Kola import Kola

    def __add_product(marka,model,godina):
        db_connection.execute(f"""INSERT INTO MODELS(MARKA,MODEL,GODINA)"
                              f"VALUES('{marka}','{model}','{int(godina)}')""")

        db_connection.commit()


app = Flask(__name__)
@app.route("/home")

def show_home_page():
    koli = list(db_connection.execute("""SELECT * FROM MODELS"""))
    koli_lista = [Kola(*x) for x in (db_connection.execute("""SELECT * FROM MODELS"""))]
    return render_template("domasno.html", kola = koli_lista)

if __name__ == "__main__":
    db_connection = sqlite3.connect("database/modeli.db", check_same_thread=False)
    try:
        db_connection.execute("""
            CREATE TABLE MODELS
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                MARKA TEXT NOT NULL,
                MODEL TEXT NOT NULL,
                 GODINA INT):
            """)
    except Exception as e:
        print(e)
    __add_product("VW","pasat",2010)
    __add_product("BMW","M3",2015)
    __add_product("AUDI","A3",2019)
    __add_product("MERCEDES","E200",2020)

    app.run()