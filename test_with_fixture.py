from main import *
import pytest
import sqlite3


def test_one():
    test_string = ""
    assert lenString(test_string) == len(test_string)

def test_two():
    test_string = "xxx@ThinkPad460:~/projects/TestPytest$"
    assert lenString(test_string) == len(test_string)

def test_three():
    test_string = "        "
    assert lenString(test_string) == len(test_string)


def readFromFile():
    with open("text.txt") as f:
        row = f.readline()
        return row

@pytest.fixture()
def connectSqlite3():
    connect = sqlite3.connect("pytest.db")
    cursor = connect.cursor()
    yield  connect
    query = "DELETE FROM users"
    cursor.execute(query)
    connect.commit()
    connect.close()

def test_saveFile():
    save_string = "Hello from text.txt"
    StringInFile(save_string)
    check_str_file = readFromFile()
    assert check_str_file == save_string

def test_DataBase(connectSqlite3):
    cursor = connectSqlite3.cursor()
    query = "INSERT INTO users ( name ) VALUES ('Ivan')"
    cursor.execute(query)
    connectSqlite3.commit()

    cursor.execute("SELECT * FROM users WHERE name = 'Ivan'")
    result = cursor.fetchone()
    assert result == (9, 'Ivan')
