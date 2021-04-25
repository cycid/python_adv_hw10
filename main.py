

import Library, book, reader,  storage
from storage import Database

msg="choose option:\n" \
              "1:show all books\n" \
              "2:show books in library\n" \
              "3:show books out of library\n" \
              "4:add book\n" \
              "5:del book\n" \
              "6:give book to reader\n" \
              "7:take book from reader\n" \
              "8:sort books base on author\n" \
              "9:sort books base on title\n" \
               "10:add reader\n" \
               "11:show all readers\n" \
              "0:Close program"

def user_in():
    while True:
        choice_client=int(input(msg))
        if choice_client==1:
            items=library.print_books("all")
            for i in items:
                print(i)
        elif choice_client==2:
            answer=library.print_books("in")
            for i in answer:
                print(i)
        elif choice_client==3:
            answer=library.print_books("any")
            for i in answer:
                print(i)
        elif choice_client==4:
            answer="please enter book id"
            book_id=input(answer)
            answer="please enter book title"
            book_title=input(answer)
            answer = "please enter book author"
            book_author = input(answer)
            answer = "please enter book year"
            book_year = int(input(answer))
            new_book=book.Book(book_id,book_title,book_author,book_year)
            if library.add_book(new_book)==True:
                answer="book was added\n"
            else:
                answer="error check values and try again\n"

        elif choice_client==5:
            answer="please enter book id to delete"
            book_id=int(input(answer))
            library.del_book(book_id)
            answer="book deleted successfully\n"

        elif choice_client==6:
            answer="please enter book id to take it"
            book_id=int(input(answer))
            answer="please enter reader id to take it"
            reader_id = int(input(answer))
            if library.give_book_to_reader(book_id,reader_id)==True:
                answer="you take the book\n"

            else:
                answer = "error"

        elif choice_client==7:
            answer = "please enter book id to return it"
            book_id=int(input(answer))
            if library.get_book_from_reader(book_id)==True:
                answer="you return the book\n"
            else:
                answer = "error"
        elif choice_client==8:
            answer=library.sort("author")

        elif choice_client==9:
            answer=library.sort("name")
        elif choice_client==10:
            answer="input reader id"
            user_id=int(input(answer))
            answer = "input reader name"
            reader_name=input(answer)
            answer="input user pass"
            reader_pass=input(answer)
            readerr=reader.Reader(user_id,reader_name, reader_pass)
            if library.add_reader(readerr)==True:
                answer="reader was added successfully"
            else:
                answer="error"

        elif choice_client==11:
            readers=library.show_all_readers()
            if len(readers)==0:
                answer="no readers"
            else:
                for i in readers:
                    print(i)

        elif choice_client==0:
            print("out of program")
            return

        else:
            answer="enter coorect value"
        print(answer)







if __name__=="__main__":
    book1 = book.Book(1, "Hobbit", "Tolkien", 1976)
    a = Database("postgresql", "postgres", "12345", "localhost", '5432', 'homework10')

    library = Library.Library(a, "my_lib")
    user1=reader.Reader(1,"Petro", 12345)
    user2=reader.Reader(2, "Bran", 1235)
    library.add_book(book1)
    book3=book.Book(3,"12 Rules of Life","Jordan Peterson",2018)
    book2=book.Book(2,"Lord of the Rings", "Tolkien", 1960)

    #add book function(takes book obj as argument)
    library.add_book(book3)
    library.add_book(book2)


    user_in()



