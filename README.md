# ACEest Fitness & Gym — DevOps Assignment

## 1. Project Overview

ACEest Fitness & Gym is a Flask-based Python application developed as part of a DevOps assignment. This project demonstrates the implementation of modern DevOps practices, including version control, automated testing, Docker containerization, Continuous Integration (CI), and Jenkins-based builds.

### Objectives

- Manage source code using Git and GitHub.
- Validate application functionality using Pytest.
- Package the application and its dependencies using Docker.
- Automate build and test validation using GitHub Actions.
- Configure Jenkins to retrieve source code and execute a build pipeline.

## 2. Technology Stack

- **Programming Language:** Python
- **Web Framework:** Flask
- **Testing Framework:** Pytest
- **Version Control:** Git and GitHub
- **Containerization:** Docker
- **Continuous Integration:** GitHub Actions
- **Build Automation:** Jenkins

## 3. Project Structure

```text
Assignment_DevOps/
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/
        └── main.yml
```

## 4. Local Setup and Execution

### Prerequisites

Install Python, Git, and a code editor such as Visual Studio Code. Install Docker Desktop if you want to run the application in a container.

### Step 1: Clone the repository

```bash
git clone https://github.com/2025tm93140-Mohanavalli/Assignment_DevOps.git
cd Assignment_DevOps
```

### Step 2: Create a virtual environment

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

On Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

Open the local URL displayed by Flask in your browser. If the application uses the default port, the address is `http://127.0.0.1:5000/`.

## 5. Automated Testing with Pytest

Pytest is used to validate the application's functionality before the build is considered successful.

Run the tests locally:

```bash
python -m pytest -v
```

The test suite is maintained in `test_app.py`. The current Jenkins pipeline has successfully executed all three automated tests.

## 6. Docker Containerization

The Dockerfile packages the Python application and its dependencies into a portable image using the Python 3.13 slim base image.

### Build the Docker image

```bash
docker build -t aceest-fitness:latest .
```

### Run the container

```bash
docker run --rm -p 5000:5000 aceest-fitness:latest
```

Open `http://127.0.0.1:5000/` in your browser if the application listens on port 5000.

### Run automated tests inside the container

```bash
docker run --rm --entrypoint sh aceest-fitness:latest -c "pip install pytest && pytest -v"
```

This runs the Pytest suite inside the containerized environment.

## 7. Jenkins BUILD Pipeline

Jenkins is configured to retrieve the project from the GitHub repository and execute the build pipeline.

The pipeline includes the following stages:

1. **Checkout from GitHub:** Retrieves source code from the `master` branch.
2. **Check Docker:** Verifies that Docker is available on the Jenkins agent.
3. **Build Docker Image:** Builds the application image using the Dockerfile.
4. **Run Automated Tests:** Executes the Pytest suite inside the Docker container.

The Jenkins pipeline has completed successfully, with all three automated tests passing.

## 8. GitHub Actions CI Pipeline

The GitHub Actions workflow is defined in:

`.github/workflows/main.yml`

The workflow is configured to run on code pushes and pull requests.

The pipeline performs these tasks:

1. **Build and Lint:** Validates Python syntax and performs the configured build and lint checks.
2. **Docker Image Assembly:** Builds the Docker image to verify the container configuration.
3. **Automated Testing:** Runs the Pytest suite in the containerized environment.

This automated workflow provides early feedback when changes are introduced and helps identify integration issues before delivery.

## 9. Version Control

Git and GitHub are used to maintain the project's source code and configuration files.

Example Git commands:

```bash
git status
git add .
git commit -m "Add project documentation"
git push origin master
```

Descriptive commit messages help maintain traceability of changes to application code, tests, and infrastructure configuration.

## 10. Conclusion

This project demonstrates an automated DevOps workflow for the ACEest Fitness & Gym application. It integrates version control, unit testing, Docker containerization, GitHub Actions, and Jenkins to improve consistency, reliability, and repeatability throughout the software delivery lifecycle.

**Repository:** https://github.com/2025tm93140-Mohanavalli/Assignment_DevOps
