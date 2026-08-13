# Terms

## Core Concepts: Container, Image, Registry, Dockerfile, etc.

### Container

A *container* is an isolated environment for running an application together with the dependencies it needs.
It is created from a container image.

### Image

A *container image* is a read-only package that contains an application, its dependencies,
and the configuration needed to run it.
Images are used to create containers.

An image is not a single file.
A Docker image is composed of layers.

Docker images are portable across machines with a compatible OS/CPU platform
and a compatible container runtime.

### Registry

A *container registry* is a service for storing and distributing container images.
Images can be pushed to a registry and pulled from it to run containers on different machines.

### Docker Hub, Repository, Tag

A container registry is a service for storing and distributing container images.
Docker Hub is Docker's default public container registry.

A *repository* is a collection of related container images.
A *tag* is a human-readable label used to identify a particular image within a repository.

For example, `diamol/ch02-hello-diamol:2e` is an image reference 
that points to an image hosted on Docker Hub, 
where `diamol/ch02-hello-diamol` is a repository and `2e` is a tag.

### Dockerfile

A *Dockerfile* defines the base image, application files, dependencies, configuration,
and the command used to run the application.

#### Running a Container from an Image: From Registry to Running Container 

```
Registry
  ↓ (optionally: docker pull <repository>:<tag>)
Image
  ↓ docker run <repository>:<tag>
Container
```

Docker images are stored locally in *Docker's local image store*.
When `docker run` is executed, Docker first looks for the image locally.
If the image is not found, Docker automatically pulls it from the registry
and then creates and starts a container from it.

A container runs as long as its main application process is running.
When that process exits, the container stops.
The stopped container still exists and can be shown with `docker container ls -a`.

```
Container starts
  ↓
Application process runs
  ↓
Application process exits
  ↓
Container stops
```

#### Building and publishing an Image: From Dockerfile to Registry

```
Dockerfile
  ↓ docker build -t <repository>:<tag> .
Image
  ↓ docker push <repository>:<tag>
Registry
```

Here `-t`, `--tag` assigns a name and optionally a tag of the image.
The final `.` is the *build context*.
It tells Docker to use the current directory as the set of files available during the image build.

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

### Docker CLI and Docker Engine

The *Docker CLI* is a client that communicates with the *Docker Engine* through the *Docker API*.

The Docker Engine is the server-side container platform responsible for 
managing Docker objects such as images, containers, networks, and volumes.

### Docker Daemon

The Docker daemon (`dockerd`) is the main background process of Docker Engine.
It listens for Docker API requests and manages Docker resources.
