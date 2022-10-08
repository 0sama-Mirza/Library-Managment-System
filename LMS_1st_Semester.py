from datetime import*
book_issue={}
x=datetime.now()

def add_books(book_name):
    a = book_name in books
    if a == True:
        print("Book already present.")
        books[book_name][4] += 1
    else:
        append_list = [1,2,3,4,5]            # temporary list made to append values after assigning them in lists for dictionary

        append_list[0] = book_name

        author_name = input("Enter Author name :")
        append_list[1] = author_name

        publisher_name = input("Enter Publisher name :")
        append_list[2] = publisher_name

        price = input("Enter Price of Book :")
        append_list[3] = price

        append_list[4] = 1
    books[book_name] = append_list


def books_edit(book_details):
    append_list=books[book_details]
    print("Press\n"
          "1. to change bookname .\n"
          "2. to change author name .\n"
          "3. to change publisher name .\n"
          "4. to change price of book .\n"
          "5. to change number of copies of book .\n")

    choice = input("Please choose :")

    if choice == '1':
        append_list[0] = input("Enter bookname :")

    elif choice == '2':
        append_list[1]=input("Enter Author name :")

    elif choice == '3':
        append_list[2]=input("Enter Publisher name :")

    elif choice == '4':
        append_list[3]=input("Enter Price of book :")

    elif choice == '5':
        append_list[4] = input("Enter Copies of book :")
    books[book_details] = append_list

    books[book_details] = append_list

def Issue_Book (members,books):
    current_date=datetime.now()
    issue_info=[]
    print("You can only issue a Book if your a Member or a Student.\n")
    id = int(input("Please enter your ID:"))
    a = id in members
    #To Check If The ID exists in the "members" List.
    if(a == True):
        bookname=input("Enter the book's name that you want to issue:")
        #To Check If The Book exists in the "books" List.
        a = bookname in books
        if(a == True and books[bookname][4]>0):
            a = id in book_issue
            if(a==True):
                book_count=book_issue[id][0]+1
                book_issue[id][0]=book_count
                book_issue[id].append(bookname)
                book_issue[id].append(current_date)
                book_issue[id].append(0)
                book_issue[id].append(0)
            else:
                book_count=1
                issue_info.append(book_count)
                issue_info.append(bookname)
                issue_info.append(current_date)
                issue_info.append(0)
                issue_info.append(0)
                book_issue[id]=issue_info
            #book_issue={210286:["Number of books issued","book's name","Issue Date","Return Date",Fine]}
            start=((book_count*4)-3)
            end=((book_count*4))
            books[bookname][4]=books[bookname][4]-1
            print("You have successfully issued the book:",bookname,"Have Fun Reading!!\nPs: The dew date is 4 weeks :)\n")
        else:
            print("Sorry, We do not have this book avaiable rightnow. Maybe comeback some other time :)\n")
            return 0
    else:
        print("Invalid ID. Only members and Students can use this library.\n")
        return 0

def book_return(books):
    count=0
    current_date=datetime.now()
    id = int(input("Please Enter Your ID:"))
    a = id in book_issue
    #To Check If The ID exists in the "book_issue" List.
    if(a == True):
        book_name = input("Please Enter The Book That You Want To Return:")
        name=((book_issue[id][0]*4)-3)
        fine=((book_issue[id][0]*4))
        for i in range (1,name+1,4):
            if (book_name==book_issue[id][i]):
                if(book_issue[id][i+2]==0):
                    if (count<=0):
                        book_issue[id][i+2]=current_date
                        pre_date=book_issue[id][i+1]
                        dd=(current_date-pre_date).days
                        if(dd>28):
                            print("You Are Submiting The Book After The Dew Date Which Is More Than 4 Weeks!!. You Will Be Fined A Heafty Price Of $20")
                            book_issue[id][i+3]
                            count=1
                            books[book_name][4]=books[book_name][4]+1
                        else:
                            print("Thank You For Returning The Book.Come Back Again!!")    
                            books[book_name][4]=books[book_name][4]+1
                else:
                    print("It Looks Like You Have Already Submitted This Book.")
            elif(i==name):
                print("Hmmm, Our Records Show That You Did Not Issue The Book:",book_name,"Maybe You Spelled It Worong Or Your At A Wrong Library.")
    else:
        print("Our Records Shows That You Did not Issue Any Book In The First Place. Maybe You Are In A Wrong Library? Something To Think About")                     

def books_display(book_details):
    title = books[book_details][0]
    print("Title : ", title)

    author = books[book_details][1]
    print("Author : ", author)

    publisher = books[book_details][2]
    print("Publisher : ", publisher)

    price = books[book_details][3]
    print("Price : ", price)

    copies = books[book_details][4]
    print("Number of copies : ", copies)

def members_add(id, name):
    z = id in members
    if z == True:
        print("Member exist!!.")
    else:
        members[id] = name


def members_remove(id):
    del members[id]


books = {'Python Machine Learning': ['Python Machine Learning', 'Sebastian Racheska', 'Packt', '$36.00', 1]
    , 'Python Essential Reference': ['Python Essential Reference', 'David M. Beazley', 'Developers Library', '$10.00',1]
    , 'Python in a nutshel': ['Python in a nutshel', 'Alex Martilli', 'O Reilly', '$30.90', 1]
    , 'C++ Primer': ['C++ Primer', 'Stanley B.Lippman', 'Addison Wesley Professional', '$44.13', 1]}

members = {210279: "Nayal usmani", 210278: "Khawar naeem ", 210284: "sadia yakoob", 210276: "muneeb khan"}

append_list1=[1,2,3,4]
condition = 'y'

while condition == 'y':
    print("\nPress\n"
          "1. to add a book .\n"
          "2. to add member .\n"
          "3. to remove member .\n"
          "4. to print details of book .\n"
          "5. to edit a book .\n"
          "6. to issue a book .\n"
          "7. to return a book .\n")

    choice = input("Please choose :")

    if choice == '1':
        book_name = input("Enter book to add :")
        add_books(book_name)

    elif choice == '2':
        id = int(input("please enter id :"))
        name = (input("please enter name :"))
        members_add(id, name)

    elif choice == '3':
        id = int(input("please enter id :"))
        members_remove(id)

    elif choice == '4':
        book_details = input("Enter Book name : ")
        books_display(book_details)

    elif choice == '5':
        book_details = input("Enter Book name to edit : ")
        books_display(book_details)
        books_edit(book_details)

    elif choice == '6':
        Issue_Book(members,books)
    elif choice == '7':

        book_return(books)
    condition = input("Do you want to use the program again? Press y/n :\n")
print(book_issue)
print("Thank you for using Program")