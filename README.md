# Ensure that secrets/credentials are handled/managed with care (aka "protected")

```bash
$ cp \
    .env.template \
    .env

# Fill out the contents of `.env.` according to the instructions therein.
```

# Create a virtual environment

```bash
$ python3 --version
Python 3.8.3

$ python3 -m venv venv

$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt

(venv) $ pre-commit install
```

# Launch the project

This section explain how to
use a container engine (such as Podman, Docker, etc.) to serve the persistence layer,
but use `localhost` (= the local network interface) to serve the web application.

(

If the container engine that you wish to use is Docker,
you "should" be able to use each of the following commands
by simply replacing `podman` with `docker` in each command.

The reason for the quotation marks in "should" is that
the commands in question are
<ins>actively monitored-and-controlled for correctness</ins>
only with the `podman` executable.

)

```bash
# Launch one terminal instance and, in it, start serving the persistence layer:
podman run \
    --name container-s-l-postgres \
    --mount type=volume,source=volume-s-l-postgres,destination=/var/lib/postgresql/data \
    --env-file .env \
    --publish 5432:5432 \
    postgres:15.1
```

(

OPTIONALLY, verify that the previous step did start serving a PostgreSQL server:

```bash
$ podman container exec \
   -it \
   container-s-l-postgres \
   /bin/bash
root@<container-id> psql \
    --host=localhost \
    --port=5432 \
    --username=<the-value-for-POSTGRES_USER-in-the-.env-file> \
    --password \
    <the-value-for-POSTGRES_DB-in-the-.env-file>

Password: 
psql (15.1 (Debian 15.1-1.pgdg110+1))
Type "help" for help.

<the-value-for-POSTGRES_DB-in-the-.env-file>=# \d
Did not find any relations.
```

)

```bash
# Launch a second terminal instance and, in it, do the following:

# (a) apply the database migrations:
(venv) $ PYTHONPATH=. \
    FLASK_APP=src \
        flask db upgrade

# (b) optionally, populate the database with some data:
(venv) $ PYTHONPATH=. \
    python src/scripts/script_2024_05_01_10_03_populate_db.py

# (c) start serving the application:
(venv) $ python run_dev_server.py
```
