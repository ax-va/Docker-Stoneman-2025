# Docker Compose

## Docker Compose File, Dependencies, Health Checks

The file defines two services, one network, and one named volume

```yaml
services:
  app:
    build:
      context: ./app
    networks:
      - app-net
    volumes:
      - app-data:/data
    depends_on:
      data-service:
        condition: service_healthy

  data-service:
    build:
      context: ./data-service
    networks:
      - app-net
    healthcheck:
      test:
        [
          "CMD",
          "python",
          "-c",
          "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
        ]
      interval: 2s
      timeout: 1s
      retries: 10

networks:
  app-net:

volumes:
  app-data:
```

- `services`

    The `services` section defines the application components that Compose manages.
    
    In this application, there are two services:
    
    - `app` - fetches data from `data-service` and stores the result;
    - `data-service` - runs an HTTP server that provides the data.

    A service is a Compose-level definition. Compose creates containers to run services.


- `build`

  `build` tells Compose to build an image for the service.

  `context` specifies the Docker build context. The path is relative to the directory containing the Compose file.

  For example:
  ```yaml
  build:
    context: ./app
  ```
  uses `./app` as the build context and, by default, uses the `Dockerfile` located in that directory.

  The same applies to `data-service`:
  ```yaml
  build:
    context: ./data-service
  ```
  
  When running
  ```console
  $ docker compose up --build
  ```
  Compose builds the required images before starting the containers.


- `networks`

  Both services are connected to the same Compose network
  ```yaml
  networks:
    - app-net 
  ```
  The network itself is declared at the top level
  ```yaml
  networks:
    app-net:
  ```
  Because the network is managed by Compose, Compose creates it automatically when the application is started.

  Services connected to the same Compose network can reach each other using their service names as DNS hostnames.

  Therefore, `app` can access
  ```
  http://data-service:8000/data
  ```
  Here:
  -  `data-service` is the Compose service name and acts as the hostname;
  -  `8000` is the port on which the application inside the `data-service` container listens.

  Compose-managed networks are created automatically when the application is started.

  The following command removes the service containers and the networks created by Compose
  ```console
  $ docker compose down
  ```


- `volumes`
  
  The `app` service mounts a nemed volume
  ```yaml
  volumes:
    - app-data:/data
  ```
  Here:
  - `app-data` is the named Docker volume;
  - `/data` is the mount point inside the `app` container.
  
  The volume itself is declared at the top level
  ```yaml
  volumes:
    app-data:
  ```
  Compose creates the volume when it is needed.

  Therefore, the data can survive the removal and recreation of the `app` container.


- `healthcheck`

  The `data-service` service defines a health check
  ```yaml
  healthcheck:
  test:
    [
      "CMD",
      "python",
      "-c",
      "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
    ]
  interval: 2s
  timeout: 1s
  retries: 10
  ```
  The health check is executed inside the `data-service` container.

  - The command
    ```console
    python -c "..."
    ```
    runs a short Python program that sends an HTTP request to `http://localhost:8000/health`.
    - `localhost` refers to the `data-service` container itself.

    - If the request succeeds, the health check succeeds.

  The options control how docker performs the check:
  - `interval: 2s` - runs the health check every 2 seconds;
  - `timeout: 1s` - considers an individual check failed if it takes longer than 1 second;
  - `retries: 10` - marks the container as unhealthy after 10 consecutive failed checks.
  
  Health checks continue to run after the container becomes healthy.
  They are not only startup checks.


- `depends_on`

  The `app` service depends on `data-service`
  ```yaml
  depends_on:
    data-service:
      condition: service_healthy
  ```
  This tells Compose not to start the `app` service until `data-service` has passed its health check.

  This is different from the short form
  ```yaml
  depends_on:
    - data-service
  ```
  The short form defines the startup order: Compose starts `data-service` before `app`, 
  but it does not check whether `data-service` is healthy or ready to accept requests.

  Using
  ```yaml
  condition: service_healthy
  ```
  makes Compose wait until the dependency passes its `healthcheck` before starting the dependent service.
