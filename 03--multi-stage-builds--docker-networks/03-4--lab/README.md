# Docker Networks

## Lab 3: Container-to-Container Communication

Task:

Build a small multi-container application
that demonstrates communication between containers over a Docker network.

The application should consist of two independent services:

- A data service that imitates a database and exposes book data through an HTTP API.

- A backend application built with FastAPI and organized into web, service, and data layers.
  The data layer should asynchronously retrieve book data from the data service,
  while the service layer should apply simple business logic to the retrieved data.

Package each service as a separate Docker image and run them in separate containers 
connected to the same user-defined Docker network.

Only the backend application should be accessible from the host.
The data service must remain internal to the Docker network
and should be accessed by the backend using Docker DNS rather than an IP address.

Verify the complete request flow by sending an HTTP request with `curl` from the host
to the backend application and confirming that the response contains data 
obtained from the data service and processed by backend.

### Building and Checking Data Service

1. 
    ```console
    $ docker image build -t data-service-image ./data-service
    ```

2. 
    ```console
    $ docker image ls data-service-image
                                                                                                    i Info →   U  In Use
    IMAGE                       ID             DISK USAGE   CONTENT SIZE   EXTRA
    data-service-image:latest   cc4ba231463c        167MB             0B  
    ```

3. 
   ```console
   $ docker container run -d \
     --name data-service \
     -p 8000:8000 \
     data-service-image
   8c158cc8055c1e67b3c9446b42a3aa4595f7c96e1d2d03939fa45db206ffc6c8
   ```

4. 
  ```console
  $ curl http://localhost:8000/books/1 ; echo
  {"id":1,"title":"Learning Docker in one Semester","author":"Ridley Bibber","price":40.0}
  ```

5.
  ```console
  $ curl http://localhost:8000/books/3 ; echo
  {"detail":"Book not found"}
  ```

6.
  ```console
  $ docker container rm -f data-service
  data-service
  ```

### Building Backend

1. 
    ```console
    $ docker image build -t backend-image ./backend
    ```

2. 
    ```console
    $ docker image ls backend-image
                                                                                                    i Info →   U  In Use
    IMAGE                  ID             DISK USAGE   CONTENT SIZE   EXTRA
    backend-image:latest   aee9e9979583        168MB             0B 
    ```

### Running and Checking Containers in a Network

1. 
    ```console
    $ docker network create lab-net
    082afdeccab44d6c6020df0476a12aebc37fa13799d41705c08b8441946a5e7c
    ```

2. 
    ```console
    $ docker container run -d \
      --name data-service \
      --network lab-net \
      data-service-image
    a855a2b95051b94340326545f6be518e566d9d2dc9d63a6a0734344d41c88dde
    ```

3. 
    ```console
    $ docker container run -d \
      --name backend \
      --network lab-net \
      -p 8000:8000 \
      backend-image
    0f8bcc7b902d56bf42d9b123fd35f395adbf1550d0d1c79d185c2d03dd028c3e
    ```

4.
    ```console
    $ curl http://localhost:8000/books/1 ; echo
    {"id":1,"title":"Learning Docker in one Semester","author":"Ridley Bibber","price":40.0,"price_with_tax":48.0}
    ```
   
    ```console
    $ curl http://localhost:8000/books/2 ; echo
    {"id":2,"title":"Learning Python in one Semester","author":"Taylor Travolta","price":30.0,"price_with_tax":36.0}
    ```
   
    ```console
    $ curl http://localhost:8000/books/3 ; echo
    {"detail":"Book not found"}
    ```
   
    ```console
    $ docker container rm -f backend
    backend
    ```
    
    ```console
    $ docker container rm -f data-service
    data-service
    ```
    
    ```console
    $ docker network rm lab-net
    lab-net
    ```