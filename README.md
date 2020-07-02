# Library-Management-Software
<img src = "/clg/static/book.jpg" height = "200" width="200" align="left">

Library Management Software works for saving data. It can used to check the updates of books in library for students well as teachers with coming to the library. It can be used for saving information like which book was return, issue and add. Issue, Return and Add new books columns can only be access by admins who have the library code.


## Working and Features

**This website is simple to use. First go to our website (our first page is designed in html it's named as homepage.html which is inside the template of shop folder) then just click the courses and platforms you want to check and learn then join courses according to your needs and budgets. It provide you the best courses and platforms.**
* **Firstly you have to login or signup for checkout the features. **
* **Then you can issue book, return book or add book. These column can only be access by those who have library code. All the data will be directly save to our database.**
* **Then there are columns for those who don't have the library code, they can use the books column in which all the books present will be there i.e. the number of books with little description. Other than this there is a resume column in which resume format has been uploaded and library map.**

## To run locally

1. Python 3
2. install dependency: \
     `pip install django`
3. move in your project folder and run the commands given below:\
     `python manage.py makemigrations`\
     `python manage.py migrate`\
     `python manage.py runserver`
