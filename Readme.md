
# HTTP Endpoint Health Checker

## Overview
This project monitors the health of HTTP endpoints as defined in a YAML configuration file. It checks each endpoint's availability every 15 seconds and logs the cumulative availability percentage for each domain.

---

## Prerequisites
- Python 3.9 or higher installed on your system.
- Install Docker (optional, for containerized execution): [Docker Installation Guide](https://docs.docker.com/get-docker/).

---

## How to Run the Project

### Option 1: Run Without Docker

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set Up a Virtual Environment (Optional)**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the YAML Configuration File**
   If you want to use a custom YAML file, change the contents of the sample.yml or just pass it as an argument while running the application

   

5. **Run the Application**
   Execute the program with the path to your YAML file or just use sample.yml:
   ```bash
   python health.py sample.yml
   ```

6. **Stopping the Application**
   Press `CTRL+C` to stop the application.

---

### Option 2: Run With Docker (Default Sample Configuration)

The Docker image includes a `sample.yml` file, which is used by default. To run the container with the included configuration:
```bash
docker run --rm health-checker
```

This will use the `sample.yml` file that is bundled with the Docker image during the build process.

---

### Option 3: Run With Docker (Custom Configuration File)

If you want to use a custom YAML configuration file, you can mount it at runtime:
```bash
docker run --rm -v $(pwd)/sample.yaml:/app/sample.yaml health
```

Replace `sample.yaml` with the path to your custom file.

---

## How to Modify the YAML File
If you need to change the endpoints being monitored:

1. **Default Sample Configuration**:
   Modify the `sample.yml` file in the project directory and rebuild the Docker image:
   ```bash
   docker build -t health .
   ```

2. **Custom Configuration File**:
   Modify your custom YAML file locally, then mount it at runtime (as shown in Option 3 above).

---

## Project Files

### 1. health.py
The main Python script that implements the health-checking logic.

### 2. sample.yml
The default YAML file defining the endpoints to be monitored, included in the Docker image.

### 3. requirements.txt
The Python dependencies for the project:
```plaintext
requests
pyyaml
```

### 4. Dockerfile
The configuration for building the Docker image.

---

## Notes
- Ensure your `sample.yml` file is well-formed.
- The availability percentages are cumulative over the lifetime of the program.

---

## Example Output
```plaintext
fetch.com has 67% availability percentage
www.fetchrewards.com has 50% availability percentage
```
