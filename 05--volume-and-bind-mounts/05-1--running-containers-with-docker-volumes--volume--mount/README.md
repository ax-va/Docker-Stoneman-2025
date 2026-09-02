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

- Display detailed information about the volume, including its name, driver, creation time,
  and mount point on the Docker host
    ```console
     docker volume inspect demo-volume
    [
        {
            "CreatedAt": "2026-09-02T23:08:22+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/demo-volume/_data",
            "Name": "demo-volume",
            "Options": null,
            "Scope": "local"
        }
    ]
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


- Note 1:
  - As an *image author*, the `VOLUME <target-path>` instruction in a Dockerfile can be used 
    as a fail-safe for directories containing persistent application data. 
    If the user does not explicitly provide a mount for that path,
    Docker creates an anonymous volume.
  - As an *image user*, it is generally better to explicitly manage storage with named volumes 
    instead of relying on automatically created anonymous volumes.


- Note 2:
  - Although a volume can be shared between multiple containers,
    this does not mean that it is always safe to use it concurrently.
  - If multiple containers read and write the same files at the same time,
    this can cause conflicts, data corruption, or application-specific problems.
  - A common use of volumes is to *preserve application state when replacing or upgrading a container*.


- Note 3:
  - Removing a container does not normally remove its volumes.
  - However, `docker container run --rm` also removes anonymous volumes 
    created for the container when the container is automatically removed.
  - Named volumes are not removed by `--rm`.
