# Sharing Images with Docker Hub and Other Registries

## Local Docker Registry

- Run a local Docker registry
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
    
    - Note 1: Container storage is ephemeral; persistent registry data should be stored in a volume.
    - Note 2: Docker requires HTTPS for remote registers by default, but allows HTTP for `localhost` registries.
    - Note 3: Using HTTP for a registry on `localhost` is generally acceptable for development
      because the traffic stays on the local machine.
      Remote or production registries should use HTTPS.


- Create a new image reference for the existing image
  ```console
  $ docker image tag axvadev/hello-from-rust:v1 localhost:5010/hello-from-rust:v1
  ```

- Push to the local Docker reigistry
  ```console
  $ docker image push localhost:5010/hello-from-rust:v1
  ```

- Find the image by reference
  ```console
  $ docker image ls --filter reference="*/hello-from-rust"
                                                                                                    i Info →   U  In Use
  IMAGE                               ID             DISK USAGE   CONTENT SIZE   EXTRA
  axvadev/hello-from-rust:v1          39064a5d2bf1       75.2MB             0B        
  localhost:5010/hello-from-rust:v1   39064a5d2bf1       75.2MB             0B  
  ```