import sqlite3


def create_database():
    database = sqlite3.connect("blog.sqlite3")
    database_cursor = database.cursor()

    create_users_query = """CREATE TABLE userInfo(userid INTEGER PRIMARY KEY, username TEXT, userpassword TEXT, userpic TEXT)"""
    database_cursor.execute(create_users_query)
    database.commit()

    create_tag_query = """CREATE TABLE tag(tagid INTEGER PRIMARY KEY, tag TEXT)"""
    database_cursor.execute(create_tag_query)
    database.commit()

    create_post_query = """CREATE TABLE postInfo(postid INTEGER PRIMARY KEY, tagid INTEGER, postcontent TEXT,
     title TEXT, postdate TEXT, FOREIGN KEY(tagid) REFERENCES tag(tagid))"""
    database_cursor.execute(create_post_query)
    database.commit()

    create_commentinfo_query = """CREATE TABLE commentInfo(commentid INTEGER PRIMARY KEY, commentcontent TEXT, commentdate TEXT)"""
    database_cursor.execute(create_commentinfo_query)
    database.commit()

    create_userpost_query = """CREATE TABLE userPosts(userid INTEGER, postid INTEGER,
     FOREIGN KEY(userid) REFERENCES userInfo(userid), FOREIGN KEY(postid) REFERENCES postInfo(postid),PRIMARY KEY(userid, postid))"""
    database_cursor.execute(create_userpost_query)
    database.commit()

    create_comment_query = """CREATE TABLE comment(commentid INTEGER, postid INTEGER, userid INTEGER, 
    FOREIGN KEY(commentid) REFERENCES commentInfo(commentid), FOREIGN KEY(postid) REFERENCES postInfo(postid),
     FOREIGN KEY(userid) REFERENCES userInfo(userid), PRIMARY KEY(postid, userid))"""
    database_cursor.execute(create_comment_query)
    database.commit()


def main():
    create_database()
    print("Database Created")


if __name__ == "__main__":
    main()
