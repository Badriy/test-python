class Library:
    
     def __init__(self):    
        self.library = []
         
     def add_book(self, book_title, book_author, book_copies):
         book = {"title":book_title,"author":book_author,"copies":book_copies }
         self.library.append(book)
        
        
     
     def diplay_books(self):
         for i in self.library:
            print(i)
        
     def searh_book(self,book_title):
         for i in self.library :
             if (i["title"] == book_title):
                    print(i)
                
lb1 =  Library()
lb1.add_book("arabic","b",6)
lb1.add_book("english","c",6)
lb1.diplay_books()
lb1.searh_book("arabic")
