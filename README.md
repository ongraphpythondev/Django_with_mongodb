# Django_with_mongodb

<h1>Objective</h1><br>
"Established connection with django and MongoDB by using djongo and perform CRUD Operation"<br>

<h1>Prerequisites:</h1><br>

You will need the following programmes properly installed on your computer.<br>
Python 3.7+<br>
django 2.2+<br>
Virtual Environment To install virtual environment on your system use:<br>
pip install virtualenv<br>

or

pip3 install virtualenv #if using linux(for python 3 and above)<br>



<h1>Installation and Running :</h1><br>


git clone https://github.com/ongraphpythondev/Django_with_mongodb.git<br>
cd Django_with_mongodb<br>
virtualenv venv or virtualenv venv -p python3 #if using linux(for python 3 and above)<br>

venv\Scripts\activate # for windows or source venv/bin/activate # for linux<br>



<h1>Install required packages for the project to run</h1><br>
pip install -r requirements.txt<br>
python manage.py runserver<br>


<h1>MongoDB Setup </h1><br>
1.Install MongoDB compass and Server<br>
  A.Create DB and connection  <br>
2.python manage.py makemigrations<br>
3.python manage.py migrate<br>
4.create super user  (Because its simple CRUD operation with only admin panel)<br>
<h1>Test Url at local system<h1><br>
http://127.0.0.1:8000/admin
