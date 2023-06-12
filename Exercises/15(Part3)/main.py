import sqlite3, json

conn=sqlite3.connect("courses.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS User;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

JSON = json.loads(open("roster_data.json").read())

for row in JSON:
    user = row[0]
    course = row[1]
    role = row[2]
    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (user,))
    user_id = cur.execute("SELECT id FROM User WHERE name = ?", (user,)).fetchone()[0]
    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES(?)", (course,))
    course_id = cur.execute("SELECT id FROM Course WHERE title = ?", (course,)).fetchone()[0]
    cur.execute("INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?,?,?)", (user_id, course_id, role))
    conn.commit()