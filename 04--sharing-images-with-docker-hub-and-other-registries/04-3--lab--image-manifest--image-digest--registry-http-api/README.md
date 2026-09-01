# Sharing Images with Docker Hub and Other Registries

## Lab 4: Image Manifest and Registry HTTP API

The goal of this lab is to interact directly with a local Docker Registry using its HTTP API.

Tasks:
- retrieve an image manifest;
- create a new image tag using the manifest;
- verify that the new tag exists;
- delete the manifest by its digest;
- verify that the image tags have been removed.

### Image Manifest

An *image manifest* is a JSON document stored in a container registry that describes a specific image.

It contains references to:
- the image configuration;
- the filesystem layers that make up the image.

Each referenced object is identified by its digest.

A manifest also has its own digest, 
which uniquely identifies the manifest by its content.

```
Image tag
  ↓
Image manifest ← manifest digest
  |- config digest → config blob (binary large object)
  |
  |- layer digests
     |- layer digest → layer blob
     |- layer digest → layer blob
     |- layer digest → layer blob
```

Multiple tags can reference the same manifest and therefore refer to the same image.

Unlike a tag, which is a human-readable reference that can be changed,
a manifest digest is derived from the manifest content.

### Registry HTTP API

The *Registry HTTP API* is a REST API for communicating directly with a container registry over HTTP.

It provides programmatic access to registry resources such as:
- repositories;
- tags;
- image manifests;
- blobs and filesystem layers.

The API can be used to query and manage registry content without using the Docker CLI.

Examples:
- `GET`: `/v2/<repository>/tag/list`
- `GET`: `/v2/<repository>/manifests/<tag/digest>`
- `PUT`: `/v2/<repository>/manifests/<tag>`
- `DELETE`: `/v2/<repository>/manifests/<digest>`

HTTP clients such as `curl` can be used to send requests directly to the Registry HTTP API.

#### Why Use the Registry HTTP API?

- Docker CLI provides convenient high-level commands for common operations
  such as pushing and pulling images, but it does not expose every registry
  operation.

- The Registry HTTP API provides direct programmatic access to repositories, tags, manifest,
  and blobs, and is useful for automation and registry management.

### Check that the Local Docker Registry is Running and Contains an Image

```console
$ docker container ls --filter name=local-registry
CONTAINER ID   IMAGE        COMMAND                  CREATED       STATUS        PORTS                                         NAMES
012d1244ae2f   registry:3   "/entrypoint.sh /etc…"   10 days ago   Up 28 hours   0.0.0.0:5010->5000/tcp, [::]:5010->5000/tcp   local-registry
```

```console
$ docker image ls --filter reference="*/hello-from-rust"
                                                                                                    i Info →   U  In Use
IMAGE                               ID             DISK USAGE   CONTENT SIZE   EXTRA
axvadev/hello-from-rust:v1          39064a5d2bf1       75.2MB             0B        
localhost:5010/hello-from-rust:v1   39064a5d2bf1       75.2MB             0B    
```

### Get the Image Manifest

The Docker Registry HTTP API can be used to retrieve the manifest associated with an image tag.

This command sends an HHTP `GET` request to the local Docker Registry and requests the manifest 
associated with the `v1` tag of the `hello-from-rust` repository.

```console
$ curl -i \
  -H "Accept: application/vdn.docker.distribution.manifest.v2+json" \
  http://localhost:5010/v2/hello-from-rust/manifests/v1
HTTP/1.1 200 OK
Content-Length: 945
Content-Type: application/vnd.docker.distribution.manifest.v2+json
Docker-Content-Digest: sha256:712c69b22340cd5f9639de58049b6bd476d251c3a947091374a5825186e8d6c9
Docker-Distribution-Api-Version: registry/2.0
Etag: "sha256:712c69b22340cd5f9639de58049b6bd476d251c3a947091374a5825186e8d6c9"
Date: Tue, 01 Sep 2026 19:26:33 GMT

{
   "schemaVersion": 2,
   "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
   "config": {
      "mediaType": "application/vnd.docker.container.image.v1+json",
      "size": 1058,
      "digest": "sha256:39064a5d2bf16574d97dfca002d70d3d91aa2b70eae8871fdb681336bd646d11"
   },
   "layers": [
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 29148307,
         "digest": "sha256:e4376313f4ed09af5cb5e63d27312153c9adce82fc4c8f8edb966f0ed6e49db5"
      },
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 93,
         "digest": "sha256:769c0331bf7310c588fdf816b04d5de9532051b40a331bd2a997e9289904a584"
      },
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 192604,
         "digest": "sha256:568f18af55100c7089b944197cbede2c368246287dc97961b6cbc9104997d513"
      }
   ]
}
```

