# BlogBridges

## Description
BlogBridges is a simple blog application built with Django. It allows users to create, view, and manage blog posts while providing user authentication features.

## Features
- User authentication (signup, login, logout)
- Create, view, and manage posts

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd django_blog
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Usage
To run the application, use the following command:
```bash
python manage.py runserver
```
Then, open your browser and go to `http://127.0.0.1:8000/`.

## URL Routing
The following URL patterns are defined in the application:
- `/signup/` - User signup
- `/loginn/` - User login
- `/signout/` - User logout
- `/` - Home page displaying all posts
- `/newpost/` - Create a new post
- `/mypost/` - View posts created by the logged-in user

## Data Models
The application includes the following model:
- **Post**
  - `title`: CharField (max_length=100)
  - `user`: ForeignKey (User)
  - `content`: TextField
  - `date`: DateTimeField (auto_now_add=True)

## Templates
The application uses Django templates for rendering HTML. The base template is `base.html`, which includes Bootstrap for styling.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.
