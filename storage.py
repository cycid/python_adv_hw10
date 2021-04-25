from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import Session
from book import Book
from reader import Reader
from sqlalchemy.ext.declarative import declarative_base
from base_class_sql import Base





class Database:
    def __init__(self, db_type, username, password, adress, port, name):
        self.engine = create_engine(f'{db_type}://{username}:{password}@'
                                    f'{adress}:{port}/{name}')
        print(self.engine)

        Base.metadata.drop_all(self.engine)
        print(Base.metadata.create_all(self.engine))
        self.session = Session(self.engine)

    def add_book(self, book):
        self.session.execute("INSERT INTO books VALUES (:id ,:title, :author, :year, :status)",
                                 {"id":book.id, "title":book.title, "author":book.author, 'year':book.year, "status":book.status})
        try:
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return False

    def show_all_readers(self):
        return self.session.execute("SELECT * FROM readers").fetchall()

    def add_reader(self, reader):
        self.session.execute('INSERT INTO readers VALUES (:id, :name, :password)',
                             {'id':reader.id, 'name':reader.name, 'password':reader.password})
        try:
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return False

    def del_book(self,book_id):
        try:
            self.session.execute("DELETE FROM books WHERE id = :id", {"id":book_id})
            return True
        except:
            return False
    def get_status(self,book_id):
        val=self.session.execute("SELECT * FROM books WHERE id= :id", {'id':book_id}).fetchone()
        return val.status

    def update_status(self, book_id, reader_id):
        self.session.execute("UPDATE books SET status=:status WHERE id=:id",{"status":reader_id, "id":book_id})
        try:
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return False

    def get_all_books(self, param):
        if param=="all":
            return self.session.execute('SELECT * FROM books').all()
        elif param=="in":
            return self.session.execute('SELECT * FROM books WHERE status is NULL').fetchall()
        else:
            return self.session.execute('SELECT * FROM books where status IS NOT NULL').fetchall()

    def get_sorted_list(self, param):
        if param=="year":
            return self.session.execute("SELECT*FROM books ORDER BY year").fetchall()
        elif param=="title":
            return self.session.execute("SELECT*FROM books ORDER BY title").fetchall()
        else:
            return self.session.execute("SELECT*FROM books ORDER BY author").fetchall()



    def show_user_books(self, user):
        return self.session.execute("SELECT*FROM books WHERE status=:user_id", {'user_id':user.id}).fetchall()



