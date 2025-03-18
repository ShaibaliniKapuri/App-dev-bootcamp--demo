# App-dev-bootcamp--demo
This is an application created for a demo in Application development Bootcamp for Application Development 1 Project Bootcamp in IIT Madras BS Degree

# Flask Blog Application

A full-featured blog application built with Flask, Flask-SQLAlchemy, Flask-Login, and Flask-RESTful. This application allows users to create, edit, and delete posts, comment on posts, and search for posts or users. It also includes an admin dashboard with statistics and charts.

---

## Features

- **User Authentication**:
  - Register, login, and logout functionality.
  - Role-based access control (admin and general user).

- **Blog Posts**:
  - Create, edit, and delete posts.
  - View all posts on the home page.

- **Comments**:
  - Add comments to posts.
  - Edit and delete your own comments.

- **Search**:
  - Search for posts or users by keyword.

- **Admin Dashboard**:
  - View app statistics (total users, posts, and comments).
  - Visualize data using Chart.js.

- **RESTful API**:
  - Retrieve all posts and comments via `GET` requests.
  - Create new posts and comments via `POST` requests.

---

## Technologies Used

- **Backend**:
  - Flask (Python web framework)
  - Flask-SQLAlchemy (ORM for database management)
  - Flask-Login (user authentication)
  - Flask-RESTful (REST API development)

- **Frontend**:
  - HTML, CSS
  - Bootstrap (styling)
  - Chart.js (data visualization)

- **Database**:
  - SQLite (default database for development)

---

## Setup Instructions

### Prerequisites

- Python 3.x
- Pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/App-dev-bootcamp--demo.git
   cd App-dev-bootcamp--demo
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   ```bash
   python
   >>> from app import db, create_app
   >>> db.create_all(app=create_app())
   >>> exit()
   ```

6. **Run the application**:
   ```bash
   python app.py
   ```

7. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:5000/`.

---

## API Documentation

### Endpoints

#### 1. **Posts**
- **GET `/api/posts`**:
  - Retrieve all posts.
  - Example response:
    ```json
    [
      {
        "id": 1,
        "title": "My First Post",
        "content": "This is the content of my first post.",
        "author": "user1",
        "comments": [
          {
            "id": 1,
            "content": "Great post!",
            "author": "user2",
            "timestamp": "2023-10-01T12:34:56"
          }
        ]
      }
    ]
    ```

- **POST `/api/posts`**:
  - Create a new post.
  - Required fields: `title`, `content`, `user_id`.
  - Example request:
    ```json
    {
      "title": "New Post",
      "content": "This is a new post.",
      "user_id": 1
    }
    ```
  - Example response:
    ```json
    {
      "message": "Post created successfully",
      "id": 3
    }
    ```

#### 2. **Comments**
- **GET `/api/comments`**:
  - Retrieve all comments.
  - Example response:
    ```json
    [
      {
        "id": 1,
        "content": "Great post!",
        "author": "user2",
        "post_id": 1,
        "timestamp": "2023-10-01T12:34:56"
      }
    ]
    ```

- **POST `/api/comments`**:
  - Create a new comment.
  - Required fields: `content`, `user_id`, `post_id`.
  - Example request:
    ```json
    {
      "content": "Great post!",
      "user_id": 2,
      "post_id": 1
    }
    ```
  - Example response:
    ```json
    {
      "message": "Comment created successfully",
      "id": 5
    }
    ```

---

## Usage

### Web Application

1. **Register a new user**:
   - Go to `http://127.0.0.1:5000/register` and fill out the registration form.

2. **Log in**:
   - Go to `http://127.0.0.1:5000/login` and enter your credentials.

3. **Create a post**:
   - After logging in, click "Create Post" and fill out the form.

4. **Add a comment**:
   - View a post and add a comment using the comment form.

5. **Search**:
   - Use the search bar in the navigation bar to search for posts or users.

6. **Admin Dashboard**:
   - Log in as an admin (`admin@example.com` / `admin123`) to access the admin dashboard at `http://127.0.0.1:5000/admin/dashboard`.

---

### RESTful API

1. **Get all posts**:
   ```bash
   curl http://127.0.0.1:5000/api/posts
   ```

2. **Create a post**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"title": "New Post", "content": "This is a new post.", "user_id": 1}' http://127.0.0.1:5000/api/posts
   ```

3. **Get all comments**:
   ```bash
   curl http://127.0.0.1:5000/api/comments
   ```

4. **Create a comment**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"content": "Great post!", "user_id": 2, "post_id": 1}' http://127.0.0.1:5000/api/comments
   ```


