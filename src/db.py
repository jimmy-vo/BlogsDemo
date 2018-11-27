import sqlite3


def init_db():
    db = sqlite3.connect('database.db')
    db.execute('DROP TABLE IF EXISTS Users;')
    db.execute('DROP TABLE IF EXISTS Posts;')
    db.execute('CREATE TABLE Users ('
               '  Id           INTEGER PRIMARY KEY AUTOINCREMENT,'
               '  UserName     TEXT UNIQUE NOT NULL,'
               '  Password     TEXT NOT NULL'
               ');')
    db.execute('CREATE TABLE Posts ('
               '  Id           INTEGER PRIMARY KEY AUTOINCREMENT,'
               '  Author       INTEGER NOT NULL,'
               '  Time         TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
               '  Title        TEXT NOT NULL,'
               '  Content         TEXT NOT NULL,'
               '  FOREIGN KEY (Author) REFERENCES Users (id)'
               ');')
    db.execute('INSERT INTO Users (UserName,Password) '
               'VALUES(?, ?)', ('root', 'root'))
    db.commit()
    db.execute('INSERT INTO Users (UserName,Password) '
               'VALUES(?, ?)', ('root1', 'root'))
    db.commit()
    db.execute('INSERT INTO Posts (Author,  Title, Content)'
               'VALUES(?, ?, ?)', ('0',  't1', 'c1'))
    db.commit()
    db.execute('INSERT INTO Posts (Author,  Title, Content)'
               'VALUES(?, ?, ?)', ('1',  't2', 'c2'))
    db.commit()
    db.execute('INSERT INTO Posts (Author,  Title, Content)'
               'VALUES(?, ?, ?)', ('1',  't3', 'c3'))
    db.commit()
    db.close()


def fetch_user_all():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    record = c.execute('SELECT Id, UserName, Password FROM Users').fetchall()
    db.close()
    return [dict(row) for row in record]


def fetch_user_id(username):
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    record = c.execute('SELECT Id, UserName, Password FROM Users '
                       'WHERE UserName = (?)', [(username)]).fetchall()
    db.close()
    return [dict(row) for row in record]


def create_user(username, password):
    db = sqlite3.connect('database.db')
    db.execute('INSERT INTO Users (UserName,Password) VALUES(?, ?)', (username, password))
    db.commit()
    db.close()


def fetch_blog_all(author):
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    record = c.execute(
        'SELECT p.Id, Title, Content, Time, Author, UserName'
        ' FROM  Posts p JOIN Users u ON p.Author = u.Id'
        ' WHERE p.Author = ?'
        ' ORDER BY Time DESC', str(author)
    ).fetchall()
    db.close()
    return [dict(row) for row in record]


def fetch_blog_single(id, author):
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    record = c.execute('SELECT p.Id, Title, Content, Time, Author, UserName'
                       ' FROM  Posts p JOIN Users u ON p.Author = u.Id'
                       ' WHERE p.Id = ? AND Author = ?'
                       ' ORDER BY Time DESC', (id, str(author))).fetchall()
    db.close()
    return [dict(row) for row in record]


def insert_blog_single(author,  title, content):
    db = sqlite3.connect('database.db')
    db.execute('INSERT INTO Posts (Author,  Title, Content)'
               'VALUES(?, ?, ?)', (author,  title, content))
    db.commit()
    db.close()


def update_blog_single(id, author,  title, content):
    db = sqlite3.connect('database.db')
    db.execute('UPDATE Posts SET Author = ?,  Title = ?, Content = ? WHERE Id = ?',
               (author,  title, content, id))
    db.commit()
    db.close()


def delete_blog_single(id):
    db = sqlite3.connect('database.db')
    db.execute('DELETE FROM Posts WHERE Id = ?', id)
    db.commit()
    db.close()
