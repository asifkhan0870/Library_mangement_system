
import random

class Library:


    #constructor

    def __init__(self,ListOfBooks) -> None:
        
        self.booksList=ListOfBooks

        print("\n")


        print("***Some Important Instructions***\n")

        print("1.You can issued any books which is availble \n")
        print("2.prerquesites of being issued you need to be student of this collage")
        print("3.you will have to return that book within 30days, after late you have been charge 5rs per days and calculation will be done by this method how much extra days you have been keeped that book")

        print("4.whenever you have been issued any book will be given a token that should important at the time of return you have to tell that number to the librarian")


    #function for printing avalible books

    def Availability_of_books(self):

        print("Thanks for reading the books of this library\n")

        print("******These are all the present books at this time*****")
        print("\n")
        i=1
        for book in self.booksList:
            print(f"   {i}. "+book)  
            i+=1

        print("\n")    


    # control of issued of books     

    def issued_of_books(self,bookName):

        tokenNumber=random.randint(1,1000)
        
        if bookName in self.booksList:
            print("Your books has been issued!")
            print(f"your token number is: {tokenNumber}")

            self.booksList.remove(bookName)

        else:
            print(f"Sorry!, {bookName} has already issued it will be availble we will be consern or you can check next days or after some days when it will be return")


# control the system of returning the books

    def returning_of_books(self,bookName):
        self.booksList.append(bookName)

        print("Thanks! , for returing safely and on time")




        






    

  


class Student:
    pass





if  __name__=='__main__':
    
    lib=Library(["DSA","DLS","SAS","Software Engineering","Computer Organization"])

    lib.Availability_of_books()

    lib.issued_of_books("DLS")
    lib.issued_of_books("SAS")
    lib.returning_of_books("DLS")
    lib.issued_of_books("DLS")


    