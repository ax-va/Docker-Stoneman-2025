# Optimizing Docker Build with the Build Cache

- Docker can reuse cached results from previous builds
  when a Dockerfile instruction and its relevant inputs have not changed.

- Therefore, Dockerfile instructions should generally be ordered 
  so that less frequently chnaging inputs come before more frequently changing ones.

- A common example is a Python application

    ```
    project/
    |-- .dockerignore
    |-- Dockerfile
    |-- requirements.txt
    |-- app/
        |-- main.py
    ```

    ```dockerfile
    FROM python:3.12-slim
    
    WORKDIR /app
    
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    COPY app .
    
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
    ```
  If the application code changes, but `requirements.txt` does not,
  Docker can reuse the cached result of the dependency installation 
  and only execute the build steps affected by the changed application code.