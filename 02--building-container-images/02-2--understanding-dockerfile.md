# Understanding a Dockerfile

- `Dockerfile` (no file extension)
    ```dockerfile
    FROM diamol/node:2e
    
    ENV TARGET=blog.sixeyed.com
    ENV METHOD=HEAD
    ENV INTERVAL=3000
    
    WORKDIR /web-ping
    COPY app.js .
    
    CMD ["node", "/web-ping/app.js"]
    ```

- `FROM <image>` specifies the *base image*.
  The new image starts from `diamol/node:2e`,
  which already contains the filesystem and Node.js
  runtime required to run the application.


- `ENV <VARIABLE>=<value>` defines default *environment variables*
  for containers created from the image.

  The application reads them through Node.js in `app.js`
  ```javascript
  process.env.TARGET
  process.env.METHOD
  process.env.INTERVAL
  ```
  
  These values are defaults stored in the image configuration
  and can be overridden when a container is created

  ```console
  $ docker container run --env TARGET=google.com diamol/ch03-web-ping:2e
  ```
  
  The image itself is not modified. The new value belongs to the container configuration.


- `WORKDIR <current-working-directory>` sets the current working directory 
  for the following Dockerfile instructions and for the application at runtime.


- `COPY <source-path-1> <source-path-2> ... <target-path>` 
  copies files or the contents of directories from the Docker build context into the image.

  - Note: `COPY app .` copies the content of the `app` directory from the Docker build context
    into the current working directory in the image. 
    The source path (`app`) is relative to the Docker build context.
    The target path (`.`) refers to the current `WORKDIR`.
  
  - Files that should not be copied can be excluded using `.dockerignore`.
  
  - It is also common to copy dependency files separately before copying the application code.
    This allows Docker to reuse the layer containing installed dependencies 
    when the application code changes but requirements do not. 


- `CMD <JSON-array>` defines the default executable and arguments that Docker runs 
  when a container is started from the image. Here `node` starts the Node.js runtime, which executes `app.js`
  ```console
  $ node /web-ping/app.js
  ```