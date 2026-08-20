# Docker Networks

- A *Docker network* allows containers to communicate with each other.

- Containers connected to the same user-defined Docker network can reach each other using
  *container names* instead of IP addresses.

- Docker provides an internal *DNS service* 
  that resolves a container name to its IP address inside the network.

## Example: Container-to-Container Communication

- Create a Docker network
    ```console
    $ docker network create my-net
    6580bcd8c7f185fa22f8b78b60b02d6745e6d55ec5799736979718dd100b3010
    ```

- Build the data service image
    ```console
    $ docker image build -t data-service-image ./data-service
    ```

- Run a data-service container in the background, connect it to the Docker network
    ```console
    $ docker container run -d --name data-service --network my-net data-service-image
    67f0d88705b860bc22524cdcd8b73ba35ba701799a2368000b7c7f20ce185fbd
    ```

- Build the application image
    ```console
    $ docker image build -t app-image ./app
    ```

- Run an application container, connect it to the Docker network
    ```console
    $ docker container run --rm --name app --network my-net app-image
    fetched data
    ```

- Force-remove the first container
    ```console
    $ docker container rm -f data-service
    data-service
    ```

- Remove the Docker network
  ```console
  $ docker network rm my-net
  my-net
  ```


### How Containers Communicate Through a Docker Network
    ```
    app container
      ↓
    HTTP request: GET http://data-service:8000/data
      ↓
    Docker DNS
      ↓  
    "data-service" → IP address of the data-service container in the Docker network
      ↓
    data-service container
      ↓
    port 8000
      ↓
    GET /data
      ↓
    `main.py` in the data-service container handels the request
      ↓
    HTTP response: "fetched data"
      ↓ 
    app receives the response
      ↓
    `repository.py` in the app container returns "fetched data"
      ↓ 
    `main.py` in the app conatiner prints "fetched data"
      ↓ 
    console
    ```

## Docker Compose

- *Docker Compose* is used to define and manage multi-container applications.

- Instead of manually creating networks and starting each container with separate Docker commands,
  the application services, networks, volumes, environment variables, ports, and other configuration
  can be described in a `compose.yaml` file and managed together.

- Docker Compose does not replace Docker networks.
  By default, Compose creates a network for the application and connects its services to that network,
  allowing them to communicate using service names.