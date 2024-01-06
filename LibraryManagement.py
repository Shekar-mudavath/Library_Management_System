class Library:

    def __init__(self, listOfBooks) :
        self.books  = listOfBooks

    def displayAvailableBooks(self) :
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book) 
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. please return it within 30 days")
            self.books.remove(bookName)
        else:
            print("Sorry, This book is either not available or has been issued to someone else, Please wait until it is available.")
    def returnBook(self, bookName):
        if bookName == '':
            print("Invalid Book Name")
        else:
            self.books.append(bookName)
            print("Thanks for returning this book!Hope you enjoyed reading")
        

                                  
class Student:
    def requestBook(self):
        self.book   = input("Enter the book you want to borrow: ")
        return self.book 
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        Welcome = '''\n=====Welcome to central Library=====
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit
        '''
        print(Welcome)

        a = int(input("Enter a choice : "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for using this library")
            exit()            
        else:
            print("Invalid!!")    
       





           



          






    


     