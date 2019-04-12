# Project Setup

- Install Python 3.7.x
- Create a virtual environment with `python -m venv [virtual_env_name]`
- Activate the virtual environment:
```
cmd: cd [virutal_env_name]
cmd: cd Scripts
cmd: activate
[virtual_env_name] cmd: .....
```

- From the root of the project install dependencies into your venv with `pip install -r requirements.txt`
- The demo project uses SQLite as a DB backend, create database tables with the command: `python manage.py migrate`
- Create a superuser (admin) with the following command `python manage.py createsuperuser`
- You can now launch the Django server with `python manage.py runserver`
- Access the standard Django admin interface at: [http://127.0.0.1:8000/admin](http://127.0.0.1/admin)
- Access the Swagger API Reference interface at: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- You may need to login to the API through the "Authorize" button with the superuser that you have created.