from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="hotel"
    )
    return conn


@app.get("/")
def home():
    conn = get_connection()
    conn.close()
    return {"message": "Hotel Booking Successful"}


@app.post("/insert")
def insert_data(id:int, name:str, room:str, days:int):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        query = "INSERT INTO booking VALUES (%s,%s,%s,%s)"

        cursor.execute(query, (id, name, room, days))

        conn.commit()

        return {"message": "Booking inserted successfully"}

    except Exception as e:
        print(f"Error occurred: {e}")
        return {"message": "Error occurred"}

    finally:
        cursor.close()
        conn.close()


@app.get("/view")
def view_data():
    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM booking"

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"data": data}

@app.get("/")
def home():
    return {"message": "Hotel Booking Started"}