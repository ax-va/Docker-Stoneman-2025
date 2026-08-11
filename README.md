# Docker-Stoneman-2025

Original repository: https://github.com/sixeyed/diamol

## On Windows and macOS

See the installation of Docker Desktop on Windows and macOS

https://www.docker.com/products/docker-desktop/

## On Linux 

See the installation of Docker Desktop on Linux

https://docs.docker.com/desktop/setup/install/linux/

On Linux, you need only Docker CLI (client) and Docker Engine (server).

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

