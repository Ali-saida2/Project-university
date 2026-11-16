import pyodbc

def get_connection():
    conniction_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=ALI-SAIDA;"
        "DATABASE=UniversityProject;"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conniction_string)

if __name__ == "__main__":
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT DB_NAME()")
            database_name = cursor.fetchone()[0]
            print("Connection successfull!")
            print("Database:",database_name)
    except pyodbc.Error as error:
        print("Connection Failed:")
        print(error)