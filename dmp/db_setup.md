## Start PostgreSQL server and get into psql
```
sudo service postgresql start
sudo -u postgres psql
```

## Make a password
```
\password postgres
```

## Stock staging DB
Use to hold stock data gotten from API.
```
create database stock_staging;
```
