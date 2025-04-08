# FastAPI_Task

This project demonstrates a simple microservices architecture using **FastAPI**, **PostgreSQL**, and **Docker Compose**. It includes two separate services that interact with each other:

- **User Service**: Manages user creation.
- **Notification Service**: Accepts notifications from the User Service when a new user is registered.

---

## Features

- Microservices-based project with independent responsibilities
- PostgreSQL as the backend database for each service
- FastAPI for building lightweight REST APIs
- Docker Compose to manage containers
- Service-to-service communication over HTTP

---

## Project Structure

```bash
/FastAPI_task
├── user_service
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── db/
│   │   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── notification_service
│   ├── app/
│   │   ├── consumers/
│   │   ├── core/
│   │   ├── services/
│   │   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Prerequisites

Before you begin, make sure you have:

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/) installed

---

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/msaisri1/FastAPI_Task.git
cd FastAPI_Task
```

### Step 2: Start the Services

Use the following command to build and start the containers:

```bash
docker-compose up --build
```

This command will:
- Build Docker images for both services
- Start the services and their PostgreSQL databases
- Expose the APIs on:
  - **User Service**: http://localhost:8000
  - **Notification Service**: http://localhost:8001
