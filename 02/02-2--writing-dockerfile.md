# Writing Dockerfile

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


- `COPY <source-path> <target-path>` copies a file from the Docker build context into the image.


- `CMD <JSON-array>` defines the default executable and arguments that Docker runs 
  when a container is started from the image. Here `node` starts the Node.js runtime, which executes `app.js`
  ```console
  $ node /web-ping/app.js
  ```