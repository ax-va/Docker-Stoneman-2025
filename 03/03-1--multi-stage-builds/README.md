# Multi-Stage Builds

- A *multi-stage build* allows different environments to be used during the image build
  while keeping only what is needed in the final image.

- Each `FROM <image>` starts a new build stage. A stage can optionally be named with `AS <stage>`.

- Files and build artifacts can be copied from one stage to another using 
  `COPY --from=<stage> <source-path> <target-path>`.

- Individual stages are isolated.
  The output in the final stage will only contain what you explicitly copy from earlier stages.

- This is useful when building an application requires tools
  that are not needed at runtime, such as compilers, build tools, source files, or development dependencies.

- As a result, the final image can contain only the application and its runtime dependencies,
  making it smaller and avoiding unnecessary build tools in the runtime image.

- Example of a multi-stage Dockerfile:
    ```dockerfile
    FROM diamol/base:2e AS build-stage
    RUN echo 'Building...' > /build.txt
    
    FROM diamol/base:2e AS test-stage
    COPY --from=build-stage /build.txt /build.txt
    RUN echo 'Testing...' >> /build.txt
    
    FROM diamol/base:2e
    COPY --from=test-stage /build.txt /build.txt
    CMD ["cat", "/build.txt"]
    ```

- Build an image from the above Dockerfile
  ```console
  $ docker image build -t multi-stage .
  [+] Building 0.6s (9/9) FINISHED                                                                                                                                                                           docker:default
   => [internal] load build definition from Dockerfile                                                                                                                                                                 0.0s
   => => transferring dockerfile: 318B                                                                                                                                                                                 0.0s
   => [internal] load metadata for docker.io/diamol/base:2e                                                                                                                                                            0.0s
   => [internal] load .dockerignore                                                                                                                                                                                    0.0s
   => => transferring context: 2B                                                                                                                                                                                      0.0s
   => [build-stage 1/2] FROM docker.io/diamol/base:2e                                                                                                                                                                  0.0s
   => [build-stage 2/2] RUN echo 'Building...' > /build.txt                                                                                                                                                            0.2s
   => [test-stage 2/3] COPY --from=build-stage /build.txt /build.txt                                                                                                                                                   0.0s
   => [test-stage 3/3] RUN echo 'Testing...' >> /build.txt                                                                                                                                                             0.2s
   => [stage-2 2/2] COPY --from=test-stage /build.txt /build.txt                                                                                                                                                       0.0s
   => exporting to image                                                                                                                                                                                               0.0s
   => => exporting layers                                                                                                                                                                                              0.0s
   => => writing image sha256:4a306ee02dd6af0c019d48223340af30b7e9d270788a7f1840cb971b91cbb1d5                                                                                                                         0.0s
   => => naming to docker.io/library/multi-stage 
  ```

- Run a container from the image
  ```console
  $ docker container run --rm multi-stage
  Building...
  Testing...
  ```