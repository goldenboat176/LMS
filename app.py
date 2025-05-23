import streamlit as st
from LMS import Member
from LMS import Library 
from LMS import Book


l = Library(120, "Fredbear Road")
st.image("9043296.png", width = 200)
st.title("  Library Management System(LMS)  ")
st.write("This is a library management system\nWe make forms")#

#sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose one: ",
                        ["Home","Books","Members","Borrowings"],
                        )

if page == "Home":
    st.header("This is a Library Management System based in Fredbear Road, we have a selection of 120 books of different genres and departments.")
    
def viewallbooks():
    bookslist = l.viewbooks()
    if bookslist:
        for book in bookslist:
            print(book)
            id,title,numpages,author = book
            col1,col2,col3 = st.columns([3,2,1])
            with col1:
                st.write(f"The title: {title}")
            with col2:
                st.write(f"The Number of pages: {numpages}")
            with col3:
                st.write(f"The Author: {author}")



if page == "Books":

    
    tab1,tab2,tab3 = st.tabs(["View all books","Add a book","Delete a book"])
    with tab1:
        st.header("View all books")
        
        viewallbooks()
    
    with tab2:
        st.header("Add a book")
        bookname = st.text_input("Enter the name of the book")
        booknumpages = st.text_input("Enter the number of pages")
        bookauthor = st.text_input("Who is the book's author?")
        

        if st.button("Submit"):
            try:

            
                b = Book(bookname,booknumpages,bookauthor)
                b.addbooktodb()
                st.success("A new book has been added to the database.") # hw is to link it to the LMS file

            except:
                st.error("Error occured while adding.\nPlease try again.")

    with tab3:
        st.header("Delete a book")
        st.write("*WARNING IF YOU DELETE THIS BOOK FROM THE DATABASE, IT CANNOT BE RESTORED*")
        #viewallbooks()
        bookslist = l.viewbooks()
        if bookslist:
            bookslist = [book[1] for book in bookslist]
            selected_book = st.selectbox("Choose a book to delete: ",bookslist)
            selectedtitle = selected_book
            
            if st.button("DELETE"):
                try:
                    l.deletebook(selectedtitle)
                    st.success(f"{selectedtitle} has been successfully deleted")
                except:
                    st.error("An error occurred, please try again")


#updte form, display everything and chooses what to change in a book's properties 
#check python anywhere or streamlit hub for streamlit
    




if page == "Members":
    st.header("Members page")
    membername = st.text_input("Enter your name")
    memberage = st.number_input("Enter your age",min_value = 0, max_value = 100, step =1 )
    departments = ["Art", "Biology", "Chemistry", "Drama", "English", "Maths", "Music", "Physics", "Social Studies", "Sport"]
    deptname = st.selectbox("Select the department",departments)

    if st.button("Submit"):
        try:

            m = Member(membername,memberage,deptname)
            m.addmembertodb()
            st.success("A new member has been created.") # hw is to link it to the LMS file

        except:
            st.error("Error occured while adding.\nPlease try again.")


    

    
#tabs about the form 
#tabs about book form ADD A NEW BOOK
