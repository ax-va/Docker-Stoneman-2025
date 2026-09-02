# Volume and Bind Mounts

## Running Containers with Docker Volumes

- Build the application image
    ```console
    $ docker image build -t volume-demo-image .
    ```

- Create an empty named volume
    ```console
    $ docker volume create demo-volume
    demo-volume
    ```
  At this point, `demo-volume` is empty.


- List all existing volumes
    ```console
    $ docker volume ls
    DRIVER    VOLUME NAME
    local     demo-volume
    ```

- Run a container, mount the volume at `/data` inside the container,
  and automatically remove the container when it exits
    ```console
    $ docker container run --rm \
      --mount type=volume,source=demo-volume,target=/data \
      volume-demo-image
    Hello from volume!
    Run 1
    ```
  - Because `demo-volume` was empty and `/data` already contains `text.txt` in the container filesystem,
    Docker copies the existing contents of `/data` into the volume.
  - The application then adds `Run 1` to `/data/text.txt`.
  - The container exists and is automatically removed because of `--rm`,
    but the volume exists independently and retains the modified file.


- Run another new container using the same volume
    ```console
    $ docker container run --rm \
      --mount type=volume,source=demo-volume,target=/data \
      volume-demo-image
    Hello from volume!
    Run 1
    Run 2
    ```
  - The volume is no longer empty, so Docker does not copy the initial `/data` contents into it again.
  - The new container sees the data previously stored in `demo-volume`, and the application adds `Run 2`.


- Finally, remove the volume
    ```console
    $ docker volume rm demo-volume
    demo-volume
    ```
  Removing the volume also removes the data stored in it.