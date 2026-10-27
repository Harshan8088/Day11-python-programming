# library book system

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True

    def issue(self):
        if self.available:
            self.available=False
            print("book issued")
        else:
            print("book not avaliable")

    def return_book(self):
        self.available=True
        print("book returned")


book=Book("python basics ","search creators")
book.issue()
book.issue()
book.return_book()