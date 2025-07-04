# Tylko Recruitment Enhanced Repo

This repository contains the enhanced version of the Tylko recruitment project. It includes a Django backend with PostgreSQL as the database and other dependencies for development and testing.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Local Development](#local-development)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)

## Features

- **Django Framework**: Used for building the backend.
- **PostgreSQL Database**: Manages data storage.
- **Docker Compose**: Simplifies running and managing multi-container Docker applications.
- **pytest**, **pytest-django**, **pytest-cov**: For testing and code coverage.

## Setup

### Prerequisites

1. **Docker**: Ensure Docker is installed on your machine.
2. **Docker Compose**: Make sure Docker Compose is available (usually included with Docker).
3. **Python**: While not directly used for running the application, it might be needed for some development tasks.

### Local Development

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/chilledsnake/tylko-recruitment-enhanced-repo.git
   cd tylko-recruitment-enhanced-repo
   ```
   
2. **Copy Environment Variables**:
    ```sh
    cp .env.template .env
   ```

3. **Start the Application**:
    ```sh
    docker compose up
   ```
This command will build the Docker images and start both the backend and database containers.

Access the Application:

Backend (swaggerUI): http://localhost:8000/docs
Database (if needed): http://localhost:5432