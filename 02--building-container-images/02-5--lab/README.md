# Building Container Images

## Lab 2

Task:
Append your name to `/diamol/ch03.txt` in a container built from the `diamol/ch03-lab:2e`
and create a new Docker image with the updated text file, but without using a Dockerfile.


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
   $ docker container commit --help
   Usage:  docker container commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
   
   Create a new image from a container's changes
   
   Aliases:
     docker container commit, docker commit
   
   Options:
     -a, --author string    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
     -c, --change list      Apply Dockerfile instruction to the created image
     -m, --message string   Commit message
         --no-pause         Disable pausing container during commit
   ```

3. 
   ```console
   $ docker container run -it --name lab2 diamol/ch03-lab:2e
   Unable to find image 'diamol/ch03-lab:2e' locally
   2e: Pulling from diamol/ch03-lab
   f18232174bc9: Already exists 
   09727307b25b: Pull complete 
   01249d7ff344: Pull complete 
   d4838e5e3af0: Pull complete 
   Digest: sha256:8e5e4de2dfd96739c2f8795920821f28194353ff054597c8c4c8c08c54512ce2
   Status: Downloaded newer image for diamol/ch03-lab:2e
   /diamol # echo "AxVa" >> /diamol/ch03.txt
   /diamol # cat /diamol/ch03.txt
   DIAMOL 2e
   Chapter 03
   Lab solution, by: AxVa
   /diamol # exit
   ```

4.
   ```console
   $ docker container commit lab2 new-lab2-image
   sha256:3db4ed9623cb46039a005bdf08f1b5973cc252b1c4f13a8f22751716c92450c3
   ```

5.   
    ```console
    $ docker container rm -f lab2
    lab2
    ```

6.
   ```console
   $ docker container run --rm new-lab2-image cat /diamol/ch03.txt
   DIAMOL 2e
   Chapter 03
   Lab solution, by: AxVa
   ```
   - `-rm` automatically removes the container after its main process exits.
   - A command specified after the image name overrides the image's `CMD`.
     If the image has an `ENTRYPOINT`, the command is passed as arguments to that `ENTRYPOINT`, e.g.,
     ```dockerfile
     ENTRYPOINT ["python"]
     CMD ["app.py"]
     ```
     Then `docker run my-image`executes `python app.py`, but `docker run my-image test.py` executes `python test.py`.