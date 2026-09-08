# Volume Mounts and Bind Mounts

## Lab 5

### Task

Create a small workflow that uses three independent container images 
and a shared Docker named volume to demonstrate persistent data storage.

- Create a named volume for storing a SQLite database.
- Build an initialization image that uses Alembic to create the database schema in the named volume.
- Build a seeding image that uses Faker to generate and insert 10 users into the existing database.
- Build a reading image that reads the users from the database and displays them as a Polars DataFrame.
- Run each image in a separate temporary container and mount the same named volume at `/data`.
- The containers must not depend on ech other's filesystem. 
  The SQLite database stored in the named volume is the only persistent data shared between them.
- Each container can be removed after completing its task, while the database continues to exist in the named volume. 

### Initiate the Database

- Create a named volume that will store the SQLite database independently of the containers
    ```console
    $ docker volume create fake-users-db
    fake-users-db
    ```

- Build the image responsible for initializing the database 
    ```console
    $ docker image build \
      -t db-init-image \
      -f db-init/Dockerfile \
      db-init
    ```

- Run a container from the image and mount the named volume at `/data`
    ```console
    $ docker container run --rm \
      --mount type=volume,source=fake-users-db,target=/data \
      db-init-image
    Skipping virtualenv creation, as specified in config file.
    ```
  - The container runs the Alembic migration and creates the SQLite database at `/data/app.db`.
  - Because `/data` is backed by the `fake-users-db` volume, the database persists after the container is removed.


### Seed the Database

- Build the image responsible for seeding the database
    ```console
    $ docker image build \
      -t db-seed-image \
      -f db-seed/Dockerfile \
      .
    ```

- Run a temporary container with the same volume mounted at `/data`
    ```console
    $ docker container run --rm \
      --mount type=volume,source=fake-users-db,target=/data \
      db-seed-image
    Skipping virtualenv creation, as specified in config file.
    ```
  - The container opens the existing `/data/app.db` database and inserts 10 fake users.
  - The container is removed after it exits, but the modified database remains in the volume.


### Read the Database

- Build the image responsible for reading the database
    ```console
    $ docker image build \
      -t db-read-image \
      -f db-read/Dockerfile \
      db-read
    ```

- Run another temporary container with the same volume
    ```console
    $ docker container run --rm \
      --mount type=volume,source=fake-users-db,target=/data \
      db-read-image
    shape: (10, 3)
    ┌─────┬───────────────────┬───────────────────────────┐
    │ id  ┆ name              ┆ email                     │
    │ --- ┆ ---               ┆ ---                       │
    │ i64 ┆ str               ┆ str                       │
    ╞═════╪═══════════════════╪═══════════════════════════╡
    │ 1   ┆ Bradley Phillips  ┆ ylynch@example.org        │
    │ 2   ┆ Katherine Bennett ┆ michael01@example.com     │
    │ 3   ┆ Brian Snyder      ┆ brian37@example.com       │
    │ 4   ┆ Lisa Kelly        ┆ vbowers@example.org       │
    │ 5   ┆ Anita Bailey      ┆ debrakaufman@example.org  │
    │ 6   ┆ Roger Williams    ┆ robertsjames@example.net  │
    │ 7   ┆ Mr. Victor Brooks ┆ youngscott@example.com    │
    │ 8   ┆ Jessica Vazquez   ┆ ericdawson@example.org    │
    │ 9   ┆ Beth Huang        ┆ christopher36@example.com │
    │ 10  ┆ Timothy Reynolds  ┆ oliviamurray@example.com  │
    └─────┴───────────────────┴───────────────────────────┘
    ```
  - The container reads the users from `/data/app.db` and prints them as a Polars DataFrame.