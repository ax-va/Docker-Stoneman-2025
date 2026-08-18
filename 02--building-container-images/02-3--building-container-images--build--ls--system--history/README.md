# Building Container Images

## Example

  - Build the image
    ```console
    $ docker image build --tag web-ping .
    [+] Building 4.4s (8/8) FINISHED                                                                                        docker:default
     => [internal] load build definition from Dockerfile                                                                              0.0s
     => => transferring dockerfile: 175B                                                                                              0.0s
     => [internal] load metadata for docker.io/diamol/node:2e                                                                         4.1s
     => [internal] load .dockerignore                                                                                                 0.0s
     => => transferring context: 2B                                                                                                   0.0s
     => [1/3] FROM docker.io/diamol/node:2e@sha256:4f5efb088512c840cc8c842b6052661425b24f8c44b0f025c0f831c21705a5d4                   0.1s
     => => resolve docker.io/diamol/node:2e@sha256:4f5efb088512c840cc8c842b6052661425b24f8c44b0f025c0f831c21705a5d4                   0.0s
     => => sha256:4f5efb088512c840cc8c842b6052661425b24f8c44b0f025c0f831c21705a5d4 1.81kB / 1.81kB                                    0.0s
     => => sha256:8f67eef21d75ff5a62cb40393f4a8e0b27ba3fdfa821a0df27c47d5215fb2091 1.16kB / 1.16kB                                    0.0s
     => => sha256:1780bb44a8c73589218241cbae4330fe7783f5f9dcc85bf5aea12f73190bd78e 6.50kB / 6.50kB                                    0.0s
     => [internal] load build context                                                                                                 0.0s
     => => transferring context: 912B                                                                                                 0.0s
     => [2/3] WORKDIR /app                                                                                                            0.0s
     => [3/3] COPY app .                                                                                                              0.0s
     => exporting to image                                                                                                            0.0s
     => => exporting layers                                                                                                           0.0s
     => => writing image sha256:52686672da09335f8d10d71ba72913c0073b2391f08b3e527c03b5f4d35e1d1a                                      0.0s
     => => naming to docker.io/library/web-ping                                                                                       0.0s
    ```

- Check whether the image is available locally:
    ```console
    $ docker image ls
                                                                                                                  i Info →   U  In Use
    IMAGE                             ID             DISK USAGE   CONTENT SIZE   EXTRA
    diamol/base:2e                    2b8ea8bae293       12.8MB             0B        
    diamol/ch02-hello-diamol-web:2e   bfce3f6fc117       63.8MB             0B    U   
    diamol/ch02-hello-diamol:2e       913b56a07a3a        7.8MB             0B        
    diamol/ch03-web-ping:2e           a7e429b1053c        156MB             0B    U   
    web-ping:latest                   52686672da09        156MB             0B  
    ```
  
  The `SIZE` column is the *logical size* of the image - the total size of its filesystem content.
  Because images layers can be shared between images, 
  the additional physical disk space used by this image may be smaller.

- Show images disk usage

  ```console
  $ docker system df
  TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
  Images          5         3         232.5MB   12.74MB (5%)
  Containers      3         0         25B       25B (100%)
  Local Volumes   9         0         789.4MB   789.4MB (100%)
  Build Cache     9         0         1.828kB   982B
  ```
  
  ```console
  $ docker system df -v
  Images space usage:
  
  REPOSITORY                     TAG       IMAGE ID       CREATED             SIZE      SHARED SIZE   UNIQUE SIZE   CONTAINERS
  web-ping                       latest    52686672da09   About an hour ago   156MB     156MB         846B          1
  diamol/ch02-hello-diamol-web   2e        bfce3f6fc117   17 months ago       63.8MB    7.834MB       55.96MB       1
  diamol/ch03-web-ping           2e        a7e429b1053c   17 months ago       156MB     156MB         846B          1
  diamol/base                    2e        2b8ea8bae293   17 months ago       12.8MB    7.834MB       4.94MB        0
  diamol/ch02-hello-diamol       2e        913b56a07a3a   17 months ago       7.8MB     0B            7.805MB       0

  ...
  ```
  - `docker system df -v` shows images and their disk usage, not the individual image layers.
  - `SHARED SIZE` is the size of image data also used by other images.
  - `UNIQUE SIZE` is the size of image data used only by this image.
  -  Docker stores shared layers only once, which reduces actual disk usage.


- List images whose repository name starts with 'w'
  ```console
  $ docker image ls 'w*'
                                                                                                                 i Info →   U  In Use
  IMAGE             ID             DISK USAGE   CONTENT SIZE   EXTRA
  web-ping:latest   52686672da09        156MB             0B 
  ```

- Run a container from the built image
  ```console
  $ docker container run -e TARGET=docker.com -e INTERVAL=5000 web-ping
  ** web-ping ** Pinging: docker.com; method: HEAD; 5000ms intervals
  Making request number: 1; at 1786792678887
  Got response status: 301 at 1786792679065; duration: 178ms
  ```
  Stop with `CTRL+C`.


- Show the history of instructions that contributed to the image
  ```console
  $ docker image history web-ping
  IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
  52686672da09   27 minutes ago   CMD ["node" "/app/app.js"]                      0B        buildkit.dockerfile.v0
  <missing>      27 minutes ago   COPY app . # buildkit                           846B      buildkit.dockerfile.v0
  <missing>      27 minutes ago   WORKDIR /app                                    0B        buildkit.dockerfile.v0
  <missing>      27 minutes ago   ENV INTERVAL=3000                               0B        buildkit.dockerfile.v0
  <missing>      27 minutes ago   ENV METHOD=HEAD                                 0B        buildkit.dockerfile.v0
  <missing>      27 minutes ago   ENV TARGET=blog.sixeyed.com                     0B        buildkit.dockerfile.v0
  <missing>      2 years ago      CMD ["node"]                                    0B        buildkit.dockerfile.v0
  <missing>      2 years ago      ENTRYPOINT ["docker-entrypoint.sh"]             0B        buildkit.dockerfile.v0
  <missing>      2 years ago      COPY docker-entrypoint.sh /usr/local/bin/ # …   388B      buildkit.dockerfile.v0
  <missing>      2 years ago      RUN /bin/sh -c apk add --no-cache --virtual …   5.59MB    buildkit.dockerfile.v0
  <missing>      2 years ago      ENV YARN_VERSION=1.22.22                        0B        buildkit.dockerfile.v0
  <missing>      2 years ago      RUN /bin/sh -c addgroup -g 1000 node     && …   143MB     buildkit.dockerfile.v0
  <missing>      2 years ago      ENV NODE_VERSION=22.6.0                         0B        buildkit.dockerfile.v0
  <missing>      2 years ago      /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B        
  <missing>      2 years ago      /bin/sh -c #(nop) ADD file:99093095d62d04215…   7.8MB  
  ```
  A history entry does not necessarily correspond to a filesystem layer:

  - Instructions that modify the filesystem, such as `COPY`, `ADD`, and usually `RUN`
    produce filesystem changes stored in image layers.

  - Instructions such as `ENV`, `CMD`, `ENTRYPOINT`, and `WORKDIR` can modify the image configuration/metadata 
    without adding filesystem content.