Here:
- `curl` - sends an HTTP request.
- `-i` (`--include`) - includes the HTTP response headers in the output.
- `-H` (`--header`) - adds a custom HTTP request header.
- `"Accept: application/vdn.docker.distribution.manifest.v2+json"` - requests a Docker Image Manifest Schema 2 response.
- `http://localhost:5010` - sets the local Docker Registry.
- `/v2/` - sets Docker Registry HTTP API V2.
- `/hello-from-rust/` - sets the repository name.
- `/manifests/v1` - requests the manifest referenced by the `v1` tag.

- A successful response contains both HTTP headers and the manifest JSON.
- The `Docker-Content-Digest` header contains the digest of the manifest.

### Save the manifest to a JSON file

```console
$ curl \
  -H "Accept: application/vdn.docker.distribution.manifest.v2+json" \
  http://localhost:5010/v2/hello-from-rust/manifests/v1 \
  -o manifest.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   945  100   945    0     0   132k      0 --:--:-- --:--:-- --:--:--  153k
```

### Create a New Image Tag Using the Manifest

An existing manifest can be sent back to the registry under a new tag.

This command sends the previously downloaded manifest to the `hello-from-rust` repository
and creates the new tag `v1.0.0`

```console
$ curl -i \
  -X PUT \
  -H "Content-Type: application/vnd.docker.distribution.manifest.v2+json" \
  --data-binary @manifest.json \
  http://localhost:5010/v2/hello-from-rust/manifests/v1.0.0
HTTP/1.1 201 Created
Docker-Content-Digest: sha256:712c69b22340cd5f9639de58049b6bd476d251c3a947091374a5825186e8d6c9
Docker-Distribution-Api-Version: registry/2.0
Location: http://localhost:5010/v2/hello-from-rust/manifests/sha256:712c69b22340cd5f9639de58049b6bd476d251c3a947091374a5825186e8d6c9
Date: Tue, 01 Sep 2026 19:34:26 GMT
Content-Length: 0
```

Here:
- `-i` (`--include`) - includes the HTTP response header in the output.
- `-X PUT` (`--request PUT`) - sends an HTTP `PUT` request.
- `-H "Content-Type: application/vnd.docker.distribution.manifest.v2+json"` - tells the registry 
  that the request body contains a Docker Image Manifest Schema 2.
- `--data-binary @manifest.json` - reads `manifest.json` and sends its contents as the HTTP request body without modifying them.
- `/v2/hello-from-rust/manifests/v1.0.0` - stores the manifest under the new `v1.0.0` tag. 

The image layers are not uploaded again because they already exist in the registry.
The new tag references the same manifest, so both tags refer to the same image.

### List Tags

```console
$ curl http://localhost:5010/v2/hello-from-rust/tags/list
{"name":"hello-from-rust","tags":["v1","v1.0.0"]}
```

### Delete the Image from the Local Docker Registry

Deleting an image through the Registry API means deleting its manifest by digest.

If multiple tags reference the same manifest, deleting that manifest removes all of those tag references.

The referenced layers may still remain in the registry storage
until garbage collection removes unreferenced blobs.

```console
$ curl -i \
  -X DELETE \
  http://localhost:5010/v2/hello-from-rust/manifests/sha256:712c69b22340cd5f9639de58049b6bd476d251c3a947091374a5825186e8d6c9
HTTP/1.1 202 Accepted
Docker-Distribution-Api-Version: registry/2.0
Date: Tue, 01 Sep 2026 19:38:54 GMT
Content-Length: 0
```

### No Tags Can Be Found

```console
$ curl http://localhost:5010/v2/hello-from-rust/tags/list
{"name":"hello-from-rust","tags":null}
```