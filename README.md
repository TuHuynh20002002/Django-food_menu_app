## Introduction
Today application is Food Menu. This project use Python programming languague and Django web application framework. Boostrap 5 is used as main css framework. Database engine is various, now it is using SQLite, it may be changed later.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,django,bootstrap,sqlite&perline=10" />
  </a>
</p>


## Features
- Food menu app using Django.
- Django built-in template view.
- Features: menu, order, order-history, store-location, reward.
- Custom Authentication function.


## Installation
To use this app, you need to have Python3 and Django on your machine. You can install them by following the instructions:
- Python: [Download](https://www.python.org/downloads/)
- Django: [Download](https://www.djangoproject.com/download/)


## Usage
1.  Clone or download the repository to your local machine.

2.  Open a terminal or command prompt and navigate to the project directory.

3.  Run initial migration:
    ```bash
    python3 manage.py migrate
    ```

4.  Create Super-admin user:
    ```bash
    python3 manage.py createsuperuser 
    ```

5.  Seeding all `seeding_file.json`:
    ```bash
    find . -path "*/fixtures/*.json" -type f -exec python3 manage.py loaddata {} +
    ```

6.  Run server:
    ```bash
    python3 manage.py runserver
    ```


## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome!