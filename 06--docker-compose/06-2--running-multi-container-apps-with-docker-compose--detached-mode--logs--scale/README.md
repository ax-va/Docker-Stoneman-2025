# Docker Compose

## Running Multi-Container Apps with Docker Compose

### Start and Stop the Application

```console
$ docker compose up --build
...
Attaching to app-1, data-service-1
Container 06-1--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-data-service-1 Waiting 
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:49] "GET /health HTTP/1.1" 200 -
Container 06-1--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-data-service-1 Healthy 
data-service-1  | 172.18.0.3 - - [11/Sep/2026 21:35:50] "GET /data HTTP/1.1" 200 -
app-1           | Data 'fetched data' are fetched and saved in the volume.
app-1 exited with code 0                                                                                                                                                                                                            
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:51] "GET /health HTTP/1.1" 200 -
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:53] "GET /health HTTP/1.1" 200 -
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:55] "GET /health HTTP/1.1" 200 -
...
<Ctrl+C>
```

- `docker compose up` brings the application to the state described in the Compose file.

  It:
  - creates the required networks and volumes if they do not already exist;
  - creates and starts the service containers;
  - attaches to the containers and displays their logs.


- By default, `docker compose up` attaches to the service containers and displays their logs in the terminal.
Press `Ctrl+C` to stop the running services. 
Alternatively, you can stop the application in another terminal in the same directory with

  ```console
  $ docker compose stop
  ```

  Stopping the application this way does not remove its containers, networks, or volumes.


- The application can be started again with
  ```console
  $ docker compose start
  ```

- The `--build` option tells Compose to build the service images before starting the containers.
  Without `--build`, Compose can reuse already existing images instead of rebuilding them 
  after changes to the application source or Dockerfiles.

### Detached Mode and Logs

- The `-d` (`--detach`) option starts the service in the background and returns control of the terminal

    ```console
    $ docker compose up -d
    ```
    
    The application continues running after the command exits.


- The logs accumulated so far can be viewed separately with

    ```console
    $ docker compose logs
    ```

- To display only the last log line (`--tail=1`) of the `app` service, use

    ```console
    $ docker compose logs --tail=1 app
    ```

- To display the accumulated logs and continue displaying new log output as it os produced, 
  use the `-f` (`--follow`) option

    ```console
    $ docker compose logs -f
    ```
    
    `-f` (`--follow`) keeps the command running.

### Remove the Application

- Using

  ```console
  $ docker compose down
  [+] down 3/3
   ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-1          Removed                          0.0s
   ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-data-service-1 Removed                          0.0s
   ✔ Network 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale_app-net          Removed                          0.1s
  ```
  
  stops and removes the resources created for the Compose application. By default, it removes:
  - service containers;
  - Compose-managed networks.


- Named volumes are not removed by default, so persistent application data is preserved.
The following command with the `-v` (`--volumes`) option removes the named volumes as well
  ```console
  $ docker compose down -v
  [+] down 4/4
   ✔ Container 06-1--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-1          Removed                          0.0s
   ✔ Container 06-1--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-data-service-1 Removed                          0.0s
   ✔ Volume 06-1--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale_app-data          Removed                          0.0s
   ✔ Network 06-1--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale_app-net          Removed                          0.1s
  ```
  
  This removes:
  - service containers;
  - Compose-managed networks;
  - named volumes declared by the Compose application.


- Note:
  - Compose does not remove external networks or external volumes.
  - Resources declared with `external: true` are managed outside the Compose application.
  - Compose uses these resources but does not own their lifecycle,
    so they are not removed by `docker compose down`.
  - External volumes are preserved even when `-v` (`--volumes`) is specified.


### Scale

A Compose service describes how its containers should run,
but a service does not necessarily correspond to only one container.

- The same service can be scaled to multiple container instances

    ```console
    $ docker compose up -d --build --scale app=3
    ...
     ✔ Image 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-data-service       Built         1.8s
     ✔ Image 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app                Built         1.8s
     ✔ Network 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale_app-net          Created       0.0s
     ✔ Volume 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale_app-data          Created       0.0s
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-data-service-1 Healthy       2.7s
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-3          Started       2.9s
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-1          Started       3.1s
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-2          Started       2.8s
    ```
  Here:
  - `--scale app=3` - sets the number of running container instances for `app` service to `3`;
  - all instances are created from the same service definition and use the same image and configuration.


- Logs can still be requested by the service name

    ```console
    $ docker compose logs --tail=1 app
    app-1  | Data 'fetched data' are fetched and added to the volume.
    app-2  | Data 'fetched data' are fetched and added to the volume.
    app-3  | Data 'fetched data' are fetched and added to the volume.
    ```
  Compose collects the logs from all containers belonging to the `app` service.
  With `--tail=1`, it displays the last log line from each container.


- Scaling can also be reduced
    ```console
    $ docker compose up -d --scale app=1
    [+] up 4/4
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-data-service-1 Healthy       0.5s
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-2          Removed       0.0s
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-3          Removed       0.0s
     ✔ Container 06-2--running-multi-container-apps-with-docker-compose--detached-mode--logs--scale-app-1          Started       0.1s
    ```
  Compose removes the extra container instances and ensure 
  that the requested number of containers for the `app` service is running.
  In this examole, `app-2` and `app-3` are removed, while the existing stopped `app-1` is started again.


- Note:
  - Compose changes the number of container instances to match the requested scale.
  - When scaling up, existing running containers remain running 
    and Compose creates additional containers to reach the requested scale.
  - When scaling down, Compose removes the extra container instances.
  - If an existing container that should remain is stopped, Compose starts it again to reach the requested scale.