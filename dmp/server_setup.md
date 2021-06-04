## Server
```
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.2 LTS
Release:        20.04
Codename:       focal
```

## Update
```
sudo apt-get update
```

## Python3 pip
```
sudo apt install python3-pip
```

## pip installs
```
pip install pandas
pip install psycopg2-binary
pip install SQLAlchemy
```
For production, ought to use ```pip install psycopg2```,
which has some build requirements, eg a C compiler.

## PostgreSQL
```
sudo apt install postgresql postgresql-contrib
```
