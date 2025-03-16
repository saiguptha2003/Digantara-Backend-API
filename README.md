# Digantara Backend

This project is a backend service built with Flask that provides several algorithm-related APIs and logging functionalities.


### Note: Sorry, I have used all my free cloud credits, so I am not deploying it to the cloud.
## Building and Running the Application

### Prerequisites

- Docker
- Docker Compose

### Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/saiguptha2003/Digantara-Backend-API
    cd Digantara-Backend-API
    ```

2. **Build and run the application using Docker Compose:**
    ```sh
    docker-compose up --build -d
    ```

3. **Access the application:**
    The application will be available at `http://localhost:5000`.

## Running API Tests

### Prerequisites
- Python 3.x
- pytest (optional, for more detailed test output)

### Running Tests

1. **Using Python's unittest:**
    ```sh
    python -m unittest tests/testApi.py
    ```

2. **Using pytest (recommended):**
    ```sh
    pytest tests/testApi.py -v
    ```

3. **Running specific test cases:**
    ```sh
    python -m unittest tests/testApi.py -k test_quickSort
    ```

### Test Coverage
The test suite includes API endpoint tests for:
- Quick Sort algorithm
- Binary Search algorithm
- BFS traversal
- Log retrieval

Test files are located in the `tests/` directory.

## API Routes

### Get Logs

- **URL:** `/api/logs`
- **Method:** `GET`
- **Description:** Retrieves all log entries.
- **Response:**
    ```json
    [
        {
            "id": 1,
            "algorithm": "BinarySearch",
            "input": "...",
            "output": "...",
            "timestamp": "..."
        },
    ]
    ```

### Binary Search

- **URL:** `/api/binarySearch`
- **Method:** `POST`
- **Description:** Performs a binary search on a sorted array.
- **Request Body:**
    ```json
    {
        "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "target": 5
    }
    ```
- **Response:**
    ```json
    {
        "index": 4
    }
    ```

### Quick Sort

- **URL:** `/api/quickSort`
- **Method:** `POST`
- **Description:** Sorts an array using the quick sort algorithm.
- **Request Body:**
    ```json
    {
        "array": [10, 7, 8, 9, 1, 5]
    }
    ```
- **Response:**
    ```json
    {
        "sortedArray": [1, 5, 7, 8, 9, 10]
    }
    ```

### Breadth-First Search (BFS)

- **URL:** `/api/bfs`
- **Method:** `POST`
- **Description:** Performs a breadth-first search on a graph.
- **Request Body:**
    ```json
    {
        "graph": {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B"],
            "E": ["B", "F"],
            "F": ["C", "E"]
        },
        "startNode": "A"
    }
    ```
- **Response:**
    ```json
    {
        "bfsTraversal": ["A", "B", "C", "D", "E", "F"]
    }
    ```

## Environment Variables

- `FLASK_APP`: The entry point of the Flask application.
- `FLASK_RUN_HOST`: The host on which the Flask application runs.
- `FLASK_ENV`: The environment in which the Flask application runs (e.g., production).
- `DATABASE_URL`: The database URL for SQLAlchemy.

## Volumes

- `./logs:/app/logs`: Persist logs outside the container.
- `./migrations:/app/migrations`: Persist migrations outside the container.

## Using and Configuring `apiTest.http` in VSCode

### Prerequisites

- Visual Studio Code
- REST Client extension for VSCode

### Steps

1. **Install the REST Client extension:**
    - Open VSCode.
    - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
    - Search for "REST Client" and install it.

2. **Open the `apiTest.http` file:**
    - Navigate to the `apiTest.http` file in your project directory.
    - Open the file in VSCode.

3. **Send HTTP requests:**
    - Place your cursor inside any HTTP request block in the `apiTest.http` file.
    - Click on the "Send Request" button that appears above the request block or use the shortcut `Ctrl+Alt+R` (Windows/Linux) or `Cmd+Alt+R` (Mac).

4. **View responses:**
    - The response from the server will be displayed in a new tab within VSCode.

