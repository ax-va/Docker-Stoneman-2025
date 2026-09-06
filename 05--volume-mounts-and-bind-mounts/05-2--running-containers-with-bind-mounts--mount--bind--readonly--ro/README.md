# Volume and Bind Mounts

## Running Containers with Bind Mounts

- Build the application image
    ```console
    $ docker image build -t bind-mount-demo-image .
    ```

- Run a container with the bind mount
    ```console
    $ docker container run --rm \
      --mount type=bind,source=$(pwd)/app/data,target=/data \
      bind-mount-demo-image
    Hello from bind mount!
    Run 1
    ```
  - The host directory `app/data` is mounted at `/data` inside the container.
  - The application accesses `/data/text.txt`, but the file is actually stored on the host.
  - When the application adds `Run <i>`, the host file is modified directly.
  - The container is removed after it exits because of `--rm`.
  - But the data remains because it is stored in the host filesystem rather than in the container's writable layer.


- A new container mounts the same host directory at `/data`.
    ```console
    $ docker container run --rm \
      --mount type=bind,source=$(pwd)/app/data,target=/data \
      bind-mount-demo-image
    Hello from bind mount!
    Run 1
    Run 2
    ```
  - It sees the changes made by the previous container and adds `Run 2`.
  - The modification is again immediately reflected in `app/data/text.txt` on the host.


- Run a new container with using `-v` (`--volume`) and the relative path to the host directory
  ```console
  $ docker container run --rm \
    -v ./app/data:/data \
    bind-mount-demo-image
  Hello from bind mount!
  Run 1
  Run 2
  Run 3
  ```


- A mount can be made read-only

    -
      ```console
      $ docker container run --rm \
        --mount type=bind,source=$(pwd)/app/data,target=/data,readonly \
        bind-mount-demo-image
      Traceback (most recent call last):
        File "/app/src/main.py", line 5, in <module>
          with file.open("r+") as f:
               ~~~~~~~~~^^^^^^
        File "/usr/local/lib/python3.13/pathlib/_local.py", line 537, in open
          return io.open(self, mode, buffering, encoding, errors, newline)
                 ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      OSError: [Errno 30] Read-only file system: '/data/text.txt'
      ```
  
    - 
      ```console
      $ docker container run --rm \
        -v ./app/data:/data:ro \
        bind-mount-demo-image
      Traceback (most recent call last):
      File "/app/src/main.py", line 5, in <module>
        with file.open("r+") as f:
             ~~~~~~~~~^^^^^^
      File "/usr/local/lib/python3.13/pathlib/_local.py", line 537, in open
        return io.open(self, mode, buffering, encoding, errors, newline)
               ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      OSError: [Errno 30] Read-only file system: '/data/text.txt'
      ```
    
    The read-only option can be used with both bind mounts and volume mounts.


- Note:
  - With `--mount type=bind`, `source` must be an absolute host path.
  - A shell expression such as `$(pwd)/app/data` can be used to construct the absolute path.
  - The `-v` (`--volume`) syntax also support relative host paths.