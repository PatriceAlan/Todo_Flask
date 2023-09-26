# Todo Flask Application Setup Guide

Welcome to the Todo Flask application! This guide will walk you through the setup process so you can efficiently manage your tasks.

## Getting Started

Let's begin by setting up the Todo Flask application.

### Installation

1. **Clone the Repository**: Start by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/todo-flask.git
   cd todo-flask
   ```

2. **Install Dependencies**: Install the necessary Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**: Create a `.env` file in the project's root directory. You can use the provided `.env.example` file as a template.

### Running the Application

Now that you've completed the installation steps, it's time to run the Todo Flask application.

1. **Start Docker Compose**: Initialize the required services using Docker Compose with the following command:

   ```bash
   docker-compose up -d
   ```

   This command will create and start containers for MariaDB and phpMyAdmin.

2. **Access phpMyAdmin**: You can access phpMyAdmin by opening your web browser and navigating to:

   http://localhost:8000/

3. **Launch the Flask Application**: To run the Flask application locally, execute the following command:

   ```bash
   python app.py
   ```

### Accessing the Web Application

Once you've completed the above steps, the Todo Flask application will be up and running. To interact with it, simply open your web browser and go to:

http://localhost:5000/

Enjoy using the Todo Flask application to manage your tasks efficiently!
