
<p align="center" markdown=1>
  <i>Basic-Ride-Sharing-API-with-Class-Based-Viewsets.</i>
</p>
<hr>
<p align="justify">
<b>FastCRUD</b> is a Python package for <b>FastAPI</b>, offering robust async CRUD operations and flexible endpoint creation utilities, streamlined through advanced features like <b>auto-detected join</b> conditions, <b>dynamic sorting</b>, and offset and cursor <b>pagination</b>.
</p>
<hr>
<h2>Requirements</h2>
<p>Before installing Ride-Sharing-API, ensure you have the following prerequisites:</p>
<ul>
  <li><b>Python:</b> Version 3.9 or newer.</li>
  <li><b>Django:</b> Django REST framework is used to built REST APIs, so having Django and Django REST framework in your project is essential.</li>
  <li><b>djangorestframework-simplejwt:</b> Ride-Sharing-API uses JWT for authentication and authorization in the project .</li>
  <li><b>drf-yasg:</b> Ride-Sharing-API uses this package for the documentation .</li>
</ul>

<h2>Installing</h2>
<P>The whole installations need to be done inside the virtual environment by activating it and use it througout the entire project .</P>

 To install required packages, just run:
 ```sh
 pip install requirements.txt
 ```
 for data migrations if needed, just run:
 ```sh
 python manage.py makemigrations
 python manage.py migrate
 ```
 To start the project, just run:
 ```sh
 python manage.py runserver
 ```
