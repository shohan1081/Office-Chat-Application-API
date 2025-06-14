# Office-Chat-Application-API

A Django backend project using WebSocket for real-time office communication.

Project Structure

- **Project Name**: `chat_project`
- **App Name**: `chat`
- **Virtual Environment**: `room`

Features

- ✅ Real-time WebSocket chat
- 🔐 Token-based authentication
- 📦 RESTful APIs with Django REST Framework
- ⚙️ Redis channel layers setup

Folder Structure

chat_project/
├── chat/
│ ├── consumers.py
│ ├── models.py
│ └── views.py
├── chatapi/
│ ├── settings.py
│ └── urls.py
├── manage.py
└── requirements.txt

Installation

### Step 1: Clone the Repository

git clone https://github.com/yourusername/chat_project.git
cd chat_project

Step 2: Set Up Virtual Environment
bash
Copy
Edit
python -m venv room

# For Windows:

room\Scripts\activate

# For macOS/Linux:

source room/bin/activate

Step 3: Install Requirements

pip install -r requirements.txt
Step 4: Run Redis Server (for Channels)
Make sure Redis is installed and running:

# For Linux/macOS

redis-server

# For Windows (using Redis CLI or WSL)

▶️ Running the Project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Visit: http://127.0.0.1:8000

🧠 Technologies Used
Django

Django Channels

Django REST Framework

WebSocket

Redis

Python 3

👨‍💻 Author
Shohanul Islam
Email: shohanulislam19892@gmail.com
GitHub: https://github.com/shohan1081
