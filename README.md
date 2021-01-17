# TrainingREST
Django REST API course - O'Reilly - DRF


## Setting up PostgreSQL

1. Create the DB and the user that will access that DB

```sql
CREATE DATABASE my_db;
CREATE USER user WITH PASSWORD 'pass';
ALTER ROLE user SET client_encoding TO 'utf8';
ALTER ROLE user SET default_transaction_isolation TO 'read committed';
ALTER ROLE user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE my_db TO root;
```

2. Install the supporting package

```shell
pip install django psycopg2
```

3. Setup the DB in the settings

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_db',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

## Set up the DRF

1. Add 'rest_framework' to the list of the installed apps
2. Create url and view for the model, etc.