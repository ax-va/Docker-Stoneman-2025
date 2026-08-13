# Connecting to Containers

- The container provides the application with its own hostname, filesystem, 
  and usually network configuration (including an IP address), while sharing the host OS kernel 
  (e.g., the Linux kernel of your Ubuntu machine).
  ```
  Host
  hostname: <your-hostname>
  IP: <your-IP>
  |-- Docker
      |-- Container A
          hostname: 52be98857905
          IP: 172.17.0.2
      |-- Container B
          hostname: d8d35c96daca
          IP: 172.17.0.2
  ```

- We can start a container in *interactive mode* and enter its isolated environment to execute commands inside it.

  ```console
  $ docker run -it diamol/base:2e
  Unable to find image 'diamol/base:2e' locally
  2e: Pulling from diamol/base
  f18232174bc9: Pull complete 
  3c460918e200: Pull complete 
  Digest: sha256:9917cf89ca33be7b6cb70905865121b9d7f6b4d83cd26365d3f4c2583fc4c08d
  Status: Downloaded newer image for diamol/base:2e
  / # hostname
  5b43ddacccf3
  / # date
  Thu Aug 13 16:06:06 UTC 2026
  / # ls
  bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
  / # 
  ```

  Here 
  - `-i`, `--interactive` keeps the container's standard input (`stdin`) open;
  - `-t`, `--tty` allocates a pseudo-terminal (TTY).

- Run in the second terminal

    ```console
    $ docker container ls 
    CONTAINER ID   IMAGE            COMMAND     CREATED          STATUS          PORTS     NAMES
    5b43ddacccf3   diamol/base:2e   "/bin/sh"   12 minutes ago   Up 12 minutes             pensive_faraday
    ```
    
    ```console
    $ docker container top 5b
    UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
    root                399364              399339              0                   18:01               pts/0               00:00:00            /bin/sh
    ```
    
    ```console
    $ docker container logs 5b
    / # hostname
    5b43ddacccf3
    / # date
    Thu Aug 13 16:06:06 UTC 2026
    / # ls
    bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
    ```
    
    ```console
    $ docker container inspect 5b
    [
        {
            "Id": "5b43ddacccf3c21b5b477e41de425d20cfbfc8f55f35e73748af6909f87a20f8",
            "Created": "2026-08-13T16:01:01.705070478Z",
            "Path": "/bin/sh",
            "Args": [],
            "State": {
                "Status": "running",
                "Running": true,
                "Paused": false,
                "Restarting": false,
                "OOMKilled": false,
                "Dead": false,
                "Pid": 399364,
                "ExitCode": 0,
                "Error": "",
                "StartedAt": "2026-08-13T16:01:01.835158885Z",
                "FinishedAt": "0001-01-01T00:00:00Z"
            },
    ...
    ```

- Close the terminal session in the first terminal
    ```console
    $ / # exit
    ```