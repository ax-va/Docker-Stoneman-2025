# Running Containers

## Detached Mode and Hosting Websites

- Run a container in the background without attaching its `STDOUT` and `STDERR` (`-d`, `--detach`).
  Publish a container port by mapping a port on the host (your machine) 
  to a port inside the container (`-p <host-port>:<container-port>`, `--publish <host-port>:<container-port>`).

  ```console
  $ docker container run -d -p 8088:80 diamol/ch02-hello-diamol-web:2e
  Unable to find image 'diamol/ch02-hello-diamol-web:2e' locally
  2e: Pulling from diamol/ch02-hello-diamol-web
  f18232174bc9: Already exists 
  f6f8d7d49e24: Pull complete 
  aca02fb0fe83: Pull complete 
  4f4fb700ef54: Pull complete 
  da9bd0c8aef2: Pull complete 
  e7c0ad6e3e09: Pull complete 
  852b1f8ff649: Pull complete 
  d2d722b24a9c: Pull complete 
  Digest: sha256:c2e9d1f0c24dbb4efe432067d212b81ca9878e38fd315abb8d08dc0b3246955b
  Status: Downloaded newer image for diamol/ch02-hello-diamol-web:2e
  e57ac2c457fd2817406c68ba7083fa482264a5d2693e401357a6af31163ea40d
  ```

  Here `-p 8088:80` publishes port `80` of the container as port `8088` on the host: `Host:8088 ↔ Container:80`.
  Publishing a container port means Docker listens for network traffic on the computer port 
  and then sends it into the container, and vice versa.

- Show running containers
  
  ```console
  $ docker container ls
  CONTAINER ID   IMAGE                             COMMAND              CREATED              STATUS              PORTS                                     NAMES
  e57ac2c457fd   diamol/ch02-hello-diamol-web:2e   "httpd-foreground"   About a minute ago   Up About a minute   0.0.0.0:8088->80/tcp, [::]:8088->80/tcp   cranky_williamson
  ```

- Browse to http://localhost:8088 on a browser.


- Show live statistics

  ```console
  $ docker container stats e57a
  CONTAINER ID   NAME                CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O    PIDS
  e57ac2c457fd   cranky_williamson   0.01%     6.363MiB / 34.66GiB   0.02%     20.1kB / 2.41kB   0B / 4.1kB   109
  ```
  
  Here:
  - `CONTAINER_ID` - the unique identifier of the container (shown in shorted form);
  - `NAME` - the name assigned to the container;
  - `CPU %` - the percentage of CPU resources currently used by the container;
  - `MEM USAGE / LIMIT` - the amount of memory currently used by the container and its memory limit;
  - `MEM %` - the percentage of the available memory limit currently used by the container;
  - `NET I/O` - the amount of network data received and sent by the container (received/sent);
  - `BLOCK I/O` - the amount of data read from and written to block devices by the container (read/written);
  - `PIDS` - the number of processes/threads counted for the container.

  If no explicit memory limits is configured, the container can generally use the memory available to Docker/the host.

  A memory limit can be set explicitly with `--memory`

  ```console
  $ docker run --memory 512m <image>
  ```
  
  Exit stats with `Ctrl+C`.


- Stop the container

  ```console
  $ docker container stop e57a
  e57a
  ```

  ```console
  $ docker container ls
  CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
  ```

- Force-remove all containers
  ```console
  $ docker container rm --force $(docker container ls --all --quiet)
  e57ac2c457fd
  5b43ddacccf3
  52be98857905
  d8d35c96daca
  ```
