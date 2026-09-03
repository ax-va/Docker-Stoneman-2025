# Docker-Stoneman-2025

## Source Code

https://github.com/sixeyed/diamol/tree/2e

## Docker

https://hub.docker.com/

## Windows and macOS

See the installation of Docker Desktop on Windows and macOS

https://www.docker.com/products/docker-desktop/

## Linux 

See the installation of Docker Desktop on Linux

https://docs.docker.com/desktop/setup/install/linux/

On Linux, you need only Docker CLI (client), Docker Engine (server), and Docker Compose.

- Show the Docker CLI version

    ```console
    $ docker --version
    Docker version 29.6.1, build 8900f1d
    ```

- Show detailed version information about both the Docker client and server

    ```console
    $ docker version
    Client: Docker Engine - Community
     Version:           29.6.1
     API version:       1.55
     Go version:        go1.26.4
     Git commit:        8900f1d
     Built:             Fri Jun 26 11:40:26 2026
     OS/Arch:           linux/amd64
     Context:           default
    
    Server: Docker Engine - Community
     Engine:
      Version:          29.6.1
      API version:      1.55 (minimum version 1.40)
      Go version:       go1.26.4
      Git commit:       8ec5ab3
      Built:            Fri Jun 26 11:40:26 2026
      OS/Arch:          linux/amd64
      Experimental:     false
     containerd:
      Version:          v2.2.5
      GitCommit:        e53c7c1516c3b2bff98eb76f1f4117477e6f4e66
     runc:
      Version:          1.3.6
      GitCommit:        v1.3.6-0-g491b69ba
     docker-init:
      Version:          0.19.0
      GitCommit:        de40ad0
    ```

- Show the current Docker environment

    ```console
    $ docker info
    Client: Docker Engine - Community
     Version:    29.6.1
     Context:    default
     Debug Mode: false
     Plugins:
      buildx: Docker Buildx (Docker Inc.)
        Version:  v0.35.0
        Path:     /usr/libexec/docker/cli-plugins/docker-buildx
      compose: Docker Compose (Docker Inc.)
        Version:  v5.2.0
        Path:     /usr/libexec/docker/cli-plugins/docker-compose
    
    ...
    ```

- Show the version of Docker Compose

    ```console
    $ docker compose version
    Docker Compose version v5.2.0
    ```

## Commands

### Containers

- Show only running containers (`ls`)
  ```console
  $ docker container ls
  CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
  ```

- Show all containers (`ls`, `-a`, `--all`)
  ```console
  $ docker container ls -a
  ```

- Show all containers (`ls`, `-a`, `--all`), only their IDs (`-q`, `--quiet`)  
  ```console
  $ docker container ls -aq
  ```

- Remove containers (`rm`), force-removing running containers (`-f`, `--force`)
  ```console
  $ docker container rm -f $(docker container ls -aq)
  ```

#### Copy Files Between a Container and the Host

`docker container cp` copies files or directories between a container and the host filesystem.

The command works in both directions.
The container does not need to be running, but it must exist.

- Container → host
    ```console
    $ docker container cp <container>:<source-path> <host-destination-path>
    ```

- Host → container
    ```console
    $ docker container cp <host-source-path> <container>:<destination-path>
    ```

Here `<container>` can be a container name, a full container ID, or a unique prefix of the container ID.

#### Attach to a Container

`-a` (`--attach`) attaches the terminal to the container's standard output 
and standard error streams when the container is started, 
so the output of the container's main process is displayed in the terminal.

```console
$ docker container start -a <container>
```

With `docker run <container>`, `STDOUT` and `STDERR` are attached by default
unless the container is started in detached mode (`-d`, `--detach`),
so `-a` is usually unnecessary.

Note:
- `-a` (`--attach`) - attaches the specified standard streams (`STDIN`, `STDOUT`, or `STDERR`) to the terminal.
- `-i` (`--interactive`) - keeps the container's `STDIN` open even if it is not attached.
They are ofen used together when interactive input is required.

### Images

- Show all images (`ls`)
  ```console
  $ docker image ls
  IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTR
  ```

- Show images (`ls`), filtered (`-f`, `--filter`) by reference (`reference='axvadev/*'`), 
  only their IDs (`-q`, `--quiet`)  
  ```console
  $ docker image ls -f reference='axvadev/*' -q
  ```

- Find the images matching `axvadev/*` and remove them (`-rm`), forcing removal when necessary (`-f`, `--force`)
  ```console
  $ docker image rm -f $(docker image ls -f reference='axvadev/*' -q)
  ```

- Find an existing image by its reference and assign a new reference to the same image
  ```console
  $ docker image tag hello-from-rust <docker-id>/hello-from-rust:v1
  ```
  Both references now point to the same image ID.

### Multiple Filters

A Docker command can contain multiple `--filter` options.
Multiple filters with different keys are generally combined as `AND`,
while multiple values for the same keys can act as `OR`:

- `AND`
  ```console
  $ docker container ls \
    --filter status=running \
    --filter name=app
  ```

- `OR`
  ```console
  $ docker image ls \
    --filter reference=diamol/golang:2e \
    --filter reference=image-gallery
  ```

### Restart Docker Daemon after Changing Settings

  - Windows
    ```console
    > Restart-Service docker
    ```

  - Linux
    ```console
    $ sudo systemctl restart docker
    ```

### How to Run a Local Docker Registry

  ```console
  $ docker container run -d \
    -p 5010:5000 \
    --restart always \
    --name local-registry \
    registry:3
  ...
  012d1244ae2fbf577c7be4b43c85d88079e64eb0f9e3c8eac8c448c7dde6a7d3
  ```

  - `docker container run` creates and starts a new container;
  - `-d` (`--detach`) runs the container in the background;
  - `-p 5010:5000` (`--publish`) maps port `5010` on the host to port `5000` inside the container;
  - `--restart always` automatically restarts the container if it stops or Docker restarts;
  - `--name local-registry` assigns the name `local-registry` to the container;
  - `registry:3` (`docker.io/library/register:3`) uses the Docker image to create the container.


    ```
    localhost:5010
      ↓
    host port 5010
      ↓
    container port 5000
      ↓
    Docker Registry
    ```

  - Container storage is ephemeral; persistent registry data should be stored in a volume.
  - Docker requires HTTPS for remote registers by default, but allows HTTP for `localhost` registries.
  - Using HTTP for a registry on `localhost` is generally acceptable for development
    because the traffic stays on the local machine.
    Remote or production registries should use HTTPS.
  - With `--restart always`, Docker automatically starts the container 
    when the Docker daemon starts, including after a Linux reboot.
    The Docker daemon itself must be running.