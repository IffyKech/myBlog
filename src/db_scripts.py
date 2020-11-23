import sqlite3


class Database:
    def __init__(self, name):
        self.name = name
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        self.connection_established = True

    def close(self):
        if self.connection_established:
            self.connection.close()
            self.connection_established = False
        else:
            raise ConnectionError

    def execute_query(self, query):
        if self.connection_established:
            try:
                self.cursor.execute(query)
                self.connection.commit()
            except Exception:
                raise Exception
        else:
            raise ConnectionError


def create_blog_database():
    """
    Create the blog's database, if it does not already exist.
    :return:
    """
    database = Database("blog.sqlite3")

    create_users_query = """CREATE TABLE userInfo(userid INTEGER PRIMARY KEY, username TEXT, userpassword TEXT, 
    userpic TEXT) """
    create_tag_query = """CREATE TABLE tag(tagid INTEGER PRIMARY KEY, tag TEXT)"""
    create_post_query = """CREATE TABLE postInfo(postid INTEGER PRIMARY KEY, tagid INTEGER, postcontent TEXT,
     title TEXT, postdate TEXT, FOREIGN KEY(tagid) REFERENCES tag(tagid))"""
    create_commentinfo_query = """CREATE TABLE commentInfo(commentid INTEGER PRIMARY KEY, commentcontent TEXT, 
    commentdate TEXT) """
    create_userpost_query = """CREATE TABLE userPosts(userid INTEGER, postid INTEGER,
     FOREIGN KEY(userid) REFERENCES userInfo(userid), FOREIGN KEY(postid) REFERENCES postInfo(postid),
     PRIMARY KEY(userid, postid))"""
    create_comment_query = """CREATE TABLE comment(commentid INTEGER, postid INTEGER, userid INTEGER, 
    FOREIGN KEY(commentid) REFERENCES commentInfo(commentid), FOREIGN KEY(postid) REFERENCES postInfo(postid),
     FOREIGN KEY(userid) REFERENCES userInfo(userid), PRIMARY KEY(postid, userid))"""

    queries = (create_users_query, create_tag_query, create_post_query, create_commentinfo_query,
               create_userpost_query, create_comment_query)
    for query in queries:
        database.execute_query(query)

    database.close()

def main():
    create_blog_database()
    print("Database Created")


if __name__ == "__main__":
    main()
