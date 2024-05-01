```bash
$ python3 --version
Python 3.8.3

$ python3 -m venv venv

$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt

(venv) $ FLASK_APP=src/app.py \
    flask db upgrade \
    --directory=src/migrations/
(venv) $ python run_dev_server.py
```
