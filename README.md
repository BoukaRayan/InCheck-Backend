# **InCheck-Backend**

This is a repository for the backend of a mobile application to streamline attendance management for events built with Django.

---

# **Frontend Repository**

You can check the frontend part of this project via this link: [Frontend](https://github.com/soualahmohammedzakaria/InCheck-App)

---

## **Prerequisites**

Before getting started, make sure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [MySQL](https://www.mysql.com/)

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

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
