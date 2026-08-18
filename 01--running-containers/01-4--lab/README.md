# Building Container Images

## Lab 1

Task:
Run the website from a container and replace its `index.html` with your `index.html`
so that the website displays a different home page.

1.
    ```console
    $ docker container --help
    Usage:  docker container COMMAND
    
    Manage containers
    
    Commands:
      attach      Attach local standard input, output, and error streams to a running container
      commit      Create a new image from a container's changes
      cp          Copy files/folders between a container and the local filesystem
      create      Create a new container
      diff        Inspect changes to files or directories on a container's filesystem
      exec        Execute a command in a running container
      export      Export a container's filesystem as a tar archive
      inspect     Display detailed information on one or more containers
      kill        Kill one or more running containers
      logs        Fetch the logs of a container
      ls          List containers
      pause       Pause all processes within one or more containers
      port        List port mappings or a specific mapping for the container
      prune       Remove all stopped containers
      rename      Rename a container
      restart     Restart one or more containers
      rm          Remove one or more containers
      run         Create and run a new container from an image
      start       Start one or more stopped containers
      stats       Display a live stream of container(s) resource usage statistics
      stop        Stop one or more running containers
      top         Display the running processes of a container
      unpause     Unpause all processes within one or more containers
      update      Update configuration of one or more containers
      wait        Block until one or more containers stop, then print their exit codes
    
    Run 'docker container COMMAND --help' for more information on a command.
    ```

2. 
    ```console
    $ docker container cp --help
    Usage:  docker container cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
            docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
    
    Copy files/folders between a container and the local filesystem
    
    Use '-' as the source to read a tar archive from stdin
    and extract it to a directory destination in a container.
    Use '-' as the destination to stream a tar archive of a
    container source to stdout.
    
    Aliases:
      docker container cp, docker cp
    
    Options:
      -a, --archive       Archive mode (copy all uid/gid information)
      -L, --follow-link   Always follow symlinks in SRC_PATH
      -q, --quiet         Suppress progress output during copy. Progress output is automatically suppressed if no terminal is attached
    ```

3. 
    ```console
    $ docker container run -d -p 8088:80 diamol/ch02-hello-diamol-web:2e
    8de0a370b7a67a0b60bea5508975434eb833000ed24ff3f46b9b9d37867df523
    ```

4. 
    ```console
    $ docker container cp index.html 8de0:/usr/local/apache2/htdocs/index.html
    Successfully copied 25B (transferred 2.05kB) to 8de0:/usr/local/apache2/htdocs/index.html
    ```

5. 
    Browse to http://localhost:8088 on a browser.

6.     
    ```console
    $ docker container stop 8de0
    8de0
    ```