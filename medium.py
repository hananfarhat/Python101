
Input = [-1,0,1,2,-1,-4]
Output=[]
for i in Input:
    for ii in Input:
        for iii in Input:
            if i+ii+iii==0:
                Output.append([i,ii,iii])
                
for i in Output:
    i.sort()

unique_items = set(tuple(x) for x in Output)
unique_items


# ex2
text = "Hello world, this is is is Python!"
words = text.split()
my_dict ={}

for i,j in enumerate(words):
    if j in my_dict:
        my_dict[j]=my_dict[j]+1
    else:
        my_dict[j]=1

my_dict

class Book:
    def __init__(self, title, author, year, is_checked_out=False):  # Constructor method
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out=is_checked_out
    def checkout(self):  # Method inside the class
        is_checked_out=True
    def return_Book(self):
        is_checked_out=False
    def str(self):
        return self.title+" by "+self.author+" (Checked out: "+str(self.is_checked_out)+")"

class Library:
    def __init__(self):  # Constructor method
        self.collection = []

    def add_book(self,Book):
        self.collection.append(Book)
    def list_books(self):
        for i in self.collection:
            print(i.title +" "+str(i.is_checked_out))
    def find_book(self,title):
        for i in self.collection:
            if i.title== title:
                return i.str()


b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.list_books()

b1.checkout()
lib.list_books()

found = lib.find_book("1984")
print(found)