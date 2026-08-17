# Multi-Stage Build: An Example with Rust

- Multi-stage build separates the build environment from the runtime environment.
  The build stage can contain compliers, build tools, source code, and other build-time dependencies,
  while the final stage contains only the artifacts and runtime dependencies needed to run the application.

- Dockerfile

    ```Dockerfile
    # build stage
    FROM rust:1.83-slim-bookworm AS builder
    
    WORKDIR /project
    
    COPY project .
    RUN cargo build --release
    
    # runtime stage
    FROM debian:bookworm-slim
    
    WORKDIR /app
    
    COPY --from=builder /project/target/release/rust-service /app
    
    ENTRYPOINT ["./rust-service"]
    ```

  - `FROM rust:1.83-slim-bookworm AS builder` starts a new build stage named `builder`.
  
    - The base image contains the Rust toolchain needed to build the application, including:
      - `rustc` - the Rust compiler;
      - `cargo` - the Rust build and package tool;
      - Debian Bookworm user space.
  
    - This environment is needed only during the build and will not become the final runtime image.

  - `WORKDIR /project` sets `/project` as the current working directory inside the `builder` stage.
    The following relative paths and commands are evaluated from this directory.

  - `COPY project .` copies the contents (excluding ones in `.dockerignore`) 
    of the `project` directory from the Docker build context into `/project` inside the `builder` stage.

  - `RUN cargo build --release` complies the dependencies and the Rust source code in release mode.
    - The resulting native executable is created at `/project/target/release/rust-service`.
    - At this point, the `builder` stage contains Rust, Cargo, the source code, dependencies,
      intermediate build files, and the final binary.

  - `FROM debian:bookworm-slim` starts a completely new stage with a fresh filesystem.
    - This stage is isolated from the `builder` stage.
    - It contains only Debian runtime environment until files are explicitly copied into it.

  - `WORKDIR /app` sets `/app` as the working directory of the final image and of containers created from it.

  - `COPY --from=builder /project/target/release/rust-service /app` copies the compiled `rust-service` executable
    from the `builder` stage into the final stage. 
    The important point is that Docker does not copy the whole builder stage.

  - `ENTRYPOINT ["./rust-service"]` defines the executable that Docker starts when a container is created from the image.


- Build the image
    ```console
    $ docker image build -t rust-example .
    ```


- Show the image
    ```console
    $ docker image ls rust-service
                                                                                                    i Info →   U  In Use
    IMAGE                 ID             DISK USAGE   CONTENT SIZE   EXTRA
    rust-service:latest   a12734f653d0       75.2MB             0B      
    ```


- Run a container from the image
    ```console
    $ docker container run --rm rust-service
    Hello from Rust!
    ```


