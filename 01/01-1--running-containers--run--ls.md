# Running Containers

- Pull the `diamol/ch02-hello-diamol:2e` image from Docker Hub and run a container from that image
    ```console
    $ docker run diamol/ch02-hello-diamol:2e
    Unable to find image 'diamol/ch02-hello-diamol:2e' locally
    2e: Pulling from diamol/ch02-hello-diamol
    0a9a5dfd008f: Pull complete 
    57ea1b951e90: Pull complete 
    3cf9c52824b0: Pull complete 
    Digest: sha256:126be15c1b2a48761f874dfbb986669fe44c4ff746dbfbbfd90a40041e389d99
    Status: Downloaded newer image for diamol/ch02-hello-diamol:2e
    ---------------------
    Hello from Chapter 2!
    ---------------------
    My name is:
    d8d35c96daca
    ---------------------
    Im running on:
    Linux 6.8.0-124-generic x86_64
    ---------------------
    My address is:
    inet addr:172.17.0.2 Bcast:172.17.255.255 Mask:255.255.0.0
    ---------------------
    ```

- Repeat the command
  ```console
  $ docker run diamol/ch02-hello-diamol:2e
  ---------------------
  Hello from Chapter 2!
  ---------------------
  My name is:
  52be98857905
  ---------------------
  Im running on:
  Linux 6.8.0-124-generic x86_64
  ---------------------
  My address is:
  inet addr:172.17.0.2 Bcast:172.17.255.255 Mask:255.255.0.0
  ---------------------
  ```

- A container runs as long as its main application process is running.
  When that process exits, the container stops.
  ```
  Container starts
    ↓
  Application process runs
    ↓
  Application process exits
    ↓
  Container stops
  ```
  
- The stopped container still exists and can be shown with `docker container ls -a`.

  ```console
  $ docker container ls
  CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
  $ docker container ls -a
  CONTAINER ID   IMAGE                         COMMAND                 CREATED         STATUS                     PORTS     NAMES
  52be98857905   diamol/ch02-hello-diamol:2e   "/bin/sh -c ./cmd.sh"   5 minutes ago   Exited (0) 5 minutes ago             magical_leavitt
  d8d35c96daca   diamol/ch02-hello-diamol:2e   "/bin/sh -c ./cmd.sh"   22 hours ago    Exited (0) 22 hours ago              jolly_fermi
  ```
