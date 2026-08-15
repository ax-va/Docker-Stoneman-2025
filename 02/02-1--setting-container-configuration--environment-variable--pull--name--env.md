# Setting a Container Configuration Difficult from Its Image Configuration - an Environment Variable 

- Pull the `diamol/ch03-web-ping:2e` image form Docker Hub https://hub.docker.com/r/diamol/ch03-web-ping

    ```console
    $ docker image pull diamol/ch03-web-ping:2e
    2e: Pulling from diamol/ch03-web-ping
    c6a83fedfae6: Pull complete 
    286f203c853b: Pull complete 
    cc70de2ae229: Pull complete 
    a0b0347273f3: Pull complete 
    3dc512960c25: Pull complete 
    ed25aa9feb7f: Pull complete 
    Digest: sha256:b04842e14dab0afeb9304750f210bcf271bf18be4f8c16f55e6c0e776c5e911a
    Status: Downloaded newer image for diamol/ch03-web-ping:2e
    docker.io/diamol/ch03-web-ping:2e
    ```

- Run a container in background (`-d`, `--detach`), give the container a friendly name (`--name`).
  The application pings by default `blog.sixeyed.com.
  ```console
  $ docker container run -d --name web-ping diamol/ch03-web-ping:2e
  828051da279fec09bb76772ba0e4f8031b86fcde8a0bddbd2f69353d461441b4
  ```

- Show ping logs of the named container
  ```console
  $ docker container logs web-ping
  ** web-ping ** Pinging: blog.sixeyed.com; method: HEAD; 3000ms intervals
  Making request number: 1; at 1786724837350
  Got response status: 200 at 1786724837670; duration: 320ms
  Making request number: 2; at 1786724840352
  Got response status: 200 at 1786724840498; duration: 146ms
  Making request number: 3; at 1786724843352
  Got response status: 200 at 1786724843498; duration: 146ms
  ```

- Force-remove the container and run another container again with the `TARGET` environment variable (`--env`).
  Now the application pings `google.com`.
  ```console
  $ docker rm -f web-ping
  web-ping
  $ docker container run --env TARGET=google.com diamol/ch03-web-ping:2e
  ** web-ping ** Pinging: google.com; method: HEAD; 3000ms intervals
  Making request number: 1; at 1786725586126
  Got response status: 301 at 1786725586369; duration: 243ms
  Making request number: 2; at 1786725589129
  Got response status: 301 at 1786725589312; duration: 183ms
  Making request number: 3; at 1786725592130
  Got response status: 301 at 1786725592295; duration: 165ms
  ```