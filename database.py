
import sqlite3

DB_NAME = "students.db"


def connect():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age > 0),
                course TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)


def add_student(student_id, name, age, course, email):
    with connect() as conn:
        conn.execute(
            """INSERT INTO students
            (student_id, name, age, course, email)
            VALUES (?, ?, ?, ?, ?)""",
            (student_id, name, age, course, email)
        )


def get_students():
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM students ORDER BY name"
        ).fetchall()


def find_student(student_id):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM students WHERE student_id = ?",
            (student_id,)
        ).fetchone()


def update_student(student_id, name, age, course, email):
    with connect() as conn:
        cursor = conn.execute(
            """UPDATE students
            SET name = ?, age = ?, course = ?, email = ?
            WHERE student_id = ?""",
            (name, age, course, email, student_id)
        )
        return cursor.rowcount > 0


def delete_student(student_id):
    with connect() as conn:
        cursor = conn.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )
        return cursor.rowcount > 0

import sqlite3

DB_NAME = "students.db"


def connect():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age > 0),
                course TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)


def add_student(student_id, name, age, course, email):
    with connect() as conn:
        conn.execute(
            """INSERT INTO students
            (student_id, name, age, course, email)
            VALUES (?, ?, ?, ?, ?)""",
            (student_id, name, age, course, email)
        )


def get_students():
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM students ORDER BY name"
        ).fetchall()


def find_student(student_id):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM students WHERE student_id = ?",
            (student_id,)
        ).fetchone()


def update_student(student_id, name, age, course, email):
    with connect() as conn:
        cursor = conn.execute(
            """UPDATE students
            SET name = ?, age = ?, course = ?, email = ?
            WHERE student_id = ?""",
            (name, age, course, email, student_id)
        )
        return cursor.rowcount > 0


def delete_student(student_id):
    with connect() as conn:
        cursor = conn.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )
        return cursor.rowcount > 0
