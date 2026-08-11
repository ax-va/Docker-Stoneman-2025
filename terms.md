# Terms

## Core Concepts: Container, Image, Registry, Dockerfile

### Container

A *container* is an isolated environment for running an application together with the dependencies it needs.
It is created from a container image.

### Image

A *container image* is a read-only package that contains an application, its dependencies,
and the configuration needed to run it.
Images are used to create containers.

### Registry

A *container registry* is a service for storing and distributing container images.
Images can be pushed to a registry and pulled from it to run containers on different machines.


### Dockerfile

A *Dockerfile* defines the base image, application files, dependencies, configuration,
and the command used to run the application.

#### Running a Container from an Image: From Registry to Running Container 

```
Registry
  ↓ (optionally: docker pull)
Image
  ↓ docker run
Container
```

#### Building and publishing an Image: From Dockerfile to Registry

```
Dockerfile
  ↓ docker build
Image
  ↓ docker push
Registry
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

### Docker CLI and Docker Engine

The *Docker CLI* is a client that sends commands to the *Docker Engine* through the *Docker API*.

The Docker Engine is the server that manages Docker objects such as images, containers, networks, and volumes.

```shell
Docker CLI (Client)

```