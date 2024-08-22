class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages!"
    
    def __len__(self):
        return self.pages
    
    def __del__(self): #deletar objeto
        print("A book object has been deleted")


b = Book("Existir","Rayara Figueiredo",200)
print(b)
del b
