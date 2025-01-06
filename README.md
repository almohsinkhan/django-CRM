
# Django CRM Website

This is a Django-based CRM (Customer Relationship Management) website that provides essential functionality for managing customer records. The project features user authentication and a responsive interface, making it easy to add, update, and delete records.

## Features
- **User Authentication:** Secure login, logout, and sign-up functionality.
- **Customer Management:** Add, update, and delete customer records.
- **Responsive Design:** Built with Bootstrap for an intuitive and mobile-friendly interface.
- **Database Integration:** Uses MySQL for robust data management.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL

## Setup and Installation
To set up this project locally, follow these steps:

1. Clone the repository:

   git clone https://github.com/almohsinkhan/django-CRM.git

2. Navigate to the project directory:
   cd django-CRM
3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
4. Install the required dependencies:
   pip install -r requirements.txt
   
5. Configure the MySQL database:
   - Create a new MySQL database.
   - Update the `DATABASES` settings in the `settings.py` file with your database credentials.
6. Apply the database migrations:
   
   python manage.py migrate
7. Create a superuser:
   python manage.py createsuperuser
   
8. Run the development server:
   python manage.py runserver
   

## Usage
1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Log in or create a new user account.
3. Use the interface to manage customer records.

## Screenshots
[Add screenshots or a demo GIF to showcase your project.]

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments
- **Django Documentation:** [Django Project](https://docs.djangoproject.com/)
- **Bootstrap Documentation:** [Bootstrap](https://getbootstrap.com/)
- Inspired by various CRM tools.


Feel free to explore the project and contribute! 😊
![Screenshot 2025-01-06 230637](https://github.com/user-attachments/assets/52943dec-65f5-44d5-b902-c4a668be9526)
![Screenshot 2025-01-06 230701](https://github.com/user-attachments/assets/9c16b233-ce69-4c56-9332-6934efdd41f1)
![Screenshot 2025-01-06 230709](https://github.com/user-attachments/assets/49e73fb7-5ba8-478d-8ef9-603226838397)
![Screenshot 2025-01-06 230731](https://github.com/user-attachments/assets/0733dcdb-8e05-4727-adb5-772789b0cea7)
![Screenshot 2025-01-06 230740](https://github.com/user-attachments/assets/120dc884-a7b1-40e8-a3d3-10e9ce670842)








