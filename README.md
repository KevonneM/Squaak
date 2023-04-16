Squaak

Welcome to Squaak, a web application for connecting with friends through a real-time communication platform!
Features

    🔒 User registration and login
    🙋‍♂️🙋‍♀️ Add and remove friends
    🗣️ Create public chat rooms for multiple user inputs
    📹 Video chat with other users based on room name
    💬 Direct messaging with other users

Getting Started

  To get started with Squaak, follow these steps:

  1. Clone the repository to your local machine by running git clone https://github.com/your-username/squaak.git.
  2. Install pipenv by running pip install pipenv.
  3. Navigate to the root directory of the project and run pipenv install to create the virtual environment and install the required dependencies.
  4. Create a .env file in the root directory of the project, and add the following environmental variables: SECRET_KEY, SENDGRID_API_KEY, appCertificate, and appID with their respective values. These variables are required for Squaak to work properly.
  5. Run the migrations by running python manage.py migrate.
  6. Create a superuser by running python manage.py createsuperuser.
  7. Start the development server by running python manage.py runserver.
  8. Access Squaak on your web browser by visiting http://localhost:8000/.
  
  That's it! You should now be able to use Squaak's video chat and messaging features. If you encounter any issues while setting up Squaak, please feel free to reach out.

Built With

    Python
    Django
    sqlite3

Authors

    Kevonne Montes - KevonneM
    Michael Brown - Michael-LeRoyBrown

Acknowledgments

    💡 Inspiration for this project came from the desire to expand my knowledge on web application development and woring with Python, Django, and many other tools.
    🙏 Special thanks to my co-contributor Michael Brown for building this along-side me.
