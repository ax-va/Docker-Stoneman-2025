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

### Running a Container from an Image: From Registry to Running Container 

```
Registry
  |
  | (optionally: docker pull)
  ↓
Image
  |
  | docker run
  ↓
Container
```

### Building and publishing an Image: From Dockerfile to Registry

```
Dockerfile
  |
  | docker build
  ↓
Image
  |
  | docker push
  ↓
Registry
```