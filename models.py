from os import path
import sqlite3 as sql
import datetime

# Get directory name then get rel path to it
#   for file we pass in
ROOT = path.dirname(path.relpath((__file__)))

# Will create post when request comes in
def create_post(name,content):
    # Connection to DB
    con = sql.connect(path.join(ROOT, 'database.db'))
    # Cursor will grab what we need instead of 
    #   whole database
    cur = con.cursor()
    # get time
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')


    # Insert row into name and content columns
    #   question marks will be replaced with name, content, time
    cur.execute('insert into posts (name, content, time) values(?,?,?)', (name,content,now))
    # Commit insert, then close
    con.commit()
    con.close()

# Get All Posts
def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    # Select all from posts(name of our table)
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

def delete_posts():
    print("delete_posts()")
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    # Delete all posts
    cur.execute('delete from posts')
    con.commit()
    con.close()
