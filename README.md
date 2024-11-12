# Sports Web Application

This is a sports-focused web application that allows users to view and manage teams, players, competitions, and matches. The application provides a backend built with Flask (Python) and a frontend built with React. This README file outlines the setup process for running the application both in a Docker container or locally using XAMPP.

## Features:
- **Frontend**: Built with React, allowing users to view and interact with teams, players, and view matches.
- **Backend**: RESTful API built with Flask, providing endpoints to interact with teams, players, matches, and other sports-related data.
- **Swagger UI**: Integrated for easy API documentation and interaction.
- **Dockerized Setup**: The application can be run in a Docker container for easy deployment.
- **Local Server (XAMPP)**: Alternative setup for running the application using local XAMPP environment with Flask backend.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Docker Setup](#docker-setup)
- [Local Setup Using XAMPP](#local-setup-using-xampp)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [POST Data for API](#post-data-for-api)
- [Unit Testing](#unit-testing)

## Prerequisites

Before you begin, ensure you have the following installed:
- **Docker**: For containerized setup.
- **Vite & React**: For frontend development.
- **Python 3.x & pip**: For backend setup.
- **XAMPP**: For local PHP/MySQL server setup (if not using Docker).
- **Swagger UI**: Accessed via Flask API.

## Docker Setup

### Step 1: Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/faraaztj7/sports_app.git
cd sports-web-app

### Step 2: Build Docker Containers
The project comes with a pre-configured Docker setup for both frontend and backend.
1. Build Docker Containers: 
2. Run the following command to build the containers: -docker-compose up -- build

3. Access the Application:
    1. Frontend: Navigate to http://localhost:5173 to view the React frontend.
    2. Backend: The Flask API will be accessible at http://localhost:5000.

4. Access Swagger UI: Swagger UI for testing the backend APIs will be available at http://localhost:5000/.
5. Stopping Cotainers Command : docker-compose down

## Local Setup Using XAMPP

### Step 1: Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/faraaztj7/sports_app.git
cd sports-web-app

### Step 2: Setup Backend with Flask
    1. Create a Virtual Environment : python -m venv venv
         Activate : .\venv\Scripts\activate
    2. Install Required Dependencies: Install the required Python packages: pip install -r requirements.txt
    3. Run the Backend: Start the Flask application: python run.py

### Step 3: Setup Frontend
    1. Install Dependencies: Navigate to the frontend directory and install the required npm packages: cd frontend & npm install
    2. Run the Frontend: Start the React development server: npm start
    3. Access the Application:
        Run the XAMPP server.
        The frontend will be available at http://localhost:5173.
        The Flask backend will be available at http://localhost:5000.

## Backend Setup
The backend provides several API endpoints to interact with the sports data. These endpoints are accessible via the Flask application running at http://localhost:5000.

Available Endpoints:
- GET /teams/: List all teams with optional filters for name and city.
- POST /teams/: Create a new team (requires name and city).
- GET /teams/{id}: Get details of a specific team by ID.

- GET /players/: List all players.
- GET /players/{id}: Get details of a specific player by ID.
- POST /teams/: Creates a new player.

- GET /areas/: List all areas.
- POST /areas/: Create a new area (requires name).
- GET /areas/{id}: Get details of a specific area by ID.

- GET /competitions/: List all the types of competitions.
- POST /competitions/: Create a new competition.

- GET /matches/: List all matches with optional filtering by date, location, team, or player
- POST /matches/: Create new matches for the teams.

## Frontend Setup
The frontend is built using React and provides an interactive UI for viewing teams, players, and matches.

1. The frontend makes API calls to the Flask backend to retrieve and display data.
2. Components:
    - TeamList: Displays a list of teams.
    - PlayerList: Displays a list of players.
    - MatchList: Displays upcoming matches.

## POST Data for API
You can implement Post data using Swagger UI in http://localhost:5000 or you can use POSTMAN

1. TEAMS - POST /teams:
        Request Body : {
                        "name": "Team Name",
                        "city": "City Name"
                        }
        Response Body (201):{
                            "id": 1,
                            "name": "Team Name",
                            "city": "City Name"
                            }

2. PLAYERS  - POST /players:
        Request Body : {
                        "name": "Player Name",
                        "position": "Player Position"
                        "team_id": 0
                        }
        Response Body (201):{
                            "id": 0,
                            "name": "string",
                            "position": "string",
                            "team": "string"
                            }

3. AREAS  - POST /areas:
        Request Body : {
                        "name": "Stadium Name",
                        }
        Response Body (201):{
                            "id": 0,
                            "name": "string"
                            }

4. COMPETITIONS  - POST /competitions:
        Request Body : {
                        "name": "Competition Name",
                        }
        Response Body (201):{
                            "id": 0,
                            "name": "string"
                            }
                        
5. MATCHES  - POST /matches:
        Request Body : {
                        "date": "2024-11-20T08:30:00",
                        "home_team_id": 0,
                        "away_team_id": 0,
                        "competition_id": 0,
                        "area_id": 0
                        }
        Response Body (201):{
                            "id": 0,
                            "date": "2024-11-11T09:57:35.730Z",
                            "home_team": "string",
                            "away_team": "string",
                            "competition": "string",
                            "area": "string"
                            }  

## Unit Testing
To run unit tests for the backend API, ensure that the Flask app is running in a separate test environment.
Also the unit tests will run if it is run by `docker` ny build step.
To run seperatey in Backend

## Step 1: Install pytest
Install the testing dependencies: pip install pytest

## Step 2: Run Tests
Run the tests with pytest: pytest

Note: The test cases are run by using static data not from Database so as to show the implementation for each functional API's.
