# Building Container Images

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

- Check the image in the local Docker Image Cache:
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
  List images whose repository name starts with 'w'
  ```console
  $ docker image ls 'w*'
                                                                                                                 i Info →   U  In Use
  IMAGE             ID             DISK USAGE   CONTENT SIZE   EXTRA
  web-ping:latest   52686672da09        156MB             0B 
  ```

- Run a container from the created and stored locally image
  ```console
  $ docker container run -e TARGET=docker.com -e INTERVAL=5000 web-ping
  ** web-ping ** Pinging: docker.com; method: HEAD; 5000ms intervals
  Making request number: 1; at 1786792678887
  Got response status: 301 at 1786792679065; duration: 178ms
  ```