# HealthApplication

This is the repository for the ELEC5622 Health Application


## Installation Instructions

### Requirements

* Python 3
* Redis server
* PostgreSQL

### Python packages

* `pip3 install django`
* `pip3 install django-channels`
* `pip3 install psycopg2`
* `pip3 install channels`
* `pip3 install asgiref==2.3`
* `pip3 install channels_redis`

## Runtime instructions

### First time setup
* Ensure redis is running with `redis-cli ping`. The server should respond with `PONG`
* Ensure PostgreSQL is running with `psql`.
* Ensure you have executed the SQL commands in `sql-files\setup-db.sql`

### Running
* Run the server with `python3 mysite/manage.py runserver`
* The server is accessible at `http://localhost:8000/ehealth/`