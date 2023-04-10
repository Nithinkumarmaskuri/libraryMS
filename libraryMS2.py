class library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
        
    def displayAvailableBooks(self):
        print("books present in the library are:")
        for book in self.books:
            print(" * ", book)
            
            
    def lendBook(self,bookName):
        if bookName in self.books:
            print("the book has been taken{bookName}.keep it safe and return in 15 days ")
            self.books.remove(bookName)
            return True
        
        else:
            print("sorry ,this book is not available \n")
            print("has been already taken by someone else\n")
            print("please wait until the book is available!\n")
            
            
            
            
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("thanks for returning the book!\n")
        print("hope you read and enjoyed the book\n")
        
        
class Student: 
    def requestBook(self):
        self.book=input("enter the name of the book you want lend:")
        return self.book
    
    
    def returnBook(self):
        self.book=input("enter the book name that you want return:")
        return self.book 
                          
if __name__=="__main__" :
    centralLibrary=library(["javascript","python","c","c++","html","css","ml&ai"])
    student =Student()
    while(True):
        welcomeMsg = '''\n=== welcome to nithin library system===
        please select an option:
        1.display all the books
        2.request a book
        3.return a book
        4.exit 
        '''
        
        print(welcomeMsg)
        a=int(input("enter a option:"))
        
        if a==1:
            centralLibrary.displayAvailableBooks()
            
        elif a==2:
            centralLibrary.lendBook(student.requestBook())
            
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
            
        elif a==4:
            print("thanks for coming:")
            
        else:
            print("invalid option !")              