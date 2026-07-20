# GateKeep

GateKeep is a Flask-based authentication system that allows users to register, log in, reset their password, and access a protected dashboard. It demonstrates the implementation of secure authentication using MySQL, bcrypt password hashing, and Flask session management, along with a clean and user-friendly interface.



## Features

- User Registration
- User Login
- Forgot & Reset Password
- Password Hashing using bcrypt
- Session-Based Authentication
- Password Strength Indicator
- Show/Hide Password
- Protected Dashboard
- Responsive User Interface



## Tech Stack

- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript
- bcrypt
- python-dotenv



## Installation

```bash
git clone https://github.com/AbhishkaCraft/GateKeep.git
cd GateKeep

pip install -r requirements.txt

python app.py
```

Create a `.env` file with your MySQL credentials and secret key before running the application.



## Security

- Passwords are hashed using bcrypt.
- Sensitive credentials are stored in a `.env` file.
- Flask sessions are used to protect authenticated routes.



## Future Improvements

- Email-based password reset
- OTP verification
- Remember Me functionality
- User profile management






