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

### Images

- Show all images (`ls`)
  ```console
  $ docker image ls
  IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTR
  ```

- Show images (`ls`), filtered (`-f`, `--filter`) by reference (`reference='diamol/*'`), only their IDs (`-q`, `--quiet`)  
  ```console
  $ docker image ls -f reference='diamol/*' -q
  ```

- Find the images matching `diamol/*` and remove them (`-rm`), forcing removal when necessary (`-f`, `--force`)
  ```console
  $  docker image rm -f $(docker image ls -f reference='diamol/*' -q)
  ```

### Multiple Filters

  A Docker command can contain multiple `--filter` options.
  Multiple filters with different keys are generally combined as `AND`,
  while multiple values for the same keys can act as `OR`:

  - 
    ```console
    $ docker container ls \
      --filter status=running \
      --filter name=app
    ```

  - 
    ```console
    $ docker image ls \
      --filter reference=diamol/golang:2e \
      --filter reference=image-gallery
    ```
