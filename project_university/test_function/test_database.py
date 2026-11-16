from function.db_connection import get_connection

def test_project_exists():
    connection = get_connection()
    try:
        cursor=connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM dbo.Project WHERE ProjectName =?",("Unit Test",)
        )
        result = cursor.fetchone()
        assert result[0] >= 1
    finally:
        connection.close()

def test_all_students_exist():
    expected_student ={
        "Ali Alsaida",
        "Layal blal",
        "nour sobh",
        "ali almalla",
        "ali al ali"
    }
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT FullName FROM dbo.Student")
        actual_students = [row[0] for row in cursor.fetchall()]
        for student in expected_student:
            assert student in actual_students,f"Student not found :{student}"
    finally:
        connection.close()