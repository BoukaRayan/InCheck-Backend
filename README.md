# **InCheck-Backend**

InCheck-Backend is the backend for a check-in platform built with Django.

---

## **Prerequisites**

Before getting started, make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- Mysql
- Git

---

## **Installation**

Clone the project and install dependencies by following these steps:

```bash
# Clone the repository
git clone https://github.com/BoukaRayan/InCheck-Backend.git

# Navigate to the project directory
cd InCheck-Backend

# Install dependencies
pipenv install

# Activate the virtual environment
pipenv shell
```

---

## **Configuration**

Create a .env file in the root directory of the project using the following format:

```bash
SECRET_KEY= 
DEBUG=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=
```
Ensure that the .env file contains the correct information for your MySQL database.

---

## **Starting the Server**

Apply migrations and start the server by following these steps:

```bash
# Apply migrations
python manage.py migrate

# Start the server
python manage.py runserver
```
The server will be accessible at http://127.0.0.1:8000/.










