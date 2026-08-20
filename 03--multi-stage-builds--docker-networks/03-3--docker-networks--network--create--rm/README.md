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
    [+] Building 10.9s (8/8) FINISHED                                                                                             docker:default
     => [internal] load build definition from Dockerfile                                                                                    0.0s
     => => transferring dockerfile: 128B                                                                                                    0.0s 
     => [internal] load metadata for docker.io/library/python:3.12-slim                                                                     2.2s 
     => [internal] load .dockerignore                                                                                                       0.0s
     => => transferring context: 2B                                                                                                         0.0s 
     => [1/3] FROM docker.io/library/python:3.12-slim@sha256:2c941e860699f878900b0edc2403613c234d4b32eda3cc9fa7036991a2a63c4a               8.2s 
     => => resolve docker.io/library/python:3.12-slim@sha256:2c941e860699f878900b0edc2403613c234d4b32eda3cc9fa7036991a2a63c4a               0.0s
     => => sha256:613c5454f914638dc2bfcab71c8630de0089f7ebff0a7239b54f34866c4b6051 5.66kB / 5.66kB                                          0.0s 
     => => sha256:26c307b5e35a59ce911f5fde5b9458120ec8734e831ea2da5649a9ad14abfd3d 29.78MB / 29.78MB                                        5.6s 
     => => sha256:fa18dfb1257a9c1afc75e233c55b0195dd02b8d6d18dd7e24c10238b039e7742 1.29MB / 1.29MB                                          1.5s
     => => sha256:b952fe9f6810de5dac5d24a3983aee5fce3884f7359a533ba325e48ecb745994 12.12MB / 12.12MB                                        1.4s
     => => sha256:2c941e860699f878900b0edc2403613c234d4b32eda3cc9fa7036991a2a63c4a 10.37kB / 10.37kB                                        0.0s
     => => sha256:876416ecde9aca2bcc90e1fb0c7a9500bbf749f5788b70f82d4c5a5c2357f8b4 1.75kB / 1.75kB                                          0.0s 
     => => sha256:6760bfe2ff00c4530bc73b2f88a1e9615a56c9a77028f41f8bb4b978d08b8439 248B / 248B                                              1.6s 
     => => extracting sha256:26c307b5e35a59ce911f5fde5b9458120ec8734e831ea2da5649a9ad14abfd3d                                               1.3s 
     => => extracting sha256:fa18dfb1257a9c1afc75e233c55b0195dd02b8d6d18dd7e24c10238b039e7742                                               0.1s 
     => => extracting sha256:b952fe9f6810de5dac5d24a3983aee5fce3884f7359a533ba325e48ecb745994                                               0.8s 
     => => extracting sha256:6760bfe2ff00c4530bc73b2f88a1e9615a56c9a77028f41f8bb4b978d08b8439                                               0.0s 
     => [internal] load build context                                                                                                       0.0s 
     => => transferring context: 894B                                                                                                       0.0s 
     => [2/3] WORKDIR /app/src                                                                                                              0.4s 
     => [3/3] COPY src/main.py .                                                                                                            0.0s 
     => exporting to image                                                                                                                  0.0s 
     => => exporting layers                                                                                                                 0.0s 
     => => writing image sha256:90de7c719ceca8386a932169845cabd62e213c69fc721622f2d363692b749d28                                            0.0s 
     => => naming to docker.io/library/data-service-image                                                                                   0.0s
    ```

- Run a data-service container in the background, connect it to the Docker network
    ```console
    $ docker container run -d --name data-service --network my-net data-service-image
    67f0d88705b860bc22524cdcd8b73ba35ba701799a2368000b7c7f20ce185fbd
    ```

- Build the application image
    ```console
    $ docker image build -t app-image ./app
    [+] Building 5.2s (10/10) FINISHED                                                                                            docker:default
     => [internal] load build definition from Dockerfile                                                                                    0.0s
     => => transferring dockerfile: 201B                                                                                                    0.0s
     => [internal] load metadata for docker.io/library/python:3.12-slim                                                                     0.7s
     => [internal] load .dockerignore                                                                                                       0.0s
     => => transferring context: 2B                                                                                                         0.0s
     => [1/5] FROM docker.io/library/python:3.12-slim@sha256:2c941e860699f878900b0edc2403613c234d4b32eda3cc9fa7036991a2a63c4a               0.0s
     => [internal] load build context                                                                                                       0.0s
     => => transferring context: 128B                                                                                                       0.0s
     => CACHED [2/5] WORKDIR /app/src                                                                                                       0.0s
     => CACHED [3/5] COPY requirements.txt /app                                                                                             0.0s
     => [4/5] RUN pip install --no-cache-dir -r /app/requirements.txt                                                                       4.1s
     => [5/5] COPY src .                                                                                                                    0.0s 
     => exporting to image                                                                                                                  0.2s 
     => => exporting layers                                                                                                                 0.2s 
     => => writing image sha256:e0ed39ea4343f92c427919770daee131d774c734d799458f730b7f3d3bc6962f                                            0.0s 
     => => naming to docker.io/library/app-image                                                                                            0.0s 
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