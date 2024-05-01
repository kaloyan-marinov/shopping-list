```bash
$ python3 --version
Python 3.8.3

$ python3 -m venv venv

$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt

(venv) $ pre-commit install

$ cp \
    .env.template \
    .env

# Fill out the contents of `.env.` according to the instructions therein.
```

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
(venv) $ PYTHONPATH=. \
    FLASK_APP=src \
        flask db upgrade
(venv) $ PYTHONPATH=. \
    python src/scripts/script_2024_05_01_10_03_populate_db.py
(venv) $ python run_dev_server.py
```
