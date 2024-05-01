```bash
$ python3 --version
Python 3.8.3

$ python3 -m venv venv

$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt

(venv) $ PYTHONPATH=. \
    FLASK_APP=src \
        flask db upgrade
(venv) $ PYTHONPATH=. \
    python src/scripts/script_2024_05_01_10_03_populate_db.py
(venv) $ python run_dev_server.py
```
