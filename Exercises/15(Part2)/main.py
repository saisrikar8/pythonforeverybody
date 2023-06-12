import xml.etree.ElementTree as ET
import sqlite3
import time

startTime = time.time()

conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER
);
CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
''')
xmlFileName = input("Hi, enter XML file name: ")
if (len(xmlFileName) < 1):
    xmlFileName = "Library.xml"
tree = ET.fromstring(open(xmlFileName).read())
tracks = tree.findall('.//dict/dict/dict')
for track in tracks:
    index = 0
    name = str()
    album = str()
    artist = str()
    genre = str()
    while (index < len(track)):
        tag = track[index]
        if (tag.tag == 'key'):
            newTag = track[index + 1]
            if (tag.text == 'Name'):
                name = newTag.text
            elif(tag.text =='Artist'):
                artist = newTag.text
            elif(tag.text == 'Album'):
                album = newTag.text
            elif(tag.text == 'Genre'):
                genre = newTag.text
        index += 2
    if (cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,)).fetchone() is None):
        cur.execute("INSERT INTO Artist (name) VALUES (?)", (artist,))
    artist_id = cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,)).fetchone()[0]
    if (cur.execute('SELECT id FROM Album WHERE title = ?', (album,)).fetchone() is None):
        cur.execute('INSERT INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    album_id = cur.execute('SELECT id FROM Album WHERE title = ?', (album,)).fetchone()[0]
    if (cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,)).fetchone() is None):
        cur.execute('INSERT INTO Genre (name) VALUES (?)', (genre,))
    genre_id = cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,)).fetchone()[0]
    if (cur.execute('SELECT id FROM Track WHERE title = ?', (name,)).fetchone() is None):
        cur.execute('INSERT INTO Track (title, album_id, genre_id) VALUES (?, ?, ?)', (name, album_id, genre_id))
    conn.commit()

    