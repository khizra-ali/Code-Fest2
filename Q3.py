'''MY LIBRARY
For this challenge you will work for the librarian who needs a computer program to help pupils
find out where books can be found in the library.
The library contains nine bookshelves labelled from A to I. Each bookshelf specializes in one
genre. For instance, bookshelf A is for comedy fiction books.'''

def FicBook(Genre):
    if Genre == "Comedy".lower():
        print("Shelf A")
    elif Genre =="Graphic Novel".lower():
        print("Shelf B")
    elif Genre == "Science Fiction ".lower():
        print("shelf C")
    else:
        print("Not Avaiiable" )

def NonFicBook(Genre):
    if Genre == "History".lower():
            print("Shelf D")
    elif Genre =="Arts".lower():
            print("Shelf E")
    elif Genre == "Science ".lower():
            print("shelf F")
    else:
        print("Not Avaiable" )

choice=input("Fiction or Non-fiction: ")
if choice == "fiction".lower():
    Gen = input("Enter Genre: ")
    FicBook(Gen)
    #print(FicBook(Gen))
elif choice == "Non-fiction".lower():
    Gen = input("Enter Genre: ")
    NonFicBook(Gen) #or print(NonFicBook(Gen))
else:
    print("Not Avaiable")