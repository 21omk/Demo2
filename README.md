# Demo2

A basic REST API backend built with Node.js and Express.js.

## Features

- RESTful API endpoints for user management
- Health check endpoint
- In-memory data storage
- Comprehensive test suite using Jest and Supertest

## Prerequisites

- Node.js (v14 or higher)
- npm

## Installation

1. Clone the repository
2. Install dependencies:
```bash
npm install
```

## Running the Server

Start the server with:
```bash
npm start
```

The server will start on port 3000 by default.

## API Endpoints

### Health Check
- **GET** `/api/health`
  - Returns server health status
  - Response: `{ "status": "OK", "message": "Server is running" }`

### Users

#### Get All Users
- **GET** `/api/users`
  - Returns a list of all users
  - Response: Array of user objects

#### Get User by ID
- **GET** `/api/users/:id`
  - Returns a specific user by ID
  - Response: User object or 404 if not found

#### Create User
- **POST** `/api/users`
  - Creates a new user
  - Request body: `{ "name": "string", "email": "string" }`
  - Response: Created user object with ID
  - Validation: Name and email are required; email must be unique

## Example Usage

### Get all users
```bash
curl http://localhost:3000/api/users
```

### Get a specific user
```bash
curl http://localhost:3000/api/users/1
```

### Create a new user
```bash
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com"}'
```

## Running Tests

Run the test suite with:
```bash
npm test
```

The test suite includes:
- Health endpoint tests
- User listing tests
- User retrieval tests
- User creation tests
- Validation tests
- Error handling tests

## Project Structure

```
Demo2/
├── app.js           # Express application and routes
├── server.js        # Server entry point
├── app.test.js      # Test suite
├── package.json     # Project dependencies and scripts
├── .gitignore       # Git ignore rules
└── README.md        # This file
```
