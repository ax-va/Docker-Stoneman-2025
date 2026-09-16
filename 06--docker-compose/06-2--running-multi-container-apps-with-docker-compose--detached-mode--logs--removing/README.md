# Docker Compose

## Running Multi-Container Apps with Docker Compose

### Start and Stop the Application

```console
$ docker compose up --build
...
Attaching to app-1, data-service-1
Container 06-1--running-multi-container-apps-with-docker-compose-data-service-1 Waiting 
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:49] "GET /health HTTP/1.1" 200 -
Container 06-1--running-multi-container-apps-with-docker-compose-data-service-1 Healthy 
data-service-1  | 172.18.0.3 - - [11/Sep/2026 21:35:50] "GET /data HTTP/1.1" 200 -
app-1           | Data 'fetched data' are fetched and saved in the volume.
app-1 exited with code 0                                                                                                                                                                                                            
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:51] "GET /health HTTP/1.1" 200 -
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:53] "GET /health HTTP/1.1" 200 -
data-service-1  | 127.0.0.1 - - [11/Sep/2026 21:35:55] "GET /health HTTP/1.1" 200 -
...
<Ctrl+C>
```

`docker compose up` brings the application to the state described in the Compose file.

It:
- creates the required networks and volumes if they do not already exist;
- creates and starts the service containers;
- attaches to the containers and displays their logs.

By default, `docker compose up` attaches to the service containers and displays their logs in the terminal.
Press `Ctrl+C` to stop the running services. 
Alternatively, you can stop the application in another terminal in the same directory with

```console
$ docker compose stop
```

Stopping the application this way does not remove its containers, networks, or volumes.

The application can be started again with
```console
$ docker compose start
```

The `--build` option tells Compose to build the service images before starting the containers.

Without `--build`, Compose can reuse already existing images instead of rebuilding them 
after changes to the application source or Dockerfiles.

### Detached Mode and Logs

The `-d` (`--detach`) option starts the service in the background and returns control of the terminal

```console
$ docker compose up -d
```

The application continues running after the command exits.

The logs accumulated so far can be viewed separately with

```console
$ docker compose logs
```

To display the accumulated logs and continue displaying new log output as it os produced, 
use the `-f` (`--follow`) option

```console
$ docker compose logs -f
```

`-f` (`--follow`) keeps the command running.

### Remove the Application

```console
$ docker compose down --volumes
[+] down 4/4
 ✔ Container 06-1--running-multi-container-apps-with-docker-compose-app-1          Removed                          0.0s
 ✔ Container 06-1--running-multi-container-apps-with-docker-compose-data-service-1 Removed                          0.0s
 ✔ Volume 06-1--running-multi-container-apps-with-docker-compose_app-data          Removed                          0.0s
 ✔ Network 06-1--running-multi-container-apps-with-docker-compose_app-net          Removed                          0.1s
```

`docker compose down` stops and removes the resources created for the Compose application.

By default, it removes:
- service containers;
- Compose-managed networks.

Named volumes are not removed by default, so persistent application data is preserved.

The following command removes the named volumes as well
```console
$ docker compose down --volumes
```

This removes:
- service containers;
- Compose-managed networks;
- named volumes declared by the Compose application.
