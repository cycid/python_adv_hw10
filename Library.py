


class Library:


    def __init__(self, storage, name):

        self.name=name
        self.storage=storage



    def __repr__(self):
        return f'{self.name}'


    def add_book(self, book):
        self.storage.add_book(book)
        return print('book was added successful')

    def add_reader(self, reader):
        return self.storage.add_reader(reader)

    def show_all_readers(self):
        return self.storage.show_all_readers()


    def del_book(self, book):
        return self.storage.del_book(book)





    def give_book_to_reader(self, book_id, reader_id):

        """
        the function change the status lib to status with reader
        status lib means the book is in library
        :param book: book object
        :param reader: reader object
        :return: message with operation
        """

        if self.storage.get_status(book_id)==None and self.storage.update_status(book_id,reader_id)==True:
            return True
        else:
            return print(f'some one already took this book or you enter incorrect data')



    def get_book_from_reader(self,book):
        """
        the func return book from any reader who had it

        """

        self.storage.update_status(book,None)
        return True

    def print_books(self,param):

        """the function return books in library depends on parameter

        :param param: could be "all", "in" mean in library, and "out" mean out of library
        :return:
        """
        return self.storage.get_all_books(param)





    def sort(self,param):
        sorted_list=self.storage.get_sorted_list(param)
        for i in sorted_list:
            print(i)
        return


    def show_user_book(self,user):
        values=self.storage.show_user_books(user)
        for i in values:
            print(i)
        return