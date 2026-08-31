# Terms

## Core Concepts: Container, Image, Registry, Dockerfile, etc.

### Container

A *container* is an isolated environment for running an application together with the dependencies it needs.
It is created from a container image.

The container provides the application with its own hostname, filesystem, 
and usually network configuration (including an IP address), while sharing the host OS kernel 
(e.g., the Linux kernel of your Ubuntu machine).

### Image

A *container image* is a read-only package that contains an application, its dependencies,
and the configuration needed to run it.
Images are used to create containers.

An image is not a single file.
A Docker image is composed of layers.

Docker images are portable across machines with a compatible OS/CPU platform
and a compatible container runtime.

### Image Layer

A Docker image consists of multiple read-only *image layers* stacked together.

For example, conceptually:

```console
Layer 1: base Debian user space (filesystem, system libraries and utilities)
Layer 2: Python runtime (CPython 3.12 for Linux/amd64)
Layer 3: application dependencies (FastAPI 0.138.0, Uvicorn 0.51.0, SQLAlchemy 2.0.51, ...)
Layer 4: application code
```

A single logical layer shown in this example may actually consist of multiple Docker image layers.
Together, these layers form a single Docker image.

Also, Docker image contains the distribution's user space, not its own Linux kernel.
Linux containers share the kernel provides by the host environment.
The container's Linux distribution does not have to be the same as the host's distribution.
For example, a Debian user space can run on the Linux kernel provided by an Ubuntu host.

#### Layers Can Be Shared and Reused Between Different Images

Docker image layers allow filesystem content to be cached, shared, and reused between builds and images,
making image building, storage, and distribution more efficient. 

### Container Writable Layer

When a container is created from an image,
Docker adds a writable container layer on top of the read-only image layers.

For example:

```console
Container writable layer
Layer 4: application code
Layer 3: application dependencies
Layer 2: Python runtime
Layer 1: base Linux user space
```

### Docker Engine, Docker Daemon, and Docker CLI

*Docker Engine* provides the core Docker functionality for managing resources, 
such as images, containers, networks, and volumes.

The *Docker CLI* does not manage these resources directly.
It communicates with Docker Engine through the *Docker API*,
which is a standard HTTP-based REST API.

The Docker daemon (`dockerd`) is the main background process of Docker Engine
It runs as a system service, listens for Docker API requests, and manages Docker resources.

```
Docker CLI → Docker API → Docker daemon (dockerd) → Docker resources
```

### Registry, Docker Hub

- An *image registry* is a service for storing and distributing container images.
Images can be pushed to a registry and pulled from it to run containers on different machines.

- *Docker Hub* is Docker's default public image registry.

### Image Reference: Owner Namespace, Repository, Tag

- An *owner namespace* identifies a user or organization that owns a repository
  and provides a namespace for its repository names.

- A *repository* is a collection of related container images.

- A *tag* is a human-readable label used to identify a particular image within a repository.
  A repository can contain images with multiple tags, typically used to identify different versions or variants.
  Multiple tags can point to the same image.
  The `latest` tag does not automatically point to the newest image.
  It is a regular tag that must be explicitly assigned or updated.

For example, `axvadev/hello-from-rust:v1` is an *image reference* 
that points to an image hosted on Docker Hub, 
where `axvadev` is an owner namespace (Docker ID), 
`hello-from-rust` is a repository, and `v1` is a tag.
If no tag is specified in an image reference, Docker uses `latest` by default.

The fully qualified image reference for this image is `docker.io/axvadev/hello-from-rust:v1`,
which explicitly includes the registry domain. 
For Docker Hub, the registry domain can normally be omitted.

A Docker image can exist locally in the Docker Engine without being stored in any registry.
A registry is only needed when you want to store and distribute the image remotely.

- Local image: `hello-from-rust:v1`
- Docker Hub: `axvadev/hello-from-rust:v1`
- Local Docker registry: `localhost:5010/hello-from-rust:v1`


### Semantic Versioning for Image Tags

Docker image tags can be used to identify different versions of an application.

A common convention is *Semantic Versioning*: `<major>.<minor>.<patch>`.

For example:

- `3.2.101`
  - `major` (`3`): May contain breaking changes or significant changes in functionality.
  - `minor` (`2`): Adds new functionality while remaining backward compatible with the same major version.
  - `patch` (`101`): Contains backward-compatible bug fixes or small changes that do not introduce new functionality.

Note:
- Docker does not understand version semantics.
- Tags such as `3`, `3.2`, `3.2.101`, and `latest` are just strings.
- Docker does not automatically upate them - each tag must be explicitly assigned to an image.


### Dockerfile

A *Dockerfile* defines the base image, application files, dependencies, configuration,
and the command used to run the application.

### Build, Share, Run Workflow

#### Building and publishing an Image: From Dockerfile to Registry

```
Dockerfile
  ↓ docker build -t <image-refernce> .
Image
  ↓ docker push <image-refernce>
Registry
```

Here `-t`, `--tag` assigns a name and optionally a tag of the image.
The final `.` is the *build context*.
It tells Docker to use the current directory as the set of files available during the image build.

Docker can reuse previously available image layers and cached build results when building an image,
so unchanged parts of the image do not need to be rebuilt.

The same read-only filesystem layers can also be shared between multiple images,
so identical layer content does not need to be stored multiple times.

#### Running a Container from an Image: From Registry to Running Container 

```
Registry (by default, Docker Hub)
  ↓ (optionally: docker pull <image-refernce>)
Image (stored locally; filesystem content is organized into read-only layers)
  ↓ docker run <image-refernce>
  ↓ + writable conatiner layer
Container
```

Docker images are stored locally.

Already downloaded images can be reused to create multiple containers without downloading the image again.
When `docker run` is executed, Docker first looks for the image locally.
If the image is not found locally, Docker automatically pulls it from the registry
and then creates and starts a container from it.

When a container is created, Docker adds a writable container layer on top of the image's read-only filesystem layers.

A container runs as long as its main application process is running.
When that process exits, the container stops.
The stopped container still exists and can be shown with `docker container ls -a` (`-a`, `--all`).

`docker run` creates and starts a new container from an image
and, by default, attaches its standard output and error to the terminal,
whereas `docker container start` starts an existing stopped container
without attaching to its output by default.
You can attach the container's `stdout`/`stderr` to the terminal with `docker container start -a` (`-a`, `--attach`).

```
Container starts
  ↓
Application process runs
  ↓
Application process exits
  ↓
Container stops
```

### Monoliths, Containers, and Microservices: From Monolith to Distributed System

Containers allow a monolithic application to be modernized incrementally 
by moving individual features into independently deployable containers
without rewriting the entire application.

A container is not a microservice.
A monolith can run in a container, and a multi-container application 
is not necessary a microservice architecture.

### Disposable Containers

Containers are designed to be replaceable.
Instead of modifying a running container, 
we typically replace it with a new container created from an image.

### Container Platform Compatibility

Container images are built for a specific operating system and CPU architecture,
such as linux/amd64 or linux/arm64.

### Container Orchestration

Container orchestration is the automated deployment, scaling, networking, and
management of containerized applications across multiple machines.
This is not a task of Docker (containers) or Docker Compose (multi-container applications), 
but typically a task of Kubernetes.

### OCI = Open Container Initiative

The *Open Container Initiative (OCI)* is an open standards organization 
that defines specifications for container images and container runtimes.

OCI standards allow different container tools to build and run compatible container images.

Docker is a container platform, but Docker and containers are not the same thing.
Containers are based on open standards and can be built and run using different tools.

A container does not require Docker specially.

### (Optional: Serverless)

Serverless is a cloud computing model where developers deploy application code or functions
while the platform manages the underlying infrastructure, execution environment, and scaling.

Serverless does not mean there are no servers.
It means developers do not manage those servers directly.

Serverless platforms may use containers or other isolation technologies internally,
and some allow developers to deploy container images.
But serverless itself is not a container technology.

### Interactive Container

We can start a container in *interactive mode* and enter its isolated environment to execute commands inside it.

```console
$ docker run -it axvadev/hello-from-rust:v1
```

Here 
- `-i`, `--interactive` keeps the container's standard input (`stdin`) open;
- `-t`, `--tty` allocates a pseudo-terminal (TTY).

After container starts, the terminal is connected to a shell running inside the container.
Commands entered there are executed in the container's environment,
with its filesystem, hostname, network configuration, etc.

`-it` does not automatically start a shell.
It connects your terminal to the process started by the container.
If that process is a shell, you get an interactive shell session.

```console
/ # 
```

Close the terminal session
```console
/ # exit
```

### BuildKit

*BuildKit* is Docker's modern build engine.
It analyzes the dependencies between Dockerfile instructions and build stages,
allowing independent work to be executed in parallel
and unnecessary stages to be skipped.

BuildKit also provides more efficient build caching and additional features
such as cache mounts and secret mounts, which can make builds faster and more secure.

### Multi-Stage Builds

- A *multi-stage build* allows different environments to be used during the image build
  while keeping only what is needed in the final image.

- Each `FROM <image-reference>` starts a new build stage. A stage can optionally be named with `AS <stage>`.

- Files and build artifacts can be copied from one stage to another using 
  `COPY --from=<stage> <source-path> <target-path>`.

- Individual stages are isolated.
  The output in the final stage will only contain what you explicitly copy from earlier stages.

- This is useful when building an application requires tools
  that are not needed at runtime, such as compilers, build tools, source files, or development dependencies.

- As a result, the final image can contain only the application and its runtime dependencies,
  making it smaller and avoiding unnecessary build tools in the runtime image.

- A multistage build is a dependency graph rather than a strictly sequential process.
  BuildKit can execute independent stages in parallel.
  If one stage depends on another, for example through `COPY --from`,
  it must wait when it reaches that dependency.

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

### Docker Networks

- A *Docker network* allows containers to communicate with each other.

- Containers connected to the same user-defined Docker network can reach each other using
  *container names* instead of IP addresses.

- Docker provides an internal *DNS service* 
  that resolves a container name to its IP address inside the network.

### Docker Compose

- *Docker Compose* is used to define and manage multi-container applications.

- Instead of manually creating networks and starting each container with separate Docker commands,
  the application services, networks, volumes, environment variables, ports, and other configuration
  can be described in a `compose.yaml` file and managed together.

- Docker Compose does not replace Docker networks.
  By default, Compose creates a network for the application and connects its services to that network,
  allowing them to communicate using service names.