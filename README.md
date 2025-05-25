# Names & Countries service

![Django REST Framework](https://www.django-rest-framework.org/img/logo.png)
![Docker](https://upload.wikimedia.org/wikipedia/commons/e/ea/Docker_%28container_engine%29_logo_%28cropped%29.png)
![Telegram Bot](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/120px-Telegram_logo.svg.png)

___

### About The Project

#### **This project provides a comprehensive set of endpoints to knowing about in which countries your name is popular**

* Check in which countries a given name is popular.

* Explore which names are popular in a specific country.


# Installation
1. **Clone the repository:**

   ```sh
   git clone 
   cd name_country

2. Create and activate **venv** (bash):
   ```sh
   python -m venv venv
   source venv/Scripts/activate
   ```
   Windows (Command Prompt)
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
   Mac / Linux (Unix like systems)
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
   
3. Create an `.env` file in the root of the project directory. You can use the `.env.example` file as a template (just change DJANGO_SECRET_KEY):
    ```sh
    cp .env.example .env
    ```
   
### Local installation:
1. Install **requirements.txt** to your **venv**:
   ```sh
   pip install -r requirements.txt
   ```
 
2. Create apply migrations:
   ```sh
   python manage.py migrate
   ```

3. Start the server:
   ```sh
   python manage.py runserver
   ```
   
### The API will now be accessible at http://localhost:8000/

##### For creating user you should:
1. Go to one of these link:
   - Register user: /user/register
   - Get token: /user/token

### Token Management
- Refresh your token when it expires using the following URL: /user/token/refresh
- Get information about yourself using the following URL: //localhost:8000/user/token/me

   
### Docker local installation:
1. Create app image and start it:
   ```sh
   docker-compose build
   docker-compose up
   ```
 
### If you used prefilled database from .json:
   - **admin_user**. email: admin@mail.com, password: 123123
   - **auth_user**. email: user@mail.com, password: 123123

## Important Endpoints in Project:

##### * /api/user/ - User page
##### * /api/names/?name="Name you are looking for"
##### * /api/popular-names/?country="Country you are looking for"
For detailed API documentation, visit [Swagger Documentation](http://localhost:8000/api/doc/swagger/).


## Key Features
Telegram alert
![Screenshot 2025-05-25 184455.png](../../../OneDrive/Pictures/Screenshots/Screenshot%202025-05-25%20184455.png)






