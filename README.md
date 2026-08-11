# Docker-Stoneman-2025

Source code: https://github.com/sixeyed/diamol/tree/2e

## On Windows and macOS

See the installation of Docker Desktop on Windows and macOS

https://www.docker.com/products/docker-desktop/

## On Linux 

See the installation of Docker Desktop on Linux

https://docs.docker.com/desktop/setup/install/linux/

On Linux, you need only Docker CLI (client), Docker Engine (server), and Docker Compose.

- Show the Docker CLI version

    ```shell
    $ docker --version
    Docker version 29.6.1, build 8900f1d
    ```

- Show detailed version information about both the Docker client and server

    ```shell
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

    ```shell
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

    ```shell
    $ docker compose version
    Docker Compose version v5.2.0
    ```

## Commands

### Containers

- Show only running containers (`ls`)
  ```shell
  $ docker container ls
  CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
  ```

- Show all containers (`ls`, `-a`, `--all`)
  ```shell
  $ docker container ls -a
  ```

- Show all containers (`ls`, `-a`, `--all`), only their IDs (`-q`, `--quiet`)  
  ```shell
  $ docker container ls -aq
  ```

- Remove containers (`rm`), force-removing running containers (`-f`, `--force`)
  ```shell
  $ docker container rm -f $(docker container ls -aq)
  ```

### Images

- Show all images (`ls`)
  ```shell
  $ docker image ls
  IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTR
  ```

- Show images (`ls`), filtered (`-f`, `--filter`) by reference (`reference='diamol/*'`), only their IDs (`-q`, `--quiet`)  
  ```shell
  $ docker image ls -f reference='diamol/*' -q
  ```

- Find the images matching `diamol/*` and remove them (`-rm`), forcing removal when necessary (`-f`, `--force`)
  ```shell
  $  docker image rm -f $(docker image ls -f reference='diamol/*' -q)
  ```